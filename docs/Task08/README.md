# Task 8 – Plan the algorithm before coding

## Pseudocode – one entry
START
INPUT month, litres, fat, snf
VALIDATE month and entry values
IF any value is invalid THEN
    OUTPUT error message
ELSE
    SELECT regular or seasonal rate card
    CALCULATE whole fat and SNF steps
    CALCULATE rate per litre
    CALCULATE entry payment
    OUTPUT rate and payment
ENDIF
END

## Pseudocode – ten-day total
START
SET total_litres and milk_total to 0
FOR each entry
    VALIDATE entry
    ADD entry litres to total_litres
    ADD rounded entry payout to milk_total
ENDFOR
IF total_litres > 500 THEN
    SET bonus to total_litres * 0.50
ELSE
    SET bonus to 0
ENDIF
OUTPUT milk_total + bonus
END

## Hand trace
Entry 1: 10 L, fat 3.5%, SNF 8.5%, regular month. Steps = 0 and 0; rate = Rs 30.00; payment = Rs 300.00.
Entry 2: 8.5 L, fat 4.2%, SNF 8.7%, regular month. Fat steps = 7; SNF steps = 2; rate = Rs 33.40; payment = Rs 283.90.
Entry 3: 12 L, fat 3.1%, SNF 8.3%, regular month. Fat steps = -4; SNF steps = -2; rate = Rs 27.80; payment = Rs 333.60.

## Storage alternative
A running total can calculate payment as each entry arrives, using O(1) extra space. Storing all entries uses O(n) space and is useful for audit, correction and reprinting receipts. Both approaches require O(n) processing. This solution stores entries for the ten-day bonus and audit trail.
