# Day 1 – Problem Solving Techniques and Data Structures I

This repository contains my solutions for the Day 1 Python assignment. Each question is in its own folder so it is easy to find the code, run it and see the output.

The assignment has three sets, with five questions in each set.

## What I'm working on

- Searching records with linear search and binary search.
- Sorting data and comparing O(n²) and O(n log n) methods.
- Finding duplicate records with dictionaries and sets.
- Writing my own stacks and queues and comparing them with the built-in ones.
- Trying greedy, divide-and-conquer and dynamic programming.
- Checking the output and the time and space complexity.

## Assignment sets

### Set 1 – Retail Order Desk
This set focuses on finding orders, sorting them by amount, identifying duplicate orders, managing edits and dispatch queues, and calculating refund change.

[Open Set 1](./Set-1-Retail-Order-Desk/)

### Set 2 – Retail Banking Transaction Review
This set covers searching transaction IDs, sorting bank statements, detecting duplicate postings, handling the review backlog and finding the minimum and maximum transaction amounts.

[Open Set 2](./Set-2-Retail-Banking/)

### Set 3 – Hospital Appointment Desk
This set includes patient search, sorting appointments by urgency, checking for double bookings, managing walk-in tokens and selecting appointments that fit a doctor's shift.

[Open Set 3](./Set-3-Hospital-Appointment-Desk/)

## How the folders are organised

Each question has its own folder. Inside, you can find:

- A Python file named after the question, such as `order_search.py` or `patient_search.py`.
- `output.txt` and `output.png` – the console output of a run (the screenshot shows it as it appeared in PowerShell).
- `README.md` with the question, how to run it and the output screenshot.
- `flowchart.svg`, which shows the steps followed in the solution.

Each set also has a `SET-NOTES.md` file with the complexity and data-structure notes.

Sets 1–3 also have a `data` folder with the sample data used by the questions (Set 1 builds `orders.csv` with `python data/generate_orders.py`).

## Running

Open the folder for the question, open a terminal there and run its Python file, for example:

```bash
python order_search.py
```

The programs only use Python's standard library, so no extra packages are needed. Timings in `output.txt` will change
from machine to machine.
