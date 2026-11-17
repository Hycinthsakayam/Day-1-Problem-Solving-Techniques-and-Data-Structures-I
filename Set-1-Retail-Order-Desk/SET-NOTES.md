# Set 1 – Retail Order Desk

| Task | Complexity | Rationale |
|---|---|---|
| Order search | Linear O(n); binary O(log n) | Binary search is suitable after sorting IDs. |
| Sorting | Bubble O(n²); merge O(n log n) | Compare simple and scalable sorting approaches. |
| Duplicate orders | Average O(n), O(n) space | Hash key combines customer, amount and minute. |
| Undo / dispatch | Stack O(1); list queue dequeue O(n) | Undo is LIFO; dispatch is FIFO. A deque is better for production. |
| Refund | DP O(amount × denominations), O(amount) space | Greedy fails for amount 6 with [4,3,1]. |

Task 1 reads the trainer's orders.csv if present; otherwise it generates 50,000 deterministic demonstration records. Timings vary by hardware.