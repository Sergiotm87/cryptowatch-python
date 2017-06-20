import cryptowatch.Client as cl
import matplotlib.pyplot as plt
import numpy as np

### create a client which targets Coinbase's ETH-USD market
client = cl.MarketClient("kraken", "btceur")

### create a time plot of recent ETH-USD trades
trades = client.GetTrades()
plt.figure()
plt.plot(*zip(*[(x.timestamp, x.price) for x in trades]))
plt.show()