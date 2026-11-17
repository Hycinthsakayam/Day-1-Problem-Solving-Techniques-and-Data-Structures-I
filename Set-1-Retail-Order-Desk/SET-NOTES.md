# Set 1 – Retail Order Desk

## Complexity and data-structure notes

| Task | Approach | Time | Space | Why this structure |
|---|---|---|---|---|
| 1 | Linear search | O(n) | O(1) | Works on unsorted data, but checks ~25,000 orders per look-up |
| 1 | Binary search | O(log n) | O(1) | Orders sorted by ID once; ≤16 checks per look-up (~158× faster in the run) |
| 2 | Insertion sort | O(n²) (O(n) if already sorted) | O(1) | Simple, in place; fine for tiny lists only (15.9 s for 10,000) |
| 2 | Merge sort | O(n log n) | O(n) | Predictable and stable (0.13 s); built-in Timsort is faster still (C code) |
| 3 | Dictionary keyed by (customer, amount, minute) | O(n) | O(n) | O(1) average look-up; a nested loop would be O(n²) |
| 4 | Linked-list Stack / Queue | O(1) per operation | O(n) | Undo is last-in-first-out; dispatch is first-in-first-out. `list` and `deque` do the same in C; `list.pop(0)` is O(n) |
| 5 | Greedy change | O(k + coins) | O(1) | Optimal for canonical sets like INR notes |
| 5 | Dynamic programming | O(amount × k) | O(amount) | Always optimal; needed when greedy fails (e.g. {1, 7, 10} for 14) |
