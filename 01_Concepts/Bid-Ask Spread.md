# Bid-Ask Spread

## Ukrainian
Спред між найкращим bid і найкращим ask.

## Simple meaning
Різниця між найкращою ціною купівлі і найкращою ціною продажу в [[Order Book]].

## Formula

Best Ask - Best Bid

## Two roles

1. Liquidity indicator.
2. Hidden [[Execution Cost]].

## Interpretation

Small spread means higher liquidity.

Large spread means lower liquidity or weaker price discovery.

## Arbitrage implication

Cross-exchange spread is not enough. Real profit must subtract:

- bid-ask spread on both exchanges
- exchange fees
- slippage
- transfer cost
- execution losses

## Related modules

- [[ARB_019_EXECUTION_COST_ESTIMATOR]]
- [[ARB_020_SPREAD_EXPANSION_MONITOR]]
- [[MICRO_001_LIQUIDITY_SCORE]]

## Related sources

- [[Bid Ask Spread Execution Cost Research]]
