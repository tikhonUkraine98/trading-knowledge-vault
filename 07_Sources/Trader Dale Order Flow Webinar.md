# Trader Dale Order Flow Webinar

Imported from `trading-bot-v1/docs/research_notes/2026-06-20_trader_dale_orderflow_webinar_v1.md`.

## Executive summary

The webinar reinforced the central hypothesis:

```text
Order Book = intentions
Tape = actions
```

Executed trades contain more actionable information than resting orders in the order book.

## Core concepts

### Volume Clusters

Large concentrations of executed volume.

Possible meanings:

- institutional participation
- support zone
- resistance zone
- fair value area

### Delta

Delta = Buy Volume - Sell Volume.

Used for momentum, reversal, and pressure measurement.

### Cumulative Delta

Accumulated Delta over time.

Used for divergence detection, trend confirmation, and hidden accumulation/distribution research.

### Imbalance

Significant asymmetry between aggressive buying and aggressive selling.

Stacked Imbalance = multiple imbalances in sequence.

### Big Orders

Large executed trades. Potential direct footprint of larger participants.

Suggested thresholds:

- 10k USD
- 50k USD
- 100k USD
- 500k USD

### Absorption

Large aggressive volume appears, but price does not continue moving.

Interpretation: opposing liquidity absorbs the aggression.

### Failed Auction

Auction process fails to fully complete. Markets may revisit such areas later.

Future module: [[OF_008_FAILED_AUCTION_DETECTOR]].

### Delta Divergence

Price and Delta/CVD move in opposite directions.

Possible early warning of exhaustion or reversal.

## Project impact

The project separates into two branches:

### Arbitrage Research

- cross-exchange spreads
- execution costs
- transfer risk
- inventory risk
- mispricing detection

Primary object: spread.

### Order Flow Research

- tape
- delta
- CVD
- imbalance
- absorption
- volume clusters

Primary object: liquidity interaction.

## Priority sequence

1. Collect tape data.
2. Collect order book data.
3. Detect large trades.
4. Detect imbalances.
5. Detect absorption.
6. Compare signals against subsequent price movement.
