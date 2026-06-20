# Trading Bot v1 Research Notes 2026-06-19

Imported from `trading-bot-v1/docs/research_notes_2026_06_19.md`.

## Main shift

Old hypothesis:

> Find a profitable pattern.

Current hypothesis:

> Find a measurable market property that creates a stable inefficiency, pass execution validation, and only then evaluate edge.

## Research principle

Do not search for beautiful charts, candle patterns, or secret indicators.

Search for:

```text
Market property
↓
Metric
↓
Statistical validation
↓
Execution validation
↓
Edge
```

## Key terms

### Pattern

Statistical repeatability. Not proof of profitability.

### Edge

Positive expectancy after fees, spread, slippage, and execution losses.

### Inefficiency

A mechanism with an understandable payer.

Questions:

- who pays?
- why do they pay?
- why does it repeat?
- why has it not disappeared?

### Execution

Validation that the expected price and size can actually be obtained.

### Persistence

How long the opportunity survives.

## Arbitrage directions

### Stale Quote Discovery

One exchange has already moved, another still shows an old price. HTX pairs such as LINK/HTX and partly ZEC/HTX were noted as candidates.

### Exchange Specific Premium

Some coins may be systematically more expensive or cheaper on a specific exchange. Interesting exchanges: HTX, MEXC, Gate, Bitget.

### Transfer Constraint Premium

Price difference may reflect closed deposits, closed withdrawals, network issues, or local coin shortage rather than free arbitrage.

### Inventory Arbitrage

Professional arbitrageurs often keep assets on both exchanges and trade locally instead of transferring after every trade.

### Arbitrage Feasibility Score

Future composite score:

- net spread
- depth
- persistence
- execution survival
- transfer status
- inventory availability
- exchange reliability

## Microstructure signals

- [[Order Book Imbalance]]
- [[Order Flow Imbalance]]
- [[Refill]]
- [[Quote Walking]]
- [[Queue Stability]]
- [[Liquidity Removal Event]]
- [[Spoofing]]
- [[VPIN]] / Toxicity

## Range Bot / Yorsh hypothesis

Range Bot is a working label for an algorithm that operates inside a narrow price corridor and repeats up/down movement.

Possible signals:

- narrow range
- sawtooth movement
- repeated or similar trade sizes
- recurring buy/sell zones
- repeated tape rhythm
- returning or moving order book quotes
- volume decay before shutdown

Required data:

- [[Order Book]]
- [[Tape]]
- aggregated volume clusters
- spread
- price range
- cycle repetition frequency

## Current priorities

Priority A:

1. Wide Arbitrage Discovery
2. Exchange Premium Discovery
3. Order Book Discovery
4. Range Bot Discovery

Priority B:

1. Refill Discovery
2. Spoofing Discovery
3. Order Flow Discovery
4. Tape / Prints Discovery

Priority C:

1. Inventory Simulator
2. Transfer Constraint Scanner
3. CEX-DEX Discovery

## Important conclusion

The most promising current directions are not classical chart patterns.

Most promising:

- structural exchange features
- order book microstructure
- market maker behavior
- cross-exchange delays
- liquidity imbalances
- range-bot-like algorithms
