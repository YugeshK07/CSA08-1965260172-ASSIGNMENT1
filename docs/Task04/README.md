# Task 4 – Write correct expressions

For each entry:
1. `fat_steps = round((fat - 3.5) / 0.1)` using an explicitly selected rounding rule.
2. `snf_steps = round((snf - 8.5) / 0.1)`.
3. `rate = base + fat_steps * fat_step_value + snf_steps * snf_step_value`.
4. `amount = litres * rate`.

The implementation uses Decimal arithmetic and ROUND_HALF_UP for the step count and money rounding. This avoids relying on Python's built-in `round()` tie-to-even rule for decimal business rules.

Operator precedence: exponentiation occurs before unary minus in expressions such as `-2**2`, which evaluates to -4; use parentheses for clarity. `and` has higher precedence than `or`; parentheses improve readability. Chained comparison `2.0 <= fat <= 7.0` checks both bounds.

`round()` rounds to a chosen number of digits; `int()` truncates toward zero; `math.floor()` rounds down. For negative values, `int(-2.7)` is -2 while `floor(-2.7)` is -3. Truncation or floor instead of nearest-step rounding changes the adjustment and can bias rates. Step count and money rounding are different decisions and should be documented separately.
