# Task 9 – Implement and test the calculator

Run `python -m unittest -v`. The test suite checks standard rates, higher and lower readings, seasonal rates, two-decimal readings, bonus eligibility and invalid values.

| Case | Expected behaviour |
|---|---|
| 10 L, 3.5 fat, 8.5 SNF, January | Rs 300.00 |
| 8.5 L, 4.2 fat, 8.7 SNF, January | Rate Rs 33.40; Rs 283.90 |
| 12 L, 3.1 fat, 8.3 SNF, January | Rate Rs 27.80; Rs 333.60 |
| Fat = 2.0 or 7.0 | Accepted |
| Fat below 2.0 or above 7.0 | Rejected |
| Negative or zero litres | Rejected |
| Exactly 500 L in ten days | No bonus |
| 501 L in ten days | Rs 250.50 bonus |

The automated test file is repeatable, unlike manually typing inputs for every test. Add screenshots of your own test execution to the `evidence/` folder.
