# Binance Futures Trading Bot

## Overview

A Python-based trading bot for Binance Futures Testnet that supports MARKET and LIMIT orders with BUY/SELL operations.

## Features

- Place MARKET orders
- Place LIMIT orders
- BUY and SELL support
- Command Line Interface
- Input validation
- Logging
- Exception handling
- Binance Futures Testnet/Demo Trading API integration

## Project Structure

```
trading_bot/

bot/
    __init__.py
    client.py
    orders.py
    validators.py
    logging_config.py
    cli.py

logs/

main.py
README.md
requirements.txt
.env
```

## Installation

```bash
pip install -r requirements.txt
```

## Setup

Create a `.env` file:

```env
API_KEY=your_api_key
API_SECRET=your_api_secret
```

## Run MARKET Order

```bash
python main.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

## Run LIMIT Order

```bash
python main.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 100000
```

## Assumptions

- Binance Futures Testnet/Demo Trading API is used.
- Orders are executed using USDT-M futures.