"""
Rate card and payment calculations for the village milk co-operative.

Assumptions:
1. Fat and SNF adjustments are counted in whole 0.1 percentage-point steps.
2. When the analyser reports hundredths, the number of 0.1 steps is rounded
   to the nearest whole step using ROUND_HALF_UP.
3. Fat is accepted from 2.00% through 7.00%, inclusive.
4. Quantity must be positive. SNF must be non-negative.
5. Each entry's milk payment is rounded to two decimal places. The ten-day
   bonus is calculated on all litres if the farmer's total is strictly > 500 L.
"""
from decimal import Decimal, ROUND_HALF_UP

CENT = Decimal("0.01")
STEP = Decimal("0.1")
STANDARD_FAT = Decimal("3.5")
STANDARD_SNF = Decimal("8.5")
MIN_FAT = Decimal("2.0")
MAX_FAT = Decimal("7.0")
BONUS_THRESHOLD_LITRES = Decimal("500")
BONUS_PER_LITRE = Decimal("0.50")

RATE_CARDS = {
    "regular": {
        "base": Decimal("30.00"),
        "fat_step": Decimal("0.40"),
        "snf_step": Decimal("0.30"),
    },
    "seasonal": {
        "base": Decimal("32.00"),
        "fat_step": Decimal("0.45"),
        "snf_step": Decimal("0.30"),
    },
}
SEASONAL_MONTHS = {4, 5, 6}


def money(value):
    """Return a Decimal amount rounded to the nearest paise."""
    return Decimal(value).quantize(CENT, rounding=ROUND_HALF_UP)


def season_for_month(month):
    """Return 'seasonal' for April-June; otherwise return 'regular'."""
    if not isinstance(month, int) or not 1 <= month <= 12:
        raise ValueError("Month must be an integer from 1 to 12.")
    return "seasonal" if month in SEASONAL_MONTHS else "regular"


def validate_entry(litres, fat, snf):
    """Validate quantity, fat and SNF readings; raise ValueError if invalid."""
    litres, fat, snf = Decimal(str(litres)), Decimal(str(fat)), Decimal(str(snf))
    if litres <= 0:
        raise ValueError("Milk quantity must be greater than zero.")
    if not MIN_FAT <= fat <= MAX_FAT:
        raise ValueError("Fat must be between 2.0% and 7.0%, inclusive.")
    if snf < 0:
        raise ValueError("SNF cannot be negative.")
    return litres, fat, snf


def whole_steps(reading, standard):
    """Count 0.1 percentage-point steps, rounding hundredth readings half-up."""
    difference = Decimal(str(reading)) - Decimal(str(standard))
    return int((difference / STEP).quantize(Decimal("1"), rounding=ROUND_HALF_UP))


def rate_per_litre(fat, snf, month=1):
    """Calculate the per-litre rate for the month, rounded to two decimals."""
    _, fat, snf = validate_entry(1, fat, snf)
    card = RATE_CARDS[season_for_month(month)]
    fat_steps = whole_steps(fat, STANDARD_FAT)
    snf_steps = whole_steps(snf, STANDARD_SNF)
    rate = (card["base"]
            + Decimal(fat_steps) * card["fat_step"]
            + Decimal(snf_steps) * card["snf_step"])
    return money(rate)


def payout(litres, fat, snf, month=1):
    """Calculate one milk-entry payment, rounded to two decimal places."""
    litres, fat, snf = validate_entry(litres, fat, snf)
    return money(litres * rate_per_litre(fat, snf, month))


def ten_day_total(entries, month=1):
    """
    Calculate ten-day payment for entries shaped as (litres, fat, snf).
    If total litres are strictly greater than 500, add Rs 0.50 for every litre.
    """
    checked = [validate_entry(*entry) for entry in entries]
    total_litres = sum((entry[0] for entry in checked), Decimal("0"))
    milk_total = sum(
        (payout(litres, fat, snf, month) for litres, fat, snf in checked),
        Decimal("0")
    )
    bonus = total_litres * BONUS_PER_LITRE if total_litres > BONUS_THRESHOLD_LITRES else Decimal("0")
    return money(milk_total + bonus), money(bonus), total_litres
