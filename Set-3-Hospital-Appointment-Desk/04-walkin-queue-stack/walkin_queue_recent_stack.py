"""Task 4 - walk-in token line (Queue) and 'recent patients viewed' history (Stack), both from scratch."""


class TokenQueue:
    """Circular array queue with a fixed capacity."""
    def __init__(self, capacity=10):
        self.data = [None] * capacity
        self.head = 0
        self.size = 0

    def enqueue(self, item):
        if self.size == len(self.data):
            raise OverflowError("token line is full")
        self.data[(self.head + self.size) % len(self.data)] = item
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            raise IndexError("no one waiting")
        item = self.data[self.head]
        self.data[self.head] = None
        self.head = (self.head + 1) % len(self.data)
        self.size -= 1
        return item


class HistoryStack:
    """Array stack for recently viewed patients; drops the oldest when full."""
    def __init__(self, limit=5):
        self.items = []
        self.limit = limit

    def push(self, item):
        if item in self.items:
            self.items.remove(item)          # viewing again moves it to the top
        self.items.append(item)
        if len(self.items) > self.limit:
            self.items.pop(0)

    def pop(self):
        if not self.items:
            raise IndexError("history is empty")
        return self.items.pop()

    def peek_all(self):
        return list(reversed(self.items))


print("Walk-in token line")
line = TokenQueue(capacity=4)
for n, name in enumerate(["Arun", "Divya", "Karthik", "Meena"], start=101):
    line.enqueue((n, name))
    print(f"  token {n} issued to {name:<8} waiting: {line.size}")
try:
    line.enqueue((105, "Rahul"))
except OverflowError as e:
    print(f"  token 105 for Rahul -> {e}")
for _ in range(2):
    n, name = line.dequeue()
    print(f"  calling token {n} ({name})   waiting: {line.size}")
line.enqueue((105, "Rahul"))
print(f"  token 105 issued to Rahul    waiting: {line.size}  (reuses the freed slot)")
while line.size:
    n, name = line.dequeue()
    print(f"  calling token {n} ({name})   waiting: {line.size}")

print("\nRecent patients viewed (most recent first)")
history = HistoryStack(limit=4)
for pid in ["P100045", "P101233", "P100045", "P108800", "P104411", "P109900"]:
    history.push(pid)
    print(f"  viewed {pid}: {history.peek_all()}")
print(f"  back -> {history.pop()}, now {history.peek_all()}")
