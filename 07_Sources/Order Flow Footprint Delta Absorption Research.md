# Order Flow Footprint Delta Absorption Research

Original source: `trading-bot-v1/docs/research_notes/2026-06-20_orderflow_footprint_delta_absorption_v1.md`

## Strategic importance

This research moved the project from price analysis toward [[Market Microstructure]] analysis.

Candles show the outcome.

[[Order Flow]] attempts to show the battle behind the outcome.

## Extracted modules

- [[OF_001_DELTA_TRACKER]]
- [[OF_002_IMBALANCE_DETECTOR]]
- [[OF_003_ABSORPTION_DETECTOR]]
- [[OF_004_CVD_TRACKER]]
- [[OF_005_DELTA_DIVERGENCE]]
- [[OF_006_FOOTPRINT_ANALYZER]]
- [[OF_007_VALUE_AREA_TRACKER]]

## Core hierarchy

[[Liquidity]]

→ [[Order Book]]

→ [[Tape]]

→ Footprint

→ [[Delta]]

→ [[Absorption]]

→ Execution

→ Price

## Key conclusion

Price becomes the final result rather than the primary signal.
