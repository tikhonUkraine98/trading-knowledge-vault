# Trading Bot v1 Microstructure Research Notes

Imported from `trading-bot-v1/docs/microstructure_research_notes_v1.md`.

## Core Principle

```text
Order Book = intentions
Tape = execution
```

Serious analysis should combine both.

## Tape Confirmation Principle

Large liquidity in the book alone is not sufficient. Need confirmation through executed trades.

Strong signal:

```text
Large bid + aggressive buying in tape
```

Weak signal:

```text
Large bid + no executions
```

## Main research objects

- [[Order Book]]
- [[Tape]]
- [[Hidden Liquidity]]
- [[Iceberg Order]]
- [[Liquidity Wall]]
- [[Moving Size]]
- [[Liquidity Pressure]]
- [[Range Bot Discovery]]
- [[Market Replay Engine]]

## Iceberg Detection

Hidden large order where only a small visible quantity is displayed. Repeated executions at the same price may indicate iceberg behavior.

## Liquidity Wall Detection

Large concentration of liquidity on a specific level. Metrics: wall size, wall lifetime, execution frequency, price impact.

## Moving Size Detection

Large order systematically moving with price. Working interpretation: active pressure from a larger participant.

## Tape Quality

Need to distinguish small retail flow from large block trades. Large blocks may indicate institutional participation.

## Range Bot / Yorsh

Working hypothesis: algorithm operating inside a narrow price corridor.

Behavior: lower zone buy, upper zone sell, repeat.

Possible signals: narrow stable range, repetitive trade sizes, recurring buy/sell zones, tape rhythm, refill behavior, volume decay before shutdown.

## Market Replay Engine

Record order book, tape, spreads, and derived metrics. Replay later to study spoofing, refill, iceberg, moving size, liquidity walls, and range bots.

## Future Research Directions

1. Tape Discovery
2. Iceberg Detection
3. Moving Size Detection
4. Liquidity Wall Detection
5. Tape Confirmation Score
6. Market Replay Engine
7. Range Bot Discovery

## Key Observation

The objective is to teach algorithms to recognize repeatable market behaviors.
