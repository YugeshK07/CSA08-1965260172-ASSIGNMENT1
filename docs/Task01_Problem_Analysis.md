# Task 1 – Understand the problem and identify the data

## Problem
The Ksheera Village Milk Producers' Co-operative receives milk from farmers twice daily. For each entry it records quantity in litres, fat percentage and SNF percentage. The program calculates the rate per litre and payment, and supports a ten-day payment period.

## Inputs
- Farmer identifier (recommended for a production system).
- Milk quantity in litres: positive decimal.
- Fat percentage: decimal from 2.0% to 7.0%, inclusive.
- SNF percentage: non-negative decimal.
- Month number (1–12), used to select the rate card.
- All entries supplied by one farmer during the ten-day period.

## Outputs
- Selected rate card/season.
- Rate per litre.
- Payment for each milk entry.
- Ten-day total litres, bonus and final amount payable.

## Constants and rules
- Standard fat = 3.5%; standard SNF = 8.5%.
- Regular base rate = Rs 30.00/litre; fat step = Rs 0.40 per 0.1%; SNF step = Rs 0.30 per 0.1%.
- April–June seasonal base = Rs 32.00/litre; fat step = Rs 0.45; SNF step = Rs 0.30.
- Two-decimal analyser readings are converted to whole 0.1 steps using ROUND_HALF_UP.
- Bonus = Rs 0.50 for every litre if ten-day supply is strictly greater than 500 litres.

## Validation and assumptions
Quantity must be greater than zero. Fat must be within the stated permitted range. SNF cannot be negative. Month must be 1–12. The assignment does not state an upper SNF limit, so none is invented. A production system should also record farmer ID, date/time, operator and analyser calibration details.

## Alternative data design and complexity
For 300 entries, three separate lists (`litres`, `fat`, `snf`) require three append operations and careful index alignment. A list of tuples/records keeps related values together, reducing alignment mistakes. Both designs use O(n) storage and O(n) processing for n entries. The tuple/list-of-records design is safer and clearer; it does not change the asymptotic complexity.
