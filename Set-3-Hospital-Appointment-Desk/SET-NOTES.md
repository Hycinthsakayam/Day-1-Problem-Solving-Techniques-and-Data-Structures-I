# Set 3 – Hospital Appointment Desk

## Complexity and rationale

| Task | Solution | Time | Space | Why |
|---|---|---|---|---|
| 1 | Binary search on records sorted by patient ID | O(log n) | O(1) | ~157× faster than linear search for 1,000 look-ups |
| 2 | Selection sort | O(n²) | O(1) | Fewest swaps (≤ n−1) but many comparisons – 0.62 s for 2,000 |
| 2 | Quick sort (key = urgency, arrival, token) | O(n log n) average | O(log n) | More swaps but far fewer comparisons – 0.0075 s |
| 3 | Set of (patientId, slot) | O(1) per booking | O(n) | A list scan is O(n) per booking → O(n²) overall, too slow for a live desk |
| 4 | Circular-array queue, array stack | O(1) | O(capacity) | Tokens are served FIFO; "back" in history is LIFO |
| 5 | DP over slots sorted by end time | O(n log n) | O(n) | Tries take/skip for every slot; earliest-finish greedy matches it, other greedy rules can fail |
