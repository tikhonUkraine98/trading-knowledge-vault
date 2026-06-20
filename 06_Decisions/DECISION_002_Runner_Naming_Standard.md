# DECISION_002 Runner Naming Standard

Imported from `trading-bot-v1/docs/research_runner_naming_standard_v1.md`.

## Decision

All research workflows, artifacts, and completion issues must be named so the result is understandable without opening logs.

Generic workflow names are no longer acceptable.

## Core format

```text
<DIRECTION>_<TASK>_<SCOPE>_<VERSION>
```

Run suffix:

```text
RUN001
RUN002
RUN003
```

## Direction prefixes

- SCALP — scalping, DOM, tape, order-flow, microstructure signals inside one exchange.
- ARB — cross-exchange arbitrage, spread charts, exchange lag, inventory and rebalance research.
- MICRO — general market microstructure research.
- DISCOVERY — wide search with unclear target.
- VALIDATION — validation of previous findings.
- REPLAY — replay / post-factum execution validation.

## Examples

```text
SCALP_TAPE_CAPTURE_MULTI_V01_RUN001
ARB_HTX_LAG_ZEC_DASH_ZEN_1H_V01_RUN001
MICRO_TAPE_DOM_COMPARE_V01_RUN001
REPLAY_ZEC_HTX_EXECUTION_V01_RUN001
```

## Issue title standard

```text
[<DIRECTION>][<TASK>][<RUN_ID>] Completed
```

## Artifact naming standard

```text
research_outputs_<DIRECTION>_<TASK>_<SCOPE>_<RUN_ID>
```

## Practical rule

Before creating a new workflow, choose direction, task, scope, version, and run id. Use the same identifiers everywhere.

## Project memory rule

The assistant should minimize the user's manual work. If a step can be automated, automate it by default.
