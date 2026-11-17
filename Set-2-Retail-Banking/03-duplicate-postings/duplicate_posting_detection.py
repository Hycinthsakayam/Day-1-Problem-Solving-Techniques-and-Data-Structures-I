"""Task 3 - find duplicate postings: same account, amount and merchant within 60 seconds."""
import sys
import time
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "data"))
from transactions import day_transactions

txns = day_transactions()                  # already ordered by posting time
print(f"Transactions in the day's file: {len(txns):,}")

start = time.perf_counter()
last_seen = {}                             # (account, amount, merchant) -> last transaction
duplicates = []
for t in txns:
    key = (t["account"], t["amount"], t["merchant"])
    prev = last_seen.get(key)
    if prev and (t["postedAt"] - prev["postedAt"]).total_seconds() <= 60:
        duplicates.append((prev, t))
    last_seen[key] = t
elapsed = time.perf_counter() - start

print(f"Duplicate postings found: {len(duplicates)}  (checked in {elapsed * 1000:.2f} ms)\n")
print(f"{'First':<11}{'Second':<11}{'Account':<9}{'Merchant':<18}{'Amount':>11}  Gap")
for a, b in duplicates:
    gap = int((b["postedAt"] - a["postedAt"]).total_seconds())
    print(f"{a['txnId']:<11}{b['txnId']:<11}{a['account']:<9}{a['merchant']:<18}{a['amount']:>11,.2f}  {gap}s")

print("\nWhy a dictionary (hash map):")
print("  the key (account, amount, merchant) finds the previous matching posting in O(1),")
print("  and the file is already in time order, so one pass is enough -> O(n) time, O(n) space.")
print("  Comparing every pair would be O(n^2).")
