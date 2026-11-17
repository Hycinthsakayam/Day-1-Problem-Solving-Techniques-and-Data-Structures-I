"""Task 2 - sort a customer's statement by posting date with insertion sort and merge sort, and show why stability matters."""
import random
import time


def insertion_sort(items, key):
    a = list(items)
    for i in range(1, len(a)):
        cur, j = a[i], i - 1
        while j >= 0 and key(a[j]) > key(cur):      # strict '>' keeps equal items in order -> stable
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = cur
    return a


def merge_sort(items, key):
    if len(items) <= 1:
        return list(items)
    mid = len(items) // 2
    left, right = merge_sort(items[:mid], key), merge_sort(items[mid:], key)
    out, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if key(left[i]) <= key(right[j]):          # '<=' takes the left one first -> stable
            out.append(left[i]); i += 1
        else:
            out.append(right[j]); j += 1
    return out + left[i:] + right[j:]


def selection_sort(items, key):                    # not stable, used only to show the problem
    a = list(items)
    for i in range(len(a)):
        m = min(range(i, len(a)), key=lambda k: key(a[k]))
        a[i], a[m] = a[m], a[i]
    return a


# statement lines in the order the bank received them (seq), with posting time
statement = [
    (1, "2026-11-16 10:05", "Salary credit",        +85000),
    (2, "2026-11-16 09:30", "ATM withdrawal",        -2000),
    (3, "2026-11-16 10:05", "Rent transfer",        -18000),
    (4, "2026-11-16 08:15", "UPI - milk",              -60),
    (5, "2026-11-16 10:05", "Credit card payment",  -12000),
]
posted = lambda t: t[1]

def show(title, rows):
    print(title)
    balance = 5000
    for seq, at, desc, amt in rows:
        balance += amt
        print(f"  seq {seq}  {at}  {desc:<20} {amt:>8}  balance {balance:>7}")

show("Received order:", statement)
show("\nInsertion sort by posting time (stable):", insertion_sort(statement, posted))
show("\nMerge sort by posting time (stable):", merge_sort(statement, posted))
show("\nSelection sort by posting time (NOT stable):", selection_sort(statement, posted))

print("\nThree lines share 10:05. A stable sort keeps them in received order (salary first), so the running")
print("balance never dips. The unstable sort moves the credit-card payment before the salary, and the statement")
print("shows a negative balance that never really happened.")

random.seed(5)
big = [(i, f"2026-11-{random.randint(1, 30):02d} {random.randint(0, 23):02d}:00", "txn", 1) for i in range(5000)]
for name, fn in [("insertion sort", insertion_sort), ("merge sort", merge_sort)]:
    start = time.perf_counter()
    result = fn(big, posted)
    print(f"\n{name:<15} 5,000 lines: {time.perf_counter() - start:.4f} s, stable: "
          f"{all(a[0] < b[0] for a, b in zip(result, result[1:]) if a[1] == b[1])}", end="")
print()
