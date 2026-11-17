"""Task 1 - find an order by ID with linear search and binary search, and benchmark both."""
import random
import sys
import time
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "data"))
from orders_loader import load_orders


def linear_search(orders, order_id):
    for i, order in enumerate(orders):
        if order["orderId"] == order_id:
            return i
    return -1


def binary_search(orders, order_id):
    low, high = 0, len(orders) - 1
    while low <= high:
        mid = (low + high) // 2
        if orders[mid]["orderId"] == order_id:
            return mid
        if orders[mid]["orderId"] < order_id:
            low = mid + 1
        else:
            high = mid - 1
    return -1


orders = load_orders()
orders.sort(key=lambda o: o["orderId"])          # binary search needs sorted data
print(f"Loaded {len(orders):,} orders")

target = "ORD031415"
i = linear_search(orders, target)
print(f"\nLinear search for {target}: index {i} -> {orders[i]}")
i = binary_search(orders, target)
print(f"Binary search for {target}: index {i} -> {orders[i]}")
print(f"Search for ORD999999 (missing): linear={linear_search(orders, 'ORD999999')}, "
      f"binary={binary_search(orders, 'ORD999999')}")

random.seed(1)
lookups = [f"ORD{random.randint(1, 50_000):06d}" for _ in range(1000)]

start = time.perf_counter()
for oid in lookups:
    linear_search(orders, oid)
linear_time = time.perf_counter() - start

start = time.perf_counter()
for oid in lookups:
    binary_search(orders, oid)
binary_time = time.perf_counter() - start

print("\nBenchmark: 1,000 look-ups on 50,000 orders")
print(f"  Linear search : {linear_time:8.4f} s  ({linear_time / 1000 * 1e6:9.1f} microseconds per look-up)")
print(f"  Binary search : {binary_time:8.4f} s  ({binary_time / 1000 * 1e6:9.1f} microseconds per look-up)")
print(f"  Binary search was about {linear_time / binary_time:,.0f} times faster")

print("\nWhy:")
print("  Linear search checks orders one by one -> O(n), about 25,000 checks on average.")
print("  Binary search halves the range each step -> O(log n), at most 16 checks for 50,000 orders.")
print("  Binary search needs the list sorted by orderId first (one-time O(n log n)).")
