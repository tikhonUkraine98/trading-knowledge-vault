# Trading Bot Research Notes 2026-06-19

Original source: `trading-bot-v1/docs/research_notes_2026_06_19.md`

## Core shift

Previous hypothesis:

Find a profitable pattern.

Current hypothesis:

Find a measurable market property, validate execution, and only then evaluate edge.

## Research method

Market property

→ metric

→ statistical verification

→ execution validation

→ edge

## Main research directions

### Arbitrage

- stale quote discovery
- exchange specific premium
- transfer constraint premium
- [[Inventory Arbitrage]]
- arbitrage feasibility score

### Market microstructure

- [[Order Book]]
- [[Tape]]
- [[Liquidity]]
- [[Order Book Imbalance]]
- Order Flow Imbalance
- [[Refill]]
- Quote Walking
- Queue Stability
- Liquidity Removal Event

### Range Bot

- [[Range Bot]]
- tape repetition
- repeated trade size
- bid/ask refill
- quote walking
- spread capture potential

## Current priorities

Priority A:

1. Wide Arbitrage Discovery
2. Exchange Premium Discovery
3. Order Book Discovery
4. Range Bot Discovery

Priority B:

1. Refill Discovery
2. Order Flow Discovery
3. Tape / Prints Discovery

Priority C:

1. Inventory Simulator
2. Transfer Constraint Scanner
3. CEX-DEX Discovery
