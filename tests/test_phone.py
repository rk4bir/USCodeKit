# tests/test_phone.py

import unittest
from uscodekit.phone import (
    is_valid_phone,
    extract_phone_number,
    extract_phone_numbers,
    cleaned_phone,
    prettify,
)


class TestPhoneUtils(unittest.TestCase):

    def test_is_valid_phone(self):
        # Valid cases with different formats
        self.assertTrue(is_valid_phone("(123) 456-7890"))
        self.assertTrue(is_valid_phone("123 456-7890"))
        self.assertTrue(is_valid_phone("123 456 7890"))
        self.assertTrue(is_valid_phone("123-456-7890"))
        self.assertTrue(is_valid_phone("1234567890"))
        self.assertTrue(is_valid_phone("+1 123 456-7890"))
        self.assertTrue(is_valid_phone("+12345678900"))
        self.assertTrue(is_valid_phone("2345678900"))
        self.assertTrue(is_valid_phone("+1 (123) 456-7890"))
        self.assertTrue(is_valid_phone("(123)456-7890"))

        # Invalid cases with different formats
        self.assertFalse(is_valid_phone("1 (123) 456 7890"))
        self.assertFalse(is_valid_phone("123-45-7890"))
        self.assertFalse(is_valid_phone("123456789"))
        self.assertFalse(is_valid_phone("12345678901"))
        self.assertFalse(is_valid_phone("(123) 456-78901"))
        self.assertFalse(is_valid_phone("+12 123-456-7890"))
        self.assertFalse(is_valid_phone("123-4567-890"))
        self.assertFalse(is_valid_phone("(123 456-7890"))
        self.assertFalse(is_valid_phone("123) 456-7890"))
        self.assertFalse(is_valid_phone("abc-def-ghij"))

        self.assertFalse(is_valid_phone("00123 456 7890"))
        self.assertFalse(is_valid_phone("+44 123 456 7890"))
        self.assertFalse(is_valid_phone("++1 123 456 7890"))

    def test_extract_phone_number(self):
        self.assertEqual(extract_phone_number("123-456-7890"), "(123) 456-7890")
        self.assertEqual(extract_phone_number("(123) 456-7890"), "(123) 456-7890")
        self.assertEqual(extract_phone_number("123-45-7890"), None)

    def test_extract_phone_numbers(self):
        text = "Contact us at (123) 456-7890 or 987-654-3210."
        extracted = extract_phone_numbers(text)
        self.assertEqual(extracted, ["(123) 456-7890", "(987) 654-3210"])

    def test_cleaned_phone(self):
        self.assertEqual(cleaned_phone("(123) 456-7890"), "1234567890")
        self.assertEqual(cleaned_phone("+1-123-456-7890"), "1234567890")
        with self.assertRaises(ValueError):
            cleaned_phone("123-45-789")

    def test_prettify(self):
        self.assertEqual(prettify("1234567890"), "(123) 456-7890")
        self.assertEqual(prettify("18234567890"), "(823) 456-7890")
