# Cryptocurrency Arbitrage Bot

This Python-based arbitrage bot identifies potential arbitrage opportunities between Binance and CoinDCX by comparing real-time cryptocurrency prices for common trading pairs across both exchanges.

## Features

- Fetches real-time prices for all trading pairs available on **Binance** and **CoinDCX**.
- Identifies common trading pairs between the two exchanges.
- Detects arbitrage opportunities by comparing price differences and accounting for exchange fees.
- Logs arbitrage opportunities when price differences exceed a specified threshold.

## Requirements

- Python 3.x
- Libraries:
  - `requests`
  - `pandas`
  - `numpy`

## Installation

1. Clone the repository:
   git clone https://github.com/yourusername/arbitrage-bot.git
   cd arbitrage-bot
