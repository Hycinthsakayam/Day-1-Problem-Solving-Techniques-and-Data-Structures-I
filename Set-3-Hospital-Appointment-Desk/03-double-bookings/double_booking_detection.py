"""Task 3 - prevent the same patient being booked twice in one slot, using a set."""
import random
import time

random.seed(21)
slots = [f"{h:02d}:{m:02d}" for h in range(8, 17) for m in (0, 15, 30, 45)]
requests = [(f"P{100000 + random.randint(0, 2_999)}", random.choice(slots)) for _ in range(20_000)]
requests += [("P100007", "09:15"), ("P100007", "09:15")]          # a clear double booking

booked = set()                       # (patientId, slot)
rejected = []
start = time.perf_counter()
for pid, slot in requests:
    if (pid, slot) in booked:
        rejected.append((pid, slot))
    else:
        booked.add((pid, slot))
t_set = time.perf_counter() - start

print(f"Booking requests: {len(requests):,}")
print(f"Booked: {len(booked):,}   Rejected as double bookings: {len(rejected)}")
print("First rejected requests:", rejected[:5])
print(f"Time with a set: {t_set * 1000:.2f} ms")

booked_list = []
sample = requests[:5000]
start = time.perf_counter()
for pid, slot in sample:
    if (pid, slot) not in booked_list:     # scans the whole list every time
        booked_list.append((pid, slot))
t_list = time.perf_counter() - start
print(f"Time with a list scan for only 5,000 requests: {t_list * 1000:.2f} ms")

print("\nA set (hash table) checks membership in O(1) on average, so n bookings cost O(n).")
print("A list scan is O(n) per check, so n bookings cost O(n^2): at 20,000 bookings that is ~200 million")
print("comparisons, which is too slow for a live reception desk.")
