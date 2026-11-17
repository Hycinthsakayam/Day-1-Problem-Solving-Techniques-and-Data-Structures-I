"""Task 4 - manual-review backlog as a queue (FIFO) and 'reverse last adjustment' as a stack, without library collections."""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class ReviewQueue:
    def __init__(self):
        self.front = self.rear = None
        self.count = 0

    def enqueue(self, item):
        node = Node(item)
        if self.rear is None:
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = node
        self.count += 1

    def dequeue(self):
        if self.front is None:
            return None
        item = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.count -= 1
        return item

    def __len__(self):
        return self.count


class AdjustmentStack:
    def __init__(self):
        self.top = None
        self.count = 0

    def push(self, item):
        node = Node(item)
        node.next = self.top
        self.top = node
        self.count += 1

    def pop(self):
        if self.top is None:
            return None
        item = self.top.value
        self.top = self.top.next
        self.count -= 1
        return item


print("Manual-review backlog (first in, first out)")
backlog = ReviewQueue()
for txn in ["TXN104512 suspicious foreign POS", "TXN104577 velocity alert", "TXN104603 high value",
            "TXN104650 card-not-present"]:
    backlog.enqueue(txn)
    print(f"  flagged : {txn:<36} backlog = {len(backlog)}")
while len(backlog):
    print(f"  reviewed: {backlog.dequeue():<36} backlog = {len(backlog)}")
print(f"  dequeue on empty backlog -> {backlog.dequeue()}")

print("\nAdjustments on account ACC0042 (last in, first out)")
balance = 25_000.00
adjustments = AdjustmentStack()
for desc, amt in [("reverse ATM fee", +25.0), ("chargeback Swiggy", +450.0), ("late fee", -500.0)]:
    adjustments.push((desc, amt))
    balance += amt
    print(f"  apply   {desc:<18} {amt:>+8.2f}  balance {balance:>10,.2f}")
for _ in range(2):
    desc, amt = adjustments.pop()
    balance -= amt
    print(f"  reverse {desc:<18} {-amt:>+8.2f}  balance {balance:>10,.2f}")
print(f"  adjustments still applied: {adjustments.count}")
