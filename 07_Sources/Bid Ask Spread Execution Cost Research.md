# Bid Ask Spread Execution Cost Research

Original source: `trading-bot-v1/docs/research_notes/2026-06-20_bid_ask_spread_execution_cost_v1.md`

## Key observation

Most traders think about arbitrage spread between exchanges.

This source focuses on spread inside one order book:

Best Ask minus Best Bid.

This is [[Bid-Ask Spread]].

## Execution cost insight

[[Bid-Ask Spread]] acts as hidden [[Execution Cost]].

A trader buying at market and immediately selling back loses the spread before exchange fees.

## Arbitrage implication

Real profit must subtract:

- execution cost on exchange A
- execution cost on exchange B
- fees
- transfer cost
- slippage

## Extracted modules

- [[ARB_019_EXECUTION_COST_ESTIMATOR]]
- [[ARB_020_SPREAD_EXPANSION_MONITOR]]
- [[MICRO_001_LIQUIDITY_SCORE]]

## Hypothesis

[[H003 Spread Expansion Predicts Arbitrage]]
