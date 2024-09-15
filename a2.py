#to check arbitrage opuurtuinty coindcx(small indian exchange) and binance 
import requests
import pandas as pd
import numpy as np
import time

BINANCE_PRICE_URL = "https://api.binance.com/api/v3/ticker/price"
COINDCX_TICKER_URL = "https://api.coindcx.com/exchange/ticker"

def get_binance_prices():
    response = requests.get(BINANCE_PRICE_URL)
    data = response.json()
    df_binance = pd.DataFrame(data)
    df_binance.set_index('symbol', inplace=True)
    return df_binance['price'].astype(float)

def get_coindcx_prices():
    response = requests.get(COINDCX_TICKER_URL)
    data = response.json()
    df_coindcx = pd.DataFrame(data)
    df_coindcx.set_index('market', inplace=True)
    return df_coindcx['last_price'].astype(float)

def get_common_symbols(binance_df, coindcx_df):
    common_symbols = set(binance_df.index).intersection(set(coindcx_df.index))
    return common_symbols

def check_arbitrage(binance_price, coindcx_price, threshold=0.5):
    price_diff = coindcx_price - binance_price
    percentage_diff = (price_diff / binance_price) * 100
    trading_fees = 0.2
    if abs(percentage_diff) > trading_fees + threshold:
        return percentage_diff, price_diff
    return None, None

if __name__ == "__main__":
    while True:
        binance_prices = get_binance_prices()
        coindcx_prices = get_coindcx_prices()
        
        common_symbols = get_common_symbols(binance_prices, coindcx_prices)
        
        for symbol in common_symbols:
            binance_price = binance_prices.loc[symbol]
            coindcx_price = coindcx_prices.loc[symbol]
            
            opportunity, price_diff = check_arbitrage(binance_price, coindcx_price)
            if opportunity:
                print(f"Arbitrage Opportunity for {symbol}: Price Difference: {price_diff} USD, Percentage: {opportunity}%")
        time.sleep(5)
    