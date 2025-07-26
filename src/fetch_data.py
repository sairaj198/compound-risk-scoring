import random
import time

def fetch_wallet_transactions(wallet):
    actions = ['deposit', 'borrow', 'repay', 'liquidationCall']
    txs = []
    for _ in range(random.randint(5, 15)):
        txs.append({
            'wallet': wallet,
            'action': random.choice(actions),
            'amount': random.uniform(10, 1000),
            'timestamp': int(time.time()) - random.randint(0, 31536000)
        })
    return txs