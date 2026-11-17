"""Task 2 - rank orders by amount (descending) with insertion sort O(n^2) and merge sort O(n log n)."""
import sys
import time
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "data"))
from orders_loader import load_orders


def insertion_sort_desc(items, key, trace=False):
    a = list(items)
    for i in range(1, len(a)):
        current = a[i]
        j = i - 1
        while j >= 0 and key(a[j]) < key(current):
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = current
        if trace and i <= 3:
            print(f"  pass {i}: {[key(x) for x in a]}")
    return a


def merge_sort_desc(items, key, trace=False, depth=0, counter=None):
    if counter is None:
        counter = [0]
    if len(items) <= 1:
        return list(items)
    mid = len(items) // 2
    left = merge_sort_desc(items[:mid], key, trace, depth + 1, counter)
    right = merge_sort_desc(items[mid:], key, trace, depth + 1, counter)
    merged, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if key(left[i]) >= key(right[j]):
            merged.append(left[i]); i += 1
        else:
            merged.append(right[j]); j += 1
    merged += left[i:] + right[j:]
    counter[0] += 1
    if trace and counter[0] <= 3:
        print(f"  merge {counter[0]}: {[key(x) for x in left]} + {[key(x) for x in right]} -> {[key(x) for x in merged]}")
    return merged


amount = lambda o: o["amount"]
orders = load_orders()

sample = orders[:6]
print("Trace on 6 orders:", [o["amount"] for o in sample])
print("\nInsertion sort (descending), first three passes:")
insertion_sort_desc(sample, amount, trace=True)
print("\nMerge sort (descending), first three merges:")
merge_sort_desc(sample, amount, trace=True)

data = orders[:10_000]
print(f"\nSorting {len(data):,} orders by amount (descending)")

start = time.perf_counter()
r1 = insertion_sort_desc(data, amount)
t1 = time.perf_counter() - start

start = time.perf_counter()
r2 = merge_sort_desc(data, amount)
t2 = time.perf_counter() - start

start = time.perf_counter()
r3 = sorted(data, key=amount, reverse=True)
t3 = time.perf_counter() - start

print(f"  Insertion sort  O(n^2)      : {t1:8.4f} s")
print(f"  Merge sort      O(n log n)  : {t2:8.4f} s")
print(f"  Built-in sorted (Timsort)   : {t3:8.4f} s")
same = [amount(o) for o in r1] == [amount(o) for o in r2] == [amount(o) for o in r3]
print(f"  All three give the same order: {same}")
print("\nTop 5 orders for dispatch:")
for o in r3[:5]:
    print(f"  {o['orderId']}  {o['customerId']}  Rs.{o['amount']:>10,.2f}")
