# Task 7 – Build and import a module

`milkrate.py` stores the rate cards and reusable calculation functions. `main.py` imports them with `from milkrate import rate_per_litre, payout, ten_day_total`.

Run `python milkrate.py` to execute any optional direct tests placed under `if __name__ == "__main__":`. When another file imports the module, that condition is false, so the direct-test block does not run. Without the guard, demonstration code at module level would run during import.

Python searches the current script directory and locations listed in `sys.path` for imports. `decimal` is a standard-library module. Keeping shared logic in one module avoids copying rate formulas into every script. Python normally loads an imported module once per process and caches it in `sys.modules`; this avoids repeated loading within that process.
