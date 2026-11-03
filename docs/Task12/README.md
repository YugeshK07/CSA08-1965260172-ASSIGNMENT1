# Task 12 – Re-evaluate and adapt the design

## A. Impact analysis
New analyser readings contain two decimal places, so the program must define how partial 0.1 percentage-point steps are treated. Seasonal rates change the base rate and fat-step value from April through June. A ten-day bonus is added only when the farmer's total supply is strictly greater than 500 litres.

## B. Evaluate the original design
A fixed rate card is no longer sufficient. The month must be passed to the rate function to select the correct card. The original one-entry payout is still useful, but the ten-day total must aggregate all entries before testing bonus eligibility. The analyser precision requires an explicit rounding rule.

## C. Adaptation
The updated module uses `season_for_month(month)` and two rate cards. `whole_steps()` uses Decimal `ROUND_HALF_UP` to convert a fractional number of 0.1 steps to the nearest whole step. The `ten_day_total()` function adds Rs 0.50 for every litre only when total litres > 500.

Worked example: in April, 10 L at 3.5% fat and 8.5% SNF gives Rs 32.00/litre and Rs 320.00. In January the same reading gives Rs 30.00/litre and Rs 300.00. For a ten-day supply of 501 L at the standard regular rate, milk value is Rs 15,030.00 and bonus is Rs 250.50, giving Rs 15,280.50. At exactly 500 L, bonus is zero.

## D. Evidence-based defence
Run the tests in `test_milkrate.py`, especially `test_seasonal_rate`, `test_two_decimal_reading_round_half_up`, `test_bonus_more_than_500` and `test_no_bonus_at_exactly_500`. Save the terminal output as evidence. The ROUND_HALF_UP interpretation is a documented assumption, not a fact explicitly specified by the assignment; confirm it with the lecturer/co-operative. If the official policy is to pay proportionally for hundredth-percent differences instead of rounding to whole 0.1 steps, change `whole_steps()` accordingly and update tests.
