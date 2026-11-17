"""Task 1 - linear and binary search over 20,000 patient records; time for 1,000 look-ups."""
import random
import sys
import time
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "data"))
from patients import patient_records


def linear_search(records, pid):
    for r in records:
        if r["patientId"] == pid:
            return r
    return None


def binary_search(records, pid):
    lo, hi = 0, len(records) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        key = records[mid]["patientId"]
        if key == pid:
            return records[mid]
        if key < pid:
            lo = mid + 1
        else:
            hi = mid - 1
    return None


records = patient_records()
records.sort(key=lambda r: r["patientId"])
print(f"Patient records: {len(records):,}")
print("Example look-up P112345 ->", binary_search(records, "P112345"))

random.seed(99)
queries = [f"P{100000 + random.randint(0, 21_000)}" for _ in range(1000)]   # a few IDs do not exist

start = time.perf_counter()
found_lin = sum(linear_search(records, q) is not None for q in queries)
t_lin = time.perf_counter() - start
start = time.perf_counter()
found_bin = sum(binary_search(records, q) is not None for q in queries)
t_bin = time.perf_counter() - start

print(f"\n1,000 look-ups ({found_lin} found, {1000 - found_lin} not registered)")
print(f"  Linear search: {t_lin:.4f} s")
print(f"  Binary search: {t_bin:.4f} s   (same results: {found_lin == found_bin})")
print(f"  Speed-up: about {t_lin / t_bin:,.0f}x")
print("\nLinear search is O(n): about 10,000 checks per look-up, and 20,000 for a missing patient.")
print("Binary search is O(log n): at most 15 checks, because the records are kept sorted by patient ID.")
