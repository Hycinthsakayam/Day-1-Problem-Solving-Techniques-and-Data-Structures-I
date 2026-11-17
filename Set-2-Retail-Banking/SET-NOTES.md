# Set 2 – Retail Banking Transaction Review

## Complexity table

| Task | Solution | Best | Average | Worst | Space | Justification |
|---|---|---|---|---|---|---|
| 1 | Binary search | O(1) – 1 comparison | O(log n) – 15.7 | O(log n) – 17 | O(1) | IDs are sorted, so each step halves the range |
| 1 | Linear search | O(1) | O(n) – ~50,000 | O(n) – 100,000 | O(1) | Shown for comparison only |
| 2 | Insertion sort | O(n) | O(n²) | O(n²) | O(1) | Stable and good for small, nearly sorted statements |
| 2 | Merge sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Stable and fast for large statements |
| 3 | Hash map (account, amount, merchant) → last posting | O(n) | O(n) | O(n) | O(n) | O(1) look-up of the previous matching posting; file is in time order |
| 4 | Linked-list queue / stack | O(1) | O(1) | O(1) | O(n) | Backlog is FIFO, reversing adjustments is LIFO |
| 5 | Divide and conquer | O(n) | O(n) | O(n) | O(log n) stack | ~3n/2 comparisons (7,950 vs 9,998) |
| 5 | Brute-force scan | O(n) | O(n) | O(n) | O(1) | 2(n−1) comparisons, but no recursion overhead, so faster in Python |

**Stability:** when two postings share a timestamp, a stable sort keeps them in the order the bank received them. In the
Task 2 output the unstable selection sort shows a negative balance that never happened.
