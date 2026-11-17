"""Task 3 - flag duplicate orders: same customerId and amount within the same minute."""
import sys
import time
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "data"))
from orders_loader import load_orders

orders = load_orders()

start = time.perf_counter()
first_seen = {}        # (customerId, amount, minute) -> first orderId
duplicates = []
for o in orders:
    key = (o["customerId"], o["amount"], o["createdAt"][:16])   # "YYYY-MM-DD HH:MM"
    if key in first_seen:
        duplicates.append((first_seen[key], o["orderId"], key))
    else:
        first_seen[key] = o["orderId"]
elapsed = time.perf_counter() - start

print(f"Checked {len(orders):,} orders in {elapsed * 1000:.1f} ms")
print(f"Duplicate submissions found: {len(duplicates)}\n")
print(f"{'Original':<11} {'Duplicate':<11} {'Customer':<9} {'Amount':>10}  Minute")
for orig, dup, (cust, amt, minute) in duplicates[:10]:
    print(f"{orig:<11} {dup:<11} {cust:<9} {amt:>10,.2f}  {minute}")
if len(duplicates) > 10:
    print(f"... and {len(duplicates) - 10} more")

print("\nComplexity:")
print("  Time : O(n) - one pass, each dictionary look-up/insert is O(1) on average")
print("  Space: O(n) - the dictionary can hold one key per order in the worst case")
print("  A nested-loop comparison would be O(n^2) = about 1.25 billion pairs for 50,000 orders.")
