# Day 1 – Problem Solving Techniques and Data Structures I

This repository contains my solutions for the Day 1 Python assignment. I have kept the programs in separate folders so that it is easy to find the code for each question and run it individually.

The assignment has three sets, with five questions in each set.

## What I'm working on

- Searching for records using linear search and binary search.
- Sorting data and comparing different sorting methods.
- Finding duplicate records using sets and dictionaries.
- Understanding stacks and queues through simple programs.
- Trying greedy, divide-and-conquer and dynamic programming approaches.
- Checking the output and understanding the time and space complexity.

## Assignment sets

### Set 1 – Retail Order Desk
This set focuses on finding orders, sorting them by amount, identifying duplicate orders, managing edits and dispatch queues, and calculating refund change.

[Open Set 1](./Set-1-Retail-Order-Desk/)

### Set 2 – Retail Banking Transaction Review
This set covers searching transaction IDs, sorting bank statements, detecting duplicate transactions, handling review requests and finding the minimum and maximum transaction amounts.

[Open Set 2](./Set-2-Retail-Banking/)

### Set 3 – Hospital Appointment Desk
This set includes patient search, sorting appointments by urgency, checking for double bookings, managing walk-in tokens and selecting appointments that fit a doctor's shift.

[Open Set 3](./Set-3-Hospital-Appointment-Desk/)

## How the folders are organised

Each question has its own folder. Inside, you can find:

- A Python file with a name related to the question, such as `order_search.py` or `patient_search.py`.
- `output.txt`, which shows a sample run of the program.
- `flowchart.svg`, which shows the steps followed in the solution.

I have also added a `SET-NOTES.md` file in each set for the complexity and algorithm notes.

## Running the programs

Open the folder for the question you want to try, then open a terminal in that folder and run its Python file.

For example:

```bash
python order_search.py
```

The filename will be different for each question. These programs use Python's standard library, so no extra packages are needed.

## A note about the sample data

For Set 1, Question 1, the program reads an `orders.csv` file if one is available in the same folder. If not, it creates 50,000 sample orders so that the search methods can still be tested.

The sample outputs are included to show how the programs run. Execution times may change depending on the system, so it is better to compare algorithms on the same machine and with the same input data.
