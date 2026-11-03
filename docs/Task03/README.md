# Task 3 – Choose variables and name constants

The solution uses descriptive names such as `litres`, `fat`, `snf`, `rate`, `bonus` and `total_litres`. Constants use uppercase names: `STANDARD_FAT`, `BASE_RATE` (stored in the rate card), `FAT_STEP_VALUE`, and `BONUS_PER_LITRE`.

Python does not enforce constants. Uppercase is a convention that tells programmers not to reassign the value. Dynamic typing means a name can refer to different types at different times, although this should be avoided in clear calculation code. Multiple assignment is `a, b = 1, 2`; swapping is `a, b = b, a` and does not need a temporary variable.

If rates were typed as magic numbers in every expression, a rate revision would require edits in many places and could be applied inconsistently. A dictionary rate card centralises values. Lookup and calculation remain O(1) per entry; the dictionary adds a small fixed memory cost.
