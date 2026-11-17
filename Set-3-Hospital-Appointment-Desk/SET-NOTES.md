# Set 3 – Hospital Appointment Desk

| Task | Complexity | Rationale |
|---|---|---|
| Patient search | Linear O(n); binary O(log n) per lookup | Sorted patient IDs enable binary search. |
| Urgency sorting | Selection O(n²); quicksort average O(n log n), worst O(n²) | Sort by urgency then arrival; report swap counts. |
| Double booking | Average O(n), O(n) space | Hash set avoids O(n²) repeated list scans. |
| Walk-in queue / recent stack | Stack O(1); list queue dequeue O(n) | FIFO tokens and LIFO recent views. |
| Appointment scheduling | O(n log n), O(n) space | DP take/skip; earliest-finish greedy is also optimal for unweighted maximum-count scheduling. |

The DP objective is maximum appointment count, not weighted priority or revenue.