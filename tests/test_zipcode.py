import unittest
from unittest.mock import MagicMock


from uscodekit.services.geo import GeoService
from uscodekit.zip_code import extract_zip_code, extract_all_zip_codes, zip_code_insight


class TestZipCodeFunctions(unittest.TestCase):

    def test_extract_zip_code_5_digit(self):
        text = "The ZIP code for New York is 10001."
        self.assertEqual(extract_zip_code(text), "10001")

    def test_extract_zip_code_zip_plus_4(self):
        text = "My ZIP+4 code is 12345-6789."
        self.assertEqual(extract_zip_code(text), "12345-6789")

    def test_extract_zip_code_no_zip_code(self):
        text = "There is no ZIP code in this text."
        self.assertIsNone(extract_zip_code(text))

    def test_extract_zip_code_multiple_codes(self):
        text = "I have two ZIP codes: 12345 and 54321-9876."
        # Expect the first occurrence of ZIP code
        self.assertEqual(extract_zip_code(text), "12345")

    def test_extract_all_zip_codes_single_code(self):
        text = "Please use ZIP code 90210."
        self.assertEqual(extract_all_zip_codes(text), ["90210"])

    def test_extract_all_zip_codes_multiple_codes(self):
        text = "Available ZIP codes are 90210, 12345-6789, and 10001."
        self.assertEqual(extract_all_zip_codes(text), ["90210", "12345-6789", "10001"])

    def test_extract_all_zip_codes_no_codes(self):
        text = "No ZIP codes are found in this text."
        self.assertEqual(extract_all_zip_codes(text), [])
