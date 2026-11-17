"""Task 2 - sort appointments by urgency, then arrival time, with selection sort and quick sort; compare swaps and time."""
import sys
import time
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "data"))
from patients import todays_appointments

key = lambda a: (a["urgency"], a["arrival"], a["token"])


def selection_sort(items):
    a, swaps = list(items), 0
    for i in range(len(a) - 1):
        m = i
        for j in range(i + 1, len(a)):
            if key(a[j]) < key(a[m]):
                m = j
        if m != i:
            a[i], a[m] = a[m], a[i]
            swaps += 1
    return a, swaps


def quick_sort(items):
    a, swaps = list(items), [0]

    def partition(lo, hi):
        pivot = key(a[(lo + hi) // 2])
        i, j = lo, hi
        while i <= j:
            while key(a[i]) < pivot:
                i += 1
            while key(a[j]) > pivot:
                j -= 1
            if i <= j:
                if i != j:
                    a[i], a[j] = a[j], a[i]
                    swaps[0] += 1
                i += 1
                j -= 1
        return i, j

    stack = [(0, len(a) - 1)]
    while stack:
        lo, hi = stack.pop()
        if lo < hi:
            i, j = partition(lo, hi)
            stack += [(lo, j), (i, hi)]
    return a, swaps[0]


appts = todays_appointments()
print(f"Appointments today: {len(appts):,}")

start = time.perf_counter()
s_sorted, s_swaps = selection_sort(appts)
t_sel = time.perf_counter() - start
start = time.perf_counter()
q_sorted, q_swaps = quick_sort(appts)
t_q = time.perf_counter() - start

print(f"\n{'Algorithm':<16}{'Swaps':>8}{'Time (s)':>11}")
print(f"{'Selection sort':<16}{s_swaps:>8,}{t_sel:>11.4f}")
print(f"{'Quick sort':<16}{q_swaps:>8,}{t_q:>11.4f}")
print(f"Same result: {s_sorted == q_sorted}")

print("\nDoctor's list (first 8):")
print(f"  {'Token':>5}  {'Urgency':>7}  Arrival  Patient")
for a in q_sorted[:8]:
    print(f"  {a['token']:>5}  {a['urgency']:>7}  {a['arrival']}    {a['patientId']}")

print("\nSelection sort makes at most n-1 swaps but always does n^2/2 comparisons -> O(n^2).")
print("Quick sort makes more swaps but only about n log n comparisons on average -> much faster.")
