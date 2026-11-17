"""Sample data shared by the Set 2 tasks: one day of card transactions (generated with a fixed seed)."""
import random
from datetime import datetime, timedelta

MERCHANTS = ["Amazon", "Swiggy", "BigBasket", "IRCTC", "Zomato", "Reliance Digital", "HP Petrol", "Apollo Pharmacy"]


def day_transactions(n=5000, seed=7, duplicates=12):
    random.seed(seed)
    start = datetime(2026, 11, 16)
    txns = []
    for i in range(n - duplicates):
        txns.append({
            "txnId": f"TXN{100000 + i}",
            "account": f"ACC{random.randint(1, 600):04d}",
            "merchant": random.choice(MERCHANTS),
            "amount": round(random.uniform(50, 75_000), 2),
            "postedAt": start + timedelta(seconds=random.randint(0, 86_399)),
        })
    for k in range(duplicates):                     # same posting again within a minute
        t = dict(random.choice(txns))
        t["txnId"] = f"TXN{100000 + n - duplicates + k}"
        t["postedAt"] = t["postedAt"] + timedelta(seconds=random.randint(5, 55))
        txns.append(t)
    txns.sort(key=lambda t: t["postedAt"])
    return txns
