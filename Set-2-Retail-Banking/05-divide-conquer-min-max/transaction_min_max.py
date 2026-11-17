"""Task 5 - highest and lowest transaction amount with divide and conquer vs a brute-force scan."""
import sys
import time
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "data"))
from transactions import day_transactions

count = 0


def min_max_dc(a, lo, hi):
    """returns (min, max) of a[lo..hi]"""
    global count
    if lo == hi:
        return a[lo], a[lo]
    if hi == lo + 1:
        count += 1
        return (a[lo], a[hi]) if a[lo] < a[hi] else (a[hi], a[lo])
    mid = (lo + hi) // 2
    min1, max1 = min_max_dc(a, lo, mid)
    min2, max2 = min_max_dc(a, mid + 1, hi)
    count += 2
    return min(min1, min2), max(max1, max2)


def min_max_brute(a):
    comparisons = 0
    lo = hi = a[0]
    for x in a[1:]:
        comparisons += 2
        if x < lo:
            lo = x
        if x > hi:
            hi = x
    return lo, hi, comparisons


amounts = [t["amount"] for t in day_transactions()]
n = len(amounts)
print(f"Amounts in the day's file: {n:,}")

start = time.perf_counter()
lo, hi = min_max_dc(amounts, 0, n - 1)
t_dc = time.perf_counter() - start
start = time.perf_counter()
lo2, hi2, brute_count = min_max_brute(amounts)
t_brute = time.perf_counter() - start

print(f"\nDivide and conquer: lowest {lo:,.2f}, highest {hi:,.2f}, comparisons {count:,}, time {t_dc * 1000:.2f} ms")
print(f"Brute-force scan  : lowest {lo2:,.2f}, highest {hi2:,.2f}, comparisons {brute_count:,}, time {t_brute * 1000:.2f} ms")
print(f"\nDivide and conquer needs about 3n/2 - 2 = {3 * n // 2 - 2:,} comparisons, brute force about 2(n-1) = {2 * (n - 1):,}.")
print("Both are O(n). D&C saves comparisons, but recursion overhead makes it slower in Python.")
