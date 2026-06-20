# Scalper Language Dictionary

## Purpose

Translate trader slang into observable market mechanics and future algorithmic signals.

| Slang | What trader sees | Possible algorithmic interpretation |
|---|---|---|
| Б'ють | Aggressive buying or selling | Market Order Flow |
| Ллють | Aggressive selling into bids | Sell Pressure |
| Давлять | Persistent pressure on level | Liquidity Pressure / Moving Size |
| Їдять щільність | Liquidity gradually consumed | Liquidity Consumption |
| Розбирають | Rapid liquidity removal by execution | Fast Consumption Event |
| Тримають рівень | Liquidity repeatedly appears | Refill / Iceberg / Defensive Liquidity |
| Захищають рівень | Active defense of price level | Defensive Liquidity |
| Відпустили рівень | Liquidity disappeared | Liquidity Removal Event |
| Щільність | Large concentration of orders | [[Liquidity Wall]] |
| Сайз | Large limit order | Large Liquidity Node |
| Принти | Executed trades tape | [[Tape]] |
| Поглинання | Aggressive flow with little price movement | [[Absorption]] |
| Абсорбція | Large participant absorbs flow | [[Absorption]] Detection |
| Піджимають | Liquidity compresses toward level | Compression Signal |
| Винос | Sudden liquidity sweep | Liquidity Sweep |
| Стопи | Expected stop concentration | Stop Cluster Hypothesis |
| Айсберг | Hidden large order | [[Iceberg Order]] Detection |
| Фейковий сайз | Visible liquidity later removed | Spoofing |
| Коррелятор | Cross-asset reaction bot | Correlation Bot |
| Фронтран | Entry before large visible liquidity | Front Running |
| Йорж / Єрш | Sawtooth movement inside range | [[Range Bot]] |

## Core observation

Most scalper slang does not describe charts.

It describes one of four market processes:

1. liquidity
2. aggression
3. absorption
4. liquidity removal

## Translation layer

Trader Language

→ Market Mechanic

→ Quantitative Metric

→ Detection Algorithm

→ Trading Signal

## Related source

- [[Scalper Language Dictionary v1]]
