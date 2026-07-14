"""
Project 2: Expense Tracker
DecodeLabs - Industrial Training Kit (Batch 2026)

Goal:
    Continuously accept expense amounts from the user, accumulate them
    into a running total, and display the Total Spent when the user is done.

Key concepts demonstrated:
    - Accumulator pattern:  total = total + new_expense
    - State initialized OUTSIDE the loop (so it persists across iterations)
    - Defensive coding:     try/except to guard against invalid (non-numeric) input
    - Sentinel value:       typing 'quit' gracefully ends the input loop
"""


def track_expenses():
    # --- INITIALIZATION (Phase: Memory) ---
    # 'total' must live OUTSIDE the loop, otherwise it resets every iteration.
    total = 0.0
    count = 0

    print("=" * 40)
    print("   DecodeLabs Expense Tracker")
    print("=" * 40)
    print("Enter an expense amount and press Enter.")
    print("Type 'quit' at any time to stop and see your total.\n")

    # --- PROCESS (Phase: The Engine / Continuous Audit Loop) ---
    while True:
        raw_input_value = input("Enter expense (or 'quit' to finish): ").strip()

        # --- KILL SWITCH: Sentinel value check ---
        if raw_input_value.lower() == "quit":
            break

        # --- DEFENSIVE CODING: The Gatekeeper ---
        # Guard against non-numeric ("garbage") input so the program
        # never crashes and never corrupts the total.
        try:
            expense = float(raw_input_value)
        except ValueError:
            print("  Invalid Data: please enter a valid number (or 'quit').\n")
            continue

        if expense < 0:
            print("  Invalid Data: expense cannot be negative.\n")
            continue

        # --- ACCUMULATOR PATTERN: The Heartbeat of the Ledger ---
        total += expense
        count += 1
        print(f"  Added: ${expense:.2f}  |  Running Total: ${total:.2f}\n")

    # --- OUTPUT (Phase: Display / API Interface) ---
    print("=" * 40)
    if count == 0:
        print("No expenses were recorded.")
    else:
        print(f"Transactions recorded : {count}")
        print(f"FINAL TOTAL SPENT     : ${total:.2f}")
    print("=" * 40)


if __name__ == "__main__":
    track_expenses()
