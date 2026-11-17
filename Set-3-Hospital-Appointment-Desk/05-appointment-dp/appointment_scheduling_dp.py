"""Task 5 - maximum number of appointments a doctor can attend in a shift (DP), compared with greedy choices."""
from bisect import bisect_right

# (patient, start, end) in minutes from 09:00; slots overlap and have different durations
slots = [
    ("Arun", 0, 60), ("Divya", 10, 30), ("Karthik", 30, 50), ("Meena", 45, 75), ("Rahul", 50, 70),
    ("Sneha", 60, 120), ("Vikram", 70, 90), ("Priya", 85, 100), ("Lakshmi", 95, 140), ("Sanjay", 100, 115),
    ("Nithya", 115, 130), ("Imran", 125, 180), ("Deepa", 130, 145), ("Arjun", 145, 160), ("Fathima", 150, 175),
]

hhmm = lambda m: f"{9 + m // 60:02d}:{m % 60:02d}"


def dp_max_appointments(slots):
    s = sorted(slots, key=lambda x: x[2])                  # by end time
    ends = [x[2] for x in s]
    best = [0] * (len(s) + 1)                              # best[i] = max using first i slots
    take = [False] * (len(s) + 1)
    for i in range(1, len(s) + 1):
        p = bisect_right(ends, s[i - 1][1])                 # slots that end before this one starts
        if best[p] + 1 > best[i - 1]:
            best[i], take[i] = best[p] + 1, True
        else:
            best[i] = best[i - 1]
    chosen, i = [], len(s)
    while i > 0:
        if take[i]:
            chosen.append(s[i - 1])
            i = bisect_right(ends, s[i - 1][1])
        else:
            i -= 1
    return list(reversed(chosen))


def greedy(slots, order_key):
    chosen = []
    for slot in sorted(slots, key=order_key):
        if all(slot[2] <= c[1] or slot[1] >= c[2] for c in chosen):
            chosen.append(slot)
    return sorted(chosen, key=lambda x: x[1])


dp = dp_max_appointments(slots)
print(f"Requested slots: {len(slots)}")
print(f"\nDynamic programming: {len(dp)} appointments")
print("  " + ", ".join(f"{p} {hhmm(a)}-{hhmm(b)}" for p, a, b in dp))

for name, k in [("earliest finish", lambda x: x[2]), ("earliest start", lambda x: x[1]),
                ("shortest duration", lambda x: x[2] - x[1])]:
    g = greedy(slots, k)
    note = "same as DP (optimal)" if len(g) == len(dp) else "fewer than DP"
    print(f"\nGreedy by {name:<17}: {len(g)} appointments - {note}")
    print("  " + ", ".join(f"{p} {hhmm(a)}-{hhmm(b)}" for p, a, b in g))

small = [("A", 0, 30), ("B", 25, 40), ("C", 35, 70)]
print("\nCounter-example for 'shortest duration': A 09:00-09:30, B 09:25-09:40, C 09:35-10:10")
print(f"  greedy by shortest duration: {len(greedy(small, lambda x: x[2] - x[1]))} (takes B, which blocks A and C)")
print(f"  dynamic programming        : {len(dp_max_appointments(small))} (A and C)")

print("\nDP checks every 'take or skip' choice: O(n log n) with binary search on end times.")
print("Greedy by earliest finish is also optimal for counting appointments; other greedy rules can fail.")
