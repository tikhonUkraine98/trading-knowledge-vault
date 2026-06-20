# Tools

## knowledge_pipeline.py

Deterministic local script for maintaining the Obsidian vault.

It scans:

```text
07_Sources/*.md
```

and generates:

```text
00_Index/KNOWLEDGE_PIPELINE_OUTPUT.md
08_Glossary/AUTO_GLOSSARY.md
03_Modules/AUTO_MODULE_REGISTRY.md
02_Hypotheses/AUTO_HYPOTHESES.md
06_Decisions/AUTO_DECISION_CANDIDATES.md
```

Optional concept stubs are created in:

```text
01_Concepts/
```

## How to run

From the repository root:

```powershell
python tools/knowledge_pipeline.py --create-stubs
```

or without concept stubs:

```powershell
python tools/knowledge_pipeline.py
```

## Workflow

1. Add raw notes to `07_Sources`.
2. Run the script.
3. Review generated files.
4. Commit and push changes with GitHub Desktop.

## Important

This script does not use OpenAI API or any external service. It only parses local markdown files.

It is intended as a safe first version of the knowledge pipeline. Later it can be extended with an AI extraction layer.
