# Set 2 – Retail Banking Transaction Review

| Task | Best / average / worst time | Space / rationale |
|---|---|---|
| Transaction search | Linear O(1)/O(n)/O(n); binary O(1)/O(log n)/O(log n) | O(1); binary needs sorted IDs. |
| Statement sorting | Insertion O(n)/O(n²)/O(n²); merge O(n log n) | O(1) insertion, O(n) merge; both stable. |
| Duplicate postings | Average O(n) plus comparisons within matching groups | O(n); group by account, amount, merchant and check 60 seconds. |
| Review queue / stack | Stack O(1); list queue dequeue O(n) | O(n); FIFO review and LIFO reversal. |
| Divide-and-conquer min/max | O(n) | O(log n) recursion; brute force is also O(n), O(1) extra. |