import pandas as pd
import os
 
def processed_data():
    base_dir = "crypto_classifier"
    raw_path = os.path.join(base_dir, "data", "raw", "raw_data.csv")
    processed_dir = os.path.join(base_dir, "data", "processed")
    output_path = os.path.join(processed_dir, "processed_data.csv")
 
    if not os.path.exists(raw_path):
        print(f"Error: {raw_path} not found.")
        return
 
    # 1. Load Data
    df = pd.read_csv(raw_path)
   
    # Clean column names (handles ' open_time' vs 'open_time')
    df.columns = df.columns.str.strip().str.lower()
 
    # 2. Convert to Datetime (IN MEMORY)
    print("Converting timestamps...")
    if 'open_time' in df.columns:
        df['open_time'] = pd.to_datetime(df['open_time'], unit='ms')
   
    if 'close_time' in df.columns:
        df['close_time'] = pd.to_datetime(df['close_time'], unit='ms')
 
    # 3. Filter Columns (Drop 'ignore', 'taker_buy...', etc)
    # If you still see 12 columns in your output, this step was skipping!
    #keep_cols = ['open_time', 'open', 'high', 'low', 'close', 'volume', 'close_time']
    #df = df[keep_cols]
 
    # 4. PROOF: Check types IN MEMORY
    print("\n---------- CHECKING IN-MEMORY TYPES ----------")
    print(df.info())
    print("----------------------------------------------\n")
    # ^^^ Look at the output HERE. It will say datetime64[ns]
 
    # 5. Save to CSV
    # WARNING: This saves dates as TEXT strings (e.g., "2023-01-01")
    os.makedirs(processed_dir, exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Saved to: {output_path}")
 
if __name__ == "__main__":
    processed_data()