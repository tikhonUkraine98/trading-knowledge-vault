# Pure vs Statistical Arbitrage Research

Original source: trading-bot-v1 research notes.

## Core insight

Arbitrage is best viewed as mispricing detection.

The goal is to identify temporary pricing inconsistencies between identical or strongly related assets.

## Pure arbitrage

Buy and sell equivalent assets simultaneously.

Characteristics:

- requires simultaneous execution
- opportunities disappear quickly
- speed is part of the strategy
- market participants remove the opportunity through trading

## Statistical arbitrage

Uses historical relationships between assets and trades deviations from expected relationships.

Examples:

- BTC and ETH
- BTC spot and BTC perpetual
- DOGE and SHIB
- exchange token pairs

## Main risks

- execution risk
- transfer risk
- exchange risk
- inventory risk

## Extracted modules

- [[ARB_021_MISPRICING_DETECTOR]]
- [[ARB_022_STATISTICAL_ARBITRAGE_RESEARCH]]
- [[ARB_023_PAIR_RELATIONSHIP_TRACKER]]
- [[ARB_024_CONVERGENCE_MONITOR]]
