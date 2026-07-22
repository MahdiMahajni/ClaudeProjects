import unittest
from datetime import date

from date_parser import parse_date


class ParseDateTests(unittest.TestCase):
    def test_valid_date(self):
        self.assertEqual(parse_date("03/04/2024"), date(2024, 4, 3))

    def test_valid_date_single_digit_day_and_month(self):
        self.assertEqual(parse_date("1/1/2024"), date(2024, 1, 1))

    def test_invalid_written_date_raises_value_error(self):
        with self.assertRaises(ValueError):
            parse_date("April 3rd, 2024")

    def test_invalid_day_out_of_range_raises_value_error(self):
        with self.assertRaises(ValueError):
            parse_date("32/01/2024")

    def test_invalid_month_out_of_range_raises_value_error(self):
        with self.assertRaises(ValueError):
            parse_date("15/13/2024")

    def test_wrong_format_raises_value_error(self):
        with self.assertRaises(ValueError):
            parse_date("2024-04-03")

    def test_empty_string_raises_value_error(self):
        with self.assertRaises(ValueError):
            parse_date("")

    def test_non_string_input_raises_value_error(self):
        with self.assertRaises(ValueError):
            parse_date(None)


if __name__ == "__main__":
    unittest.main()
