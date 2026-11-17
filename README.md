# Day 1 – Problem Solving Techniques and Data Structures I

**Mavericks Segue 2026 | Python Track | Assignment date: 14 October 2026**

This repository contains my Day 1 Python assignment solutions. The work is organised around the three scenarios and the exact task sequence in the trainer's assignment: a retail order desk, a retail banking transaction review, and a hospital appointment desk.

## Learning objectives

- Understand algorithm basics and compare time and space complexity.
- Apply linear search and binary search to suitable data.
- Implement and compare sorting techniques.
- Use hash-based structures to identify duplicate records.
- Implement stacks and queues and understand LIFO and FIFO behaviour.
- Apply greedy, divide-and-conquer and dynamic-programming approaches.
- Validate solutions with sample inputs and recorded console output.

## Assignment sets

| Set | Scenario | Main concepts |
|---|---|---|
| [Set 1 – Retail Order Desk](./Set-1-Retail-Order-Desk/) | Order lookup, dispatch ranking, duplicate orders and refunds | Linear/binary search, bubble/merge sort, hashing, stack, queue, greedy and DP |
| [Set 2 – Retail Banking Transaction Review](./Set-2-Retail-Banking/) | Transaction lookup, statement ordering and duplicate-posting review | Search comparison counts, stable sorting, hashing, FIFO/LIFO and divide-and-conquer |
| [Set 3 – Hospital Appointment Desk](./Set-3-Hospital-Appointment-Desk/) | Patient lookup, appointment urgency, double-booking prevention and scheduling | Search benchmarking, selection/quicksort, hash set, queue, stack and scheduling DP |

Each set contains five task folders. Folder names describe the question being solved, and each Python source file has a descriptive name rather than using one generic filename.

## Folder contents

Each task folder includes:

- A question-specific Python source file (for example, `order_search.py` or `appointment_scheduling_dp.py`).
- `output.txt` with the command used and the captured sample console output.
- `flowchart.svg` showing the solution process.

Each set also has a `SET-NOTES.md` file summarising the algorithm choices and complexity.

## Running a solution

1. Open the required task folder.
2. Open a terminal in that folder.
3. Run the Python file shown in the folder. For example:

```bash
python order_search.py
```

Use the actual filename in that task folder. The programs use Python's standard library; no third-party package is required.

### Input and benchmark notes

- **Set 1, Task 1:** If an `orders.csv` file is placed beside the Python script, the program reads it. Otherwise, it creates 50,000 deterministic demonstration records. Use the trainer-provided CSV for the assignment's actual data benchmark.
- Runtime measurements depend on the computer and Python environment. Compare the algorithms using the same input data and machine.
- Sample data printed in the output files is for demonstrating the program logic; replace it with trainer-provided data wherever the assignment specifies a supplied dataset.

## Repository map

```text
.
├── Set-1-Retail-Order-Desk/
│   ├── 01-order-search/
│   ├── 02-order-sorting/
│   ├── 03-duplicate-orders/
│   ├── 04-stack-queue/
│   ├── 05-refund-change/
│   └── SET-NOTES.md
├── Set-2-Retail-Banking/
│   ├── 01-transaction-search/
│   ├── 02-statement-sorting/
│   ├── 03-duplicate-postings/
│   ├── 04-review-queue-stack/
│   ├── 05-divide-conquer-min-max/
│   └── SET-NOTES.md
└── Set-3-Hospital-Appointment-Desk/
    ├── 01-patient-search/
    ├── 02-urgency-sorting/
    ├── 03-double-bookings/
    ├── 04-walkin-queue-stack/
    ├── 05-appointment-dp/
    └── SET-NOTES.md
```

## Day 1 completion checklist

- [x] Three assignment sets organised separately.
- [x] Fifteen task folders created.
- [x] Question-specific Python filenames.
- [x] Sample console output files.
- [x] Flowchart files for the tasks.
- [x] Complexity and data-structure notes for each set.

---
*Prepared as a learning and problem-solving submission for the Python Track – Day 1.*
