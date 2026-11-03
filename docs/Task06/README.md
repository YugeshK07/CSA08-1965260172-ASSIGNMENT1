# Task 6 – Organise the logic into functions

The module defines `validate_entry()`, `season_for_month()`, `whole_steps()`, `rate_per_litre()`, `payout()` and `ten_day_total()`. Each function has a focused responsibility, parameters and a return value, plus a docstring.

A parameter is an input to a function; a return value sends a result back to the caller. `print()` displays information but does not return the displayed result. Local variables exist inside the function. Constants are read from module scope and are not modified inside functions.

A single long script repeats logic and makes testing difficult. Functions make the code reusable and easier to test. Function-call overhead is generally small compared with processing a large number of entries; processing n entries remains O(n). Lambda expressions are best for short anonymous expressions, not multi-step validation and payment logic.
