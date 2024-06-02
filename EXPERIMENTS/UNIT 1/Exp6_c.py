def sum_scores(*scores):
    return sum(scores)

total = sum_scores(88,92,79,93)
print(f'Total score:{total}')

total = sum_scores(88,92)
print(f'Total score:{total}')