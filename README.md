# 💼 Wallet Risk Scoring – Compound Protocol

This project performs **risk scoring (0–1000)** for a set of DeFi wallet addresses based on their behavior using mock transaction data from Compound V2/V3 protocols. The scoring is inspired by responsible DeFi usage patterns like repayments, deposits, and liquidation avoidance.

---

## 🚀 Objective

- Input: Wallet addresses (from `Wallet id.xlsx`)
- Output: `scores.csv` containing risk scores for each wallet

| wallet            | score |
|-------------------|-------|
| 0xabc...123       | 732   |
| 0xdef...456       | 512   |

---

## 📥 Data Collection Method

- The project **simulates on-chain data** using mock logic in `fetch_data.py`.
- For each wallet, random transactions are generated with fields:
  - `action` (`deposit`, `borrow`, `repay`, `liquidationCall`)
  - `amount`: random float
  - `timestamp`: random time within the last year

> ⚠️ In production, this function should be replaced with live data fetching from Compound’s subgraphs or APIs.

---

## 🧠 Feature Selection Rationale

We engineered the following features for each wallet based on its transaction history:

| Feature                  | Meaning                                                      |
|--------------------------|--------------------------------------------------------------|
| `repay_borrow_ratio`     | Measures responsibility in paying back loans                 |
| `deposit_borrow_ratio`   | Indicates over-collateralization (healthy wallets)           |
| `liquidation_ratio`      | Shows how often the wallet faced liquidation (a risk signal) |
| `interaction_frequency`  | Measures wallet activity over time (trust metric)            |

---

## 📊 Scoring Method

Implemented in `scoring.py`, the formula:

```python
score = 1000
score -= 200 * liquidation_ratio
score += 150 * repay_borrow_ratio
score += 100 * deposit_borrow_ratio
score -= 50 / interaction_frequency if interaction_frequency > 0 else 50
