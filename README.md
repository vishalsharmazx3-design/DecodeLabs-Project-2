# Project 2: Expense Tracker

**DecodeLabs Industrial Training Kit — Batch 2026**

A command-line Python script that continuously accepts expense entries from a user, accumulates them into a running total, and displays the final amount spent.

## Goal

Build a script where users enter expense amounts (e.g., `100`, `50`, `20`) one at a time. The program adds each one to a running total and displays the **Total Spent** once the user is finished.

## Key Skills Practiced

- **Accumulator pattern** — `total += new_expense`, with `total` initialized *outside* the loop so state persists across iterations instead of resetting each time.
- **Defensive coding** — `try/except ValueError` guards against invalid (non-numeric) input so the program never crashes.
- **Sentinel values** — typing `quit` cleanly breaks out of the loop instead of relying on a fixed number of entries.
- **Separation of Process and Output** — the loop only computes; the final total is displayed once, after processing ends.

## How to Run

```bash
python3 expense_tracker.py
```

You'll be prompted to enter expenses one at a time:

```
========================================
   DecodeLabs Expense Tracker
========================================
Enter an expense amount and press Enter.
Type 'quit' at any time to stop and see your total.

Enter expense (or 'quit' to finish): 100
  Added: $100.00  |  Running Total: $100.00

Enter expense (or 'quit' to finish): 50
  Added: $50.00  |  Running Total: $150.00

Enter expense (or 'quit' to finish): quit
========================================
Transactions recorded : 2
FINAL TOTAL SPENT     : $150.00
========================================
```

## Input Handling

| Input          | Behavior                                      |
|----------------|------------------------------------------------|
| A positive number (e.g. `20`, `19.99`) | Added to the running total |
| A negative number | Rejected with an "Invalid Data" message |
| Non-numeric text (e.g. `ten`) | Rejected with an "Invalid Data" message, loop continues |
| `quit` (any case) | Ends input and prints the final total |

## Requirements

- Python 3.6+
- No external dependencies

## Files

- `expense_tracker.py` — the main script

## Possible Extensions (Stretch Goals)

- Track expenses by category (e.g., food, transport, bills)
- Save the transaction log to a `.csv` or `.txt` file
- Show min/max/average expense alongside the total
- Add an "undo last entry" option


