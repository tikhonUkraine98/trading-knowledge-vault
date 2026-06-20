# H001 Tape Confirms Order Book

## Statement

Large visible liquidity in [[Order Book]] becomes more meaningful only when confirmed by executed trades in [[Tape]].

## Source idea

Order Book shows intentions.

Tape shows actions.

## Strong signal

Large bid plus aggressive buying in tape.

## Weak signal

Large bid with no executions.

## Required data

- order book snapshots
- executed trades
- price reaction after event

## Test method

Compare future price movement after:

1. visible liquidity only
2. visible liquidity plus tape confirmation

## Related concepts

- [[Order Book]]
- [[Tape]]
- [[Liquidity Wall]]
- [[Absorption]]

## Status

Open.
