#!/usr/bin/env python3
"""
Trading Knowledge Vault - deterministic knowledge pipeline.

Purpose:
- Scan 07_Sources/*.md
- Extract wiki links, headings, module IDs, hypotheses, decisions and key terms
- Create/update generated index files under 00_Index, 02_Hypotheses, 03_Modules, 08_Glossary

This script does not call any external API. It is safe to run locally.
"""

from __future__ import annotations

import argparse
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Iterable

VAULT_DIRS = {
    "sources": "07_Sources",
    "concepts": "01_Concepts",
    "hypotheses": "02_Hypotheses",
    "modules": "03_Modules",
    "decisions": "06_Decisions",
    "glossary": "08_Glossary",
    "index": "00_Index",
}

KNOWN_TERMS = {
    "Market Microstructure": "Market Microstructure — мікроструктура ринку — внутрішня механіка ринку: стакан, угоди, спред, ліквідність, виконання.",
    "Order Book": "Order Book — стакан заявок — список лімітних заявок на купівлю і продаж.",
    "Tape": "Tape / Prints — стрічка угод — фактично виконані угоди.",
    "Liquidity": "Liquidity — ліквідність — доступний обсяг для входу/виходу без сильного руху ціни.",
    "Spread": "Spread — спред — різниця між найкращою ціною купівлі та продажу.",
    "Delta": "Delta — дельта — агресивні покупки мінус агресивні продажі.",
    "CVD": "CVD — cumulative volume delta — накопичена дельта за період.",
    "Imbalance": "Imbalance — дисбаланс — значна перевага одного боку потоку або стакану над іншим.",
    "Absorption": "Absorption — поглинання — великий агресивний потік не рухає ціну, бо протилежна ліквідність його поглинає.",
    "Iceberg Order": "Iceberg Order — айсберг-заявка — прихований великий ордер, де видима лише мала частина.",
    "Refill": "Refill — автопоповнення заявки — заявка виконується і швидко з'являється знову.",
    "Quote Walking": "Quote Walking — рухома заявка — великий ордер систематично рухається за ціною.",
    "Liquidity Wall": "Liquidity Wall — стіна ліквідності — велика концентрація заявок на рівні.",
    "Liquidity Removal Event": "Liquidity Removal Event — зняття ліквідності — різке зникнення заявок зі стакану.",
    "Spoofing": "Spoofing — фальшива ліквідність — велика заявка впливає на поведінку ринку, потім знімається.",
    "Inventory Arbitrage": "Inventory Arbitrage — інвентарний арбітраж — активи лежать на двох біржах, купівля/продаж виконуються одночасно без негайного переказу.",
    "Transfer Constraint Premium": "Transfer Constraint Premium — премія обмеження переказу — різниця цін через закритий депозит/вивід або дефіцит монети.",
    "Stale Quote": "Stale Quote — застаріла котировка — одна біржа вже змінила ціну, інша ще ні.",
    "Range Bot": "Range Bot — бот діапазону — алгоритм, який купує/продає всередині вузького коридору.",
}

MODULE_RE = re.compile(r"\b(?:OF|ARB|SCALP|MICRO|REPLAY|VALIDATION|DISCOVERY)_[0-9A-Z_]+\b")
WIKILINK_RE = re.compile(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.MULTILINE)
HYPOTHESIS_RE = re.compile(r"(?im)^.*\b(hypothesis|гіпотез[аи]|гіпотеза|working hypothesis|research hypothesis)\b.*$")
DECISION_RE = re.compile(r"(?im)^.*\b(decision|вирішено|рішення|core rule|rules of work|заборонене|правильна дія)\b.*$")


@dataclass
class SourceDoc:
    path: Path
    rel_path: str
    title: str
    text: str


def read_sources(root: Path) -> list[SourceDoc]:
    source_dir = root / VAULT_DIRS["sources"]
    docs: list[SourceDoc] = []
    for path in sorted(source_dir.rglob("*.md")):
        if path.name.lower() == "readme.md":
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        title = extract_title(text) or path.stem
        docs.append(SourceDoc(path=path, rel_path=str(path.relative_to(root)).replace("\\", "/"), title=title, text=text))
    return docs


def extract_title(text: str) -> str | None:
    match = re.search(r"^#\s+(.+?)\s*$", text, flags=re.MULTILINE)
    return match.group(1).strip() if match else None


def sanitize_filename(name: str) -> str:
    name = re.sub(r"[\\/:*?\"<>|]", " ", name)
    name = re.sub(r"\s+", " ", name).strip()
    return name[:120] or "Untitled"


def write_if_changed(path: Path, content: str) -> bool:
    path.parent.mkdir(parents=True, exist_ok=True)
    content = content.rstrip() + "\n"
    if path.exists() and path.read_text(encoding="utf-8", errors="replace") == content:
        return False
    path.write_text(content, encoding="utf-8", newline="\n")
    return True


def extract_wikilinks(docs: Iterable[SourceDoc]) -> Counter[str]:
    counter: Counter[str] = Counter()
    for doc in docs:
        for link in WIKILINK_RE.findall(doc.text):
            counter[link.strip()] += 1
    return counter


def extract_modules(docs: Iterable[SourceDoc]) -> dict[str, list[str]]:
    found: dict[str, list[str]] = defaultdict(list)
    for doc in docs:
        for module in MODULE_RE.findall(doc.text):
            if doc.rel_path not in found[module]:
                found[module].append(doc.rel_path)
    return dict(sorted(found.items()))


