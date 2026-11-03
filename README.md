# SIMATS Python Programming Lab – Assignment 1
## Payment Calculator for a Village Milk Co-operative

**Student name:** [Enter your name]  
**Register number:** [Enter your register number]  
**Course:** CSA08 – Python Programming I  
**Assignment:** 1  
**Python version:** Python 3.10 or later

## Project overview
This project calculates milk payments using litres, fat percentage and SNF percentage. It supports regular and April–June seasonal rate cards, validates entries, uses `Decimal` for money, and adds a ten-day bonus when total supply is strictly greater than 500 litres.

## Folder guide
- `milkrate.py` – rate constants, validation, rate and payout functions.
- `main.py` – interactive command-line program.
- `test_milkrate.py` – automated test cases.
- `task02_decimal_demo.py` – float versus Decimal demonstration.
- `benchmark.py` – timing experiment for 300, 6,000 and 150,000 entries.
- `Task01/` through `Task12/` – separate task folders, each with its explanation, relevant source file(s), and an evidence folder for your screenshots.
- `docs/` – consolidated task explanations for convenient reading.
- `evidence/` – sample output and places to add your own execution screenshots.
- `flowchart.mmd` – flowchart source.

## How to run
Open a terminal in this folder and run:

```bash
python main.py
```

Run automated tests:

```bash
python -m unittest -v
```

Run the Decimal demonstration:

```bash
python task02_decimal_demo.py
```

Run the timing experiment:

```bash
python benchmark.py
```

## Important assumptions
1. Fat must be between 2.0% and 7.0%, inclusive; quantity must be positive; SNF must be non-negative.
2. Each 0.1 percentage-point difference is counted as a whole step.
3. For analyser readings with two decimal places, fractional step counts are rounded to the nearest whole step using decimal `ROUND_HALF_UP`. This is an explicit interpretation to make the rule deterministic; confirm with your lecturer if the co-operative uses a different policy.
4. April, May and June use the seasonal card. All other months use the regular card.
5. A bonus is paid only when the farmer's combined ten-day supply is greater than 500 litres. If eligible, Rs 0.50 is added for every litre in that ten-day period.
6. Individual entry payments are rounded to paise before being added to the ten-day total. The bonus is then added and the final total is rounded to paise.

## Submission checklist
- Replace all student placeholders in this README and report.
- Run all Python files and save fresh screenshots in `evidence/`.
- Check the actual output on your own system; execution times vary by device.
- Create one GitHub repository named `CSA08-<RegisterNumber>-Assignment1`.
- Upload the contents of this folder, not just the ZIP file.
- Commit each task progressively and share the repository URL with your faculty.
- Export or print the report PDF and upload it to the SIMATS portal.

## Academic note
Use this as a prepared working draft and learning aid. Read the explanations, run the code yourself, verify the outputs, and be prepared to explain the assumptions and design choices during evaluation.
