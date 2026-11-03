# Task 10 – Compare expectations with execution

The Decimal demonstration shows why binary float can accumulate small representation errors for money. Decimal values created from strings represent decimal currency exactly. Integer paise is another exact option: convert Rs 33.40 to 3340 paise, add integers, then divide by 100 only for display.

Run `python benchmark.py` to measure 300, 6,000 and 150,000 entries with `time.perf_counter()`. Record the actual times from your own computer in the table below; times depend on CPU, Python version and background load.

| Entries | Expected total for Rs 300 each | Your measured time |
|---:|---:|---:|
| 300 | Rs 90,000.00 | [Fill after run] |
| 6,000 | Rs 1,800,000.00 | [Fill after run] |
| 150,000 | Rs 45,000,000.00 | [Fill after run] |

The calculation is O(n) time. If every payment is rounded before summing, the total can differ from rounding only once at the end. The assignment asks for bank-correct payments; this project explicitly rounds each entry to paise and then adds the entries, matching a receipt/ledger approach. The co-operative should confirm its official accounting policy.
