import requests
import pandas as pd
import os
 
def fetch_binance_data(symbol="BTCUSDT", interval="1d", limit=1000):
    """
    Fetches historical kline (candlestick) data from Binance API.
    """
    print(f"Fetching {limit} rows of {interval} data for {symbol}...")
   
    url = "https://api.binance.com/api/v3/klines"
    params = {
        "symbol": symbol,
        "interval": interval,
        "limit": limit
    }
   
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
       
        # Define columns based on Binance API documentation
        cols = [
            "open_time", "open", "high", "low", "close", "volume",
            "close_time", "quote_asset_volume", "num_trades",
            "taker_base_volume", "taker_quote_volume", "ignore"
        ]
       
        df = pd.DataFrame(data, columns=cols)
       
        # Create directory if it doesn't exist
        os.makedirs("data/raw", exist_ok=True)
       
        # Save to CSV
        output_path = f"crypto_classifier/data/raw/raw_data.csv"
        df.to_csv(output_path, index=False)
        print(f"Data saved to {output_path}")
        return df
       
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None
 
if __name__ == "__main__":
    fetch_binance_data(symbol="BTCUSDT", interval="1d", limit=1000)