import pandas as pd
from collections import defaultdict

def generate_wallet_features(wallets):
    from .fetch_data import fetch_wallet_transactions

    all_features = []
    for wallet in wallets:
        txs = fetch_wallet_transactions(wallet)
        if not txs:
            continue

        df = pd.DataFrame(txs)
        df['amount'] = pd.to_numeric(df['amount'], errors='coerce')
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s', errors='coerce')

        deposits = df[df['action'] == 'deposit']
        borrows = df[df['action'] == 'borrow']
        repays = df[df['action'] == 'repay']
        liquidations = df[df['action'] == 'liquidationCall']

        total_deposit = deposits['amount'].sum()
        total_borrow = borrows['amount'].sum()
        total_repay = repays['amount'].sum()

        repay_borrow_ratio = total_repay / total_borrow if total_borrow > 0 else 0
        liquidation_ratio = len(liquidations) / len(borrows) if len(borrows) > 0 else 0
        deposit_borrow_ratio = total_deposit / total_borrow if total_borrow > 0 else 0

        if pd.isna(df['timestamp'].min()) or pd.isna(df['timestamp'].max()):
            time_active_days = 1
        else:
            time_active_days = (df['timestamp'].max() - df['timestamp'].min()).days + 1

        interaction_frequency = len(df) / time_active_days if time_active_days > 0 else 0

        all_features.append({
            'wallet': wallet,
            'repay_borrow_ratio': repay_borrow_ratio,
            'deposit_borrow_ratio': deposit_borrow_ratio,
            'liquidation_ratio': liquidation_ratio,
            'interaction_frequency': interaction_frequency
        })

    return pd.DataFrame(all_features)
