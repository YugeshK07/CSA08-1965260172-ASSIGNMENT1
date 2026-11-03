"""Automated tests for the milk payment calculator."""
import unittest
from decimal import Decimal
from milkrate import rate_per_litre, payout, ten_day_total, season_for_month, validate_entry


class MilkRateTests(unittest.TestCase):
    def test_standard_rate_regular(self):
        self.assertEqual(rate_per_litre("3.5", "8.5", 1), Decimal("30.00"))

    def test_sample_rate_regular(self):
        self.assertEqual(rate_per_litre("4.2", "8.7", 1), Decimal("33.40"))

    def test_sample_payout(self):
        self.assertEqual(payout("8.5", "4.2", "8.7", 1), Decimal("283.90"))

    def test_fat_below_standard(self):
        self.assertEqual(rate_per_litre("3.1", "8.3", 1), Decimal("27.80"))

    def test_seasonal_rate(self):
        self.assertEqual(rate_per_litre("3.5", "8.5", 4), Decimal("32.00"))

    def test_two_decimal_reading_round_half_up(self):
        # 4.25 is 7.5 steps above 3.5, rounded half-up to 8 steps.
        self.assertEqual(rate_per_litre("4.25", "8.63", 1), Decimal("33.50"))

    def test_bonus_more_than_500(self):
        total, bonus, litres = ten_day_total(
            [("251", "3.5", "8.5"), ("250", "3.5", "8.5")], 1
        )
        self.assertEqual(bonus, Decimal("250.50"))
        self.assertEqual(litres, Decimal("501"))
        self.assertEqual(total, Decimal("15280.50"))

    def test_no_bonus_at_exactly_500(self):
        total, bonus, litres = ten_day_total(
            [("250", "3.5", "8.5"), ("250", "3.5", "8.5")], 1
        )
        self.assertEqual(bonus, Decimal("0.00"))
        self.assertEqual(total, Decimal("15000.00"))

    def test_invalid_quantity(self):
        with self.assertRaises(ValueError):
            validate_entry("-1", "3.5", "8.5")

    def test_invalid_fat(self):
        with self.assertRaises(ValueError):
            validate_entry("10", "7.1", "8.5")

    def test_invalid_month(self):
        with self.assertRaises(ValueError):
            season_for_month(13)


if __name__ == "__main__":
    unittest.main(verbosity=2)
