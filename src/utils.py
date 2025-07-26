# src/utils.py
import pandas as pd

def load_wallets(file_path):
    df = pd.read_excel(file_path)  # Use read_excel instead of read_csv
    return df['wallet_id'].tolist()  # Make sure the column is named 'wallet_id'
