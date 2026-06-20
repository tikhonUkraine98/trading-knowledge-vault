# Order Flow Footprint Delta Absorption

Imported from `trading-bot-v1/docs/research_notes/2026-06-20_orderflow_footprint_delta_absorption_v1.md`.

## Strategic importance

This moved the project from price analysis to market microstructure analysis.

```text
Candle = outcome
Order Flow = battle behind the outcome
```

## Core modules

### OF_001_DELTA_TRACKER

Delta = Buy Volume - Sell Volume.

Questions:

- Does delta lead price?
- Does delta lag price?
- Can delta predict reversals?

### OF_002_IMBALANCE_DETECTOR

Imbalance exists when one side dominates the opposite side by about 3x volume.

Observed rule:

```text
Buyer Volume / Seller Volume >= 3
or
Seller Volume / Buyer Volume >= 3
```

### OF_003_ABSORPTION_DETECTOR

Large aggressive volume appears, but price does not move accordingly.

Interpretation: opposing liquidity absorbs aggression.

Hypothesis: absorption may precede reversals.

### OF_004_CVD_TRACKER

CVD = cumulative volume delta.

Purpose: observe the long-term balance between aggressive buyers and sellers.

### OF_005_DELTA_DIVERGENCE

Price and delta/CVD tell different stories.

Potential signal: early warning of exhaustion or reversal.

### OF_006_FOOTPRINT_ANALYZER

Volume footprint shows executed buy and sell volume at each price level.

### OF_007_VALUE_AREA_TRACKER

Track VAH and VAL and test if value area boundaries behave as support, resistance, or liquidity magnets.

## Core hypothesis

Price alone is insufficient.

Useful research hierarchy:

```text
Liquidity
↓
Order Book
↓
Tape
↓
Footprint
↓
Delta
↓
Absorption
↓
Execution
↓
Price
```

Price is the final result, not the primary signal.
