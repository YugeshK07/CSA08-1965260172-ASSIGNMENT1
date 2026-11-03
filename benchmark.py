"""Task 10: reproducible timing comparison. Run with python benchmark.py."""
from time import perf_counter
from decimal import Decimal
from milkrate import payout

SIZES = (300, 6000, 150000)

for n in SIZES:
    entries = [("10", "3.5", "8.5")] * n
    start = perf_counter()
    total = sum((payout(*entry) for entry in entries), Decimal("0"))
    elapsed = perf_counter() - start
    print(f"{n:>6} payments | total Rs {total:.2f} | {elapsed:.6f} seconds")
