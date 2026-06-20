# Scalper Language Dictionary v1

Imported from `trading-bot-v1/docs/scalper_language_dictionary_v1.md`.

## Purpose

Translate trader slang into observable market mechanics and future algorithmic signals.

## Dictionary

| Slang | Trader sees | Algorithmic interpretation |
|---|---|---|
| Б'ють | Aggressive buying/selling | [[Market Order Flow]] |
| Ллють | Aggressive selling into bids | [[Sell Pressure]] |
| Давлять | Persistent pressure on level | [[Liquidity Pressure]] / [[Moving Size]] |
| Їдять щільність | Liquidity gradually consumed | [[Liquidity Consumption]] |
| Розбирають | Rapid liquidity removal by execution | [[Fast Consumption Event]] |
| Тримають рівень | Liquidity repeatedly appears | [[Refill]] / [[Iceberg Order]] / [[Defensive Liquidity]] |
| Захищають рівень | Active defense of price level | [[Defensive Liquidity]] |
| Відпустили рівень | Liquidity disappeared | [[Liquidity Removal Event]] |
| Щільність | Large concentration of orders | [[Liquidity Wall]] |
| Сайз | Large limit order | [[Large Liquidity Node]] |
| Принти | Executed trades tape | [[Tape]] |
| Поглинання | Aggressive flow with little price movement | [[Absorption]] |
| Абсорбція | Large participant absorbs flow | [[Absorption]] |
| Піджимають | Liquidity compresses toward level | [[Compression Signal]] |
| Винос | Sudden liquidity sweep | [[Liquidity Sweep]] |
| Стопи | Expected stop concentration | [[Stop Cluster Hypothesis]] |
| Айсберг | Hidden large order | [[Iceberg Order]] |
| Фейковий сайз | Visible liquidity later removed | [[Spoofing]] |
| Коррелятор | Cross-asset reaction bot | [[Correlation Bot]] |
| Фронтран | Entry before large visible liquidity | [[Front Running]] |
| Йорж / Ёрш | Sawtooth movement inside range | [[Range Bot Discovery]] |

## Core Observation

Most scalper slang does not describe charts.

It describes one of four market processes:

1. [[Liquidity]]
2. Aggression
3. [[Absorption]]
4. [[Liquidity Removal Event]]

## Research questions for every slang term

1. What exactly does the trader observe?
2. Which market data is required?
3. Can software detect it?
4. Can it generate edge?

## Long-term goal

```text
Trader Language
↓
Market Mechanic
↓
Quantitative Metric
↓
Detection Algorithm
↓
Trading Signal
```
