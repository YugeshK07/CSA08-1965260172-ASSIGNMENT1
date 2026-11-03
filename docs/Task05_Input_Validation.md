# Task 5 – Read input and convert types

`input()` always returns a string. Convert numeric input using `Decimal(text)` for financial calculations. A string such as `eight` raises `InvalidOperation`; `8,5` is not accepted as a decimal point format and should be re-entered as `8.5`.

The command-line program uses a `try/except` loop to reject non-numeric values and ask again. The calculation module separately validates numeric ranges, so invalid data cannot silently enter the calculation. Output uses f-strings and two decimal places, for example `f"Payment: Rs {amount:.2f}"`.

An alternative is checking characters with string methods before conversion. That becomes complicated for signs, decimal points and whitespace. `try/except` is clearer and handles conversion errors directly. Both approaches are O(k) in the length of the input text; exception handling is especially useful for invalid cases.
