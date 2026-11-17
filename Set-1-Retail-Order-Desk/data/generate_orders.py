"""Creates orders.csv with 50,000 orders for one day (plus a few duplicate submissions)."""
import csv
import random
from datetime import datetime, timedelta
from pathlib import Path

random.seed(42)
DAY_START = datetime(2026, 11, 16)
N_ORDERS = 50_000
N_DUPLICATES = 25

rows = []
for _ in range(N_ORDERS - N_DUPLICATES):
    created = DAY_START + timedelta(seconds=random.randint(0, 86_399))
    rows.append([f"CUST{random.randint(1, 8000):04d}", round(random.uniform(99, 25_000), 2), created])

# duplicate submissions: same customer and amount, a few seconds later in the same minute
for _ in range(N_DUPLICATES):
    cust, amount, created = random.choice(rows)
    second = min(59, created.second + random.randint(1, 20))
    rows.append([cust, amount, created.replace(second=second)])

rows.sort(key=lambda r: r[2])
out = Path(__file__).with_name("orders.csv")
with out.open("w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["orderId", "customerId", "amount", "createdAt"])
    for i, (cust, amount, created) in enumerate(rows, 1):
        w.writerow([f"ORD{i:06d}", cust, f"{amount:.2f}", created.strftime("%Y-%m-%d %H:%M:%S")])
print(f"wrote {len(rows)} orders to {out.name}")
