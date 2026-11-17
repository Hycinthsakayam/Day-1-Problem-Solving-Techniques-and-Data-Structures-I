"""Task 4 - own Stack (undo last order edit) and own Queue (dispatch line), then the built-in versions."""
import time
from collections import deque


class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class Stack:
    """Linked-list stack: push and pop at the head, both O(1)."""
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, value):
        self.top = Node(value, self.top)
        self.size += 1

    def pop(self):
        if self.top is None:
            raise IndexError("pop from empty stack")
        value = self.top.value
        self.top = self.top.next
        self.size -= 1
        return value

    def peek(self):
        return None if self.top is None else self.top.value

    def is_empty(self):
        return self.top is None


class Queue:
    """Linked-list queue: enqueue at the tail, dequeue at the head, both O(1)."""
    def __init__(self):
        self.head = self.tail = None
        self.size = 0

    def enqueue(self, value):
        node = Node(value)
        if self.tail:
            self.tail.next = node
        else:
            self.head = node
        self.tail = node
        self.size += 1

    def dequeue(self):
        if self.head is None:
            raise IndexError("dequeue from empty queue")
        value = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.size -= 1
        return value

    def is_empty(self):
        return self.head is None


# ---- undo last order edit ----
print("Undo last order edit (own Stack)")
order = {"orderId": "ORD000123", "qty": 1, "address": "Anna Nagar", "amount": 1499.0}
history = Stack()

def edit(field, value):
    history.push((field, order[field]))      # save the old value
    order[field] = value
    print(f"  edit  {field:<8} -> {value!s:<12} order = {order}")

def undo():
    field, old = history.pop()
    order[field] = old
    print(f"  undo  {field:<8} -> {old!s:<12} order = {order}")

edit("qty", 2)
edit("amount", 2998.0)
edit("address", "T Nagar")
undo()
undo()
print(f"  edits left to undo: {history.size}")

# ---- dispatch line ----
print("\nDispatch line (own Queue)")
line = Queue()
for oid in ["ORD000501", "ORD000502", "ORD000503", "ORD000504"]:
    line.enqueue(oid)
    print(f"  packed   {oid}  (waiting: {line.size})")
while not line.is_empty():
    print(f"  dispatch {line.dequeue()}  (waiting: {line.size})")

# ---- compare with built-ins ----
N = 200_000
print(f"\nTiming {N:,} push+pop / enqueue+dequeue operations")

def run(push, pop):
    start = time.perf_counter()
    for i in range(N):
        push(i)
    for _ in range(N):
        pop()
    return time.perf_counter() - start

s = Stack(); q = Queue(); lst = []; dq = deque(); bad = []
print(f"  own Stack             : {run(s.push, s.pop):.4f} s")
print(f"  list (append / pop)   : {run(lst.append, lst.pop):.4f} s")
print(f"  own Queue             : {run(q.enqueue, q.dequeue):.4f} s")
print(f"  deque (append/popleft): {run(dq.append, dq.popleft):.4f} s")
small = 20_000
start = time.perf_counter()
for i in range(small):
    bad.append(i)
for _ in range(small):
    bad.pop(0)
print(f"  list.pop(0) as a queue, only {small:,} ops: {time.perf_counter() - start:.4f} s  (O(n) per dequeue)")
print("\nBuilt-ins are faster because they are written in C; all are O(1) per operation except list.pop(0).")
