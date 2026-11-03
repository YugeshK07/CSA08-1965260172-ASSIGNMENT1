# Task 2 – Explore values and types in the interpreter

## Type exploration
`type(10)` is `int`; `type(10.0)` is `float`; `type("10")` is `str`; `type(True)` is `bool`; `type([10, 8.5])` is `list`.

## Division operators
- `7 / 2` gives `3.5` (true division).
- `7 // 2` gives `3` (floor division for positive values).
- `7 % 2` gives `1` (remainder).
- `-7 // 2` gives `-4`, because floor division rounds down toward negative infinity.

## Floating-point surprise
`0.1 + 0.2` is commonly displayed as `0.30000000000000004`; therefore `0.1 + 0.2 == 0.3` is `False`. Binary floating point stores approximations for many decimal fractions.

## Exact money
Use `Decimal` created from strings: `Decimal("0.1") + Decimal("0.2") == Decimal("0.3")` is `True`. Avoid `Decimal(float_value)`, because it imports the float's existing approximation. Use `Decimal(str(value))` if a value is already received from a numeric source.

## Complete-code result
Run `python task02_decimal_demo.py`. The expected Decimal total for 1,000 payments of Rs 33.40 plus three Rs 0.10 adjustments is Rs 33,400.30. The float result may display a small binary representation error.
