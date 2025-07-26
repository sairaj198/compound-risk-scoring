import pandas as pd
import os
from src.utils import load_wallets
from src.feature_engineering import generate_wallet_features
from src.scoring import calculate_score

def main():
    print("[INFO] Loading wallet list...")
    wallets = load_wallets('data/Wallet id.xlsx')

    print("[INFO] Generating features for each wallet...")
    df = generate_wallet_features(wallets)

    print("[INFO] Calculating risk scores...")
    df['score'] = df.apply(calculate_score, axis=1)

    os.makedirs('output', exist_ok=True)
    df[['wallet', 'score']].to_csv('output/scores.csv', index=False)
    print("[DONE] Risk scoring complete. Saved to output/scores.csv")

if __name__ == '__main__':
    main()
