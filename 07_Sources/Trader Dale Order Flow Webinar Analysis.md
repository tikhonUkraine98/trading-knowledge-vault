# Trader Dale Order Flow Webinar Analysis

Original source: trading-bot-v1 research notes.

## Executive summary

The webinar reinforces the central hypothesis:

Executed trades contain more actionable information than resting orders.

[[Order Book]] = intentions.

[[Tape]] = actions.

## Core concepts

- Volume Clusters
- [[Delta]]
- [[CVD]]
- [[Imbalance]]
- Big Orders
- [[Absorption]]
- Failed Auction
- Delta Divergence

## Project impact

The project separates into two branches:

### Arbitrage Research

- cross-exchange spreads
- execution costs
- transfer risk
- inventory risk
- mispricing detection

### Order Flow Research

- [[Tape]]
- [[Delta]]
- [[CVD]]
- [[Imbalance]]
- [[Absorption]]
- Volume Clusters

## Current validation priority

1. collect tape data
2. collect order book data
3. detect large trades
4. detect imbalances
5. detect absorption
6. compare signals against later price movement

## Extracted module

- [[OF_008_FAILED_AUCTION_DETECTOR]]