def extract_lines(pattern: re.Pattern[str], docs: Iterable[SourceDoc], max_per_doc: int = 12) -> list[tuple[str, str]]:
    out: list[tuple[str, str]] = []
    for doc in docs:
        count = 0
        for match in pattern.finditer(doc.text):
            line = match.group(0).strip(" -\t")
            if line and len(line) < 240:
                out.append((doc.rel_path, line))
                count += 1
            if count >= max_per_doc:
                break
    return out


def generate_import_index(docs: list[SourceDoc], links: Counter[str], modules: dict[str, list[str]]) -> str:
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    lines = [
        "# Knowledge Pipeline Output",
        "",
        f"Generated: {now}",
        "",
        "## Source files scanned",
        "",
    ]
    for doc in docs:
        lines.append(f"- [[{doc.title}]] — `{doc.rel_path}`")
    lines += ["", "## Most used wiki links", ""]
    for link, count in links.most_common(50):
        lines.append(f"- [[{link}]] — {count}")
    lines += ["", "## Detected module IDs", ""]
    for module, paths in modules.items():
        lines.append(f"- [[{module}]] — {len(paths)} source(s)")
    return "\n".join(lines)


def generate_glossary(links: Counter[str]) -> str:
    lines = [
        "# AUTO_GLOSSARY",
        "",
        "Generated glossary from source notes and known trading terms.",
        "",
    ]
    used = set()
    for term, definition in sorted(KNOWN_TERMS.items()):
        lines.append(f"## {term}")
        lines.append("")
        lines.append(definition)
        lines.append("")
        used.add(term)
    extra = [term for term in links if term not in used]
    if extra:
        lines += ["## Unclassified linked terms", ""]
        for term in sorted(extra):
            lines.append(f"- [[{term}]]")
    return "\n".join(lines)


def generate_modules(modules: dict[str, list[str]]) -> str:
    lines = ["# AUTO_MODULE_REGISTRY", "", "Detected module identifiers from source notes.", ""]
    for module, paths in modules.items():
        lines.append(f"## {module}")
        lines.append("")
        lines.append("Sources:")
        for path in paths:
            lines.append(f"- `{path}`")
        lines.append("")
        if module.startswith("OF_"):
            lines.append("Direction: [[Order Flow]]")
        elif module.startswith("ARB_"):
            lines.append("Direction: [[Cross Exchange Arbitrage]]")
        elif module.startswith("SCALP_"):
            lines.append("Direction: [[Scalping]]")
        elif module.startswith("MICRO_"):
            lines.append("Direction: [[Market Microstructure]]")
        lines.append("")
    return "\n".join(lines)


def generate_hypotheses(rows: list[tuple[str, str]]) -> str:
    lines = ["# AUTO_HYPOTHESES", "", "Candidate hypotheses extracted from source notes.", ""]
    for path, line in rows:
        lines.append(f"- `{path}` — {line}")
    return "\n".join(lines)


def generate_decisions(rows: list[tuple[str, str]]) -> str:
    lines = ["# AUTO_DECISION_CANDIDATES", "", "Candidate decisions and rules extracted from source notes.", ""]
    for path, line in rows:
        lines.append(f"- `{path}` — {line}")
    return "\n".join(lines)


def generate_concept_stubs(root: Path, links: Counter[str]) -> list[Path]:
    created: list[Path] = []
    concept_dir = root / VAULT_DIRS["concepts"]
    for term in sorted(KNOWN_TERMS):
        path = concept_dir / f"{sanitize_filename(term)}.md"
        if path.exists():
            continue
        content = f"# {term}\n\n{KNOWN_TERMS[term]}\n\n## Sources\n\n- [[AUTO_GLOSSARY]]\n\n## Status\n\nGenerated stub. Needs manual/AI refinement.\n"
        if write_if_changed(path, content):
            created.append(path)
    return created


def run(root: Path, create_stubs: bool) -> list[Path]:
    docs = read_sources(root)
    links = extract_wikilinks(docs)
    modules = extract_modules(docs)
    hypotheses = extract_lines(HYPOTHESIS_RE, docs)
    decisions = extract_lines(DECISION_RE, docs)

    changed: list[Path] = []
    outputs = {
        root / VAULT_DIRS["index"] / "KNOWLEDGE_PIPELINE_OUTPUT.md": generate_import_index(docs, links, modules),
        root / VAULT_DIRS["glossary"] / "AUTO_GLOSSARY.md": generate_glossary(links),
        root / VAULT_DIRS["modules"] / "AUTO_MODULE_REGISTRY.md": generate_modules(modules),
        root / VAULT_DIRS["hypotheses"] / "AUTO_HYPOTHESES.md": generate_hypotheses(hypotheses),
        root / VAULT_DIRS["decisions"] / "AUTO_DECISION_CANDIDATES.md": generate_decisions(decisions),
    }
    for path, content in outputs.items():
        if write_if_changed(path, content):
            changed.append(path)

    if create_stubs:
        changed.extend(generate_concept_stubs(root, links))

    return changed


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".", help="Vault root path")
    parser.add_argument("--create-stubs", action="store_true", help="Create concept stubs for known terms")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    changed = run(root, create_stubs=args.create_stubs)
    print(f"Changed files: {len(changed)}")
    for path in changed:
        print(path.relative_to(root))


if __name__ == "__main__":
    main()
