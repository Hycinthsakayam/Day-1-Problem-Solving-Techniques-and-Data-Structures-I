"""Task 1 - binary search on 100,000 sorted transaction IDs: comparisons in best, average and worst case vs linear search."""
import math
import random


def binary_search(ids, target):
    comparisons = 0
    low, high = 0, len(ids) - 1
    while low <= high:
        mid = (low + high) // 2
        comparisons += 1
        if ids[mid] == target:
            return mid, comparisons
        if ids[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1, comparisons


def linear_search(ids, target):
    for i, value in enumerate(ids):
        if value == target:
            return i, i + 1
    return -1, len(ids)


N = 100_000
ids = [f"TXN{n:07d}" for n in range(1_000_000, 1_000_000 + N)]   # already sorted
print(f"{N:,} sorted transaction IDs: {ids[0]} ... {ids[-1]}\n")

middle = ids[(N - 1) // 2]
_, best = binary_search(ids, middle)
worst = max(binary_search(ids, t)[1] for t in [ids[0], ids[-1], ids[1], ids[-2], "TXN0000000", "TXN9999999"])
total = sum(binary_search(ids, t)[1] for t in ids)
avg = total / N

_, lin_best = linear_search(ids, ids[0])
_, lin_worst = linear_search(ids, "TXN9999999")
random.seed(3)
lin_avg = sum(linear_search(ids, random.choice(ids))[1] for _ in range(300)) / 300

print(f"{'Case':<10}{'Binary search':>16}{'Linear search':>16}")
print(f"{'Best':<10}{best:>16}{lin_best:>16,}   (binary: middle element / linear: first element)")
print(f"{'Average':<10}{avg:>16.2f}{lin_avg:>16,.0f}   (binary: all 100,000 IDs / linear: 300 random IDs)")
print(f"{'Worst':<10}{worst:>16}{lin_worst:>16,}   (missing ID)")
print(f"\nlog2({N:,}) = {math.log2(N):.2f}, so binary search never needs more than {math.floor(math.log2(N)) + 1} comparisons.")
print("Linear search needs n/2 comparisons on average and n in the worst case.")
