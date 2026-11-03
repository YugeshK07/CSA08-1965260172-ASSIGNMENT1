"""Command-line application for the village milk co-operative."""
from decimal import Decimal, InvalidOperation
from milkrate import rate_per_litre, payout, ten_day_total


def read_decimal(prompt):
    """Read a decimal number and reject non-numeric text."""
    while True:
        text = input(prompt).strip()
        try:
            return Decimal(text)
        except InvalidOperation:
            print("Invalid number. Enter a value such as 10 or 4.25.")


def main():
    print("Ksheera Village Milk Co-operative - Payment Calculator")
    print("Enter the month number (1=January ... 12=December).")
    month = int(read_decimal("Month: "))
    count = int(read_decimal("Number of milk entries for this farmer: "))
    if count <= 0:
        raise ValueError("Number of entries must be positive.")

    entries = []
    for index in range(1, count + 1):
        print(f"\\nEntry {index}")
        litres = read_decimal("Milk quantity (litres): ")
        fat = read_decimal("Fat percentage: ")
        snf = read_decimal("SNF percentage: ")
        entries.append((litres, fat, snf))
        print(f"Rate per litre: Rs {rate_per_litre(fat, snf, month):.2f}")
        print(f"Entry payment: Rs {payout(litres, fat, snf, month):.2f}")

    total, bonus, total_litres = ten_day_total(entries, month)
    print("\\n--- TEN-DAY PAYMENT SUMMARY ---")
    print(f"Total litres: {total_litres}")
    print(f"Bonus: Rs {bonus:.2f}")
    print(f"Total amount payable: Rs {total:.2f}")


if __name__ == "__main__":
    main()
