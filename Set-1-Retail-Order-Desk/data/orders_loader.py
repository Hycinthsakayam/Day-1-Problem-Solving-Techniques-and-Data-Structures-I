"""Small helper used by every task to read orders.csv."""
import csv
from pathlib import Path

CSV_PATH = Path(__file__).with_name("orders.csv")


def load_orders():
    with CSV_PATH.open() as f:
        return [
            {"orderId": r["orderId"], "customerId": r["customerId"],
             "amount": float(r["amount"]), "createdAt": r["createdAt"]}
            for r in csv.DictReader(f)
        ]
