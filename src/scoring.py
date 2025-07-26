def calculate_score(row):
    score = 1000
    score -= 200 * row['liquidation_ratio']
    score += 150 * row['repay_borrow_ratio']
    score += 100 * row['deposit_borrow_ratio']
    score -= 50 / row['interaction_frequency'] if row['interaction_frequency'] > 0 else 50
    return max(min(score, 1000), 0)