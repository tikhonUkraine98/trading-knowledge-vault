# ARB_019_EXECUTION_COST_ESTIMATOR

## Purpose

Estimate real arbitrage profitability after execution-related losses.

## Core formula concept

Real profit equals cross-exchange spread minus:

- execution cost on exchange A
- execution cost on exchange B
- fees
- slippage
- transfer cost

## Inputs

- cross-exchange spread
- [[Bid-Ask Spread]]
- order book depth
- fees
- expected slippage
- transfer cost

## Outputs

- estimated net profit
- executable spread flag
- risk-adjusted opportunity score

## Related concepts

- [[Cross Exchange Arbitrage]]
- [[Execution Cost]]
- [[Liquidity]]
- [[Bid-Ask Spread]]

## Status

Backlog.
