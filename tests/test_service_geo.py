import json
import pytest
from unittest.mock import patch, mock_open
from uscodekit.services.geo import GeoService, get_cached_database


class MockConfig:
    encryption_key_fp = "mock_key"
    file_missing_message = "File not found."


class MockGeoConfig:
    encrypted_database_fp = "mock_encrypted_db"
    decompressed_data_fp = "mock_decompressed_data"
    decompressed_json_fp = "mock_decompressed_json"


@pytest.fixture
def geo_service():
    return GeoService()


# @patch("uscodekit.configs.GeoConfig", new=MockGeoConfig)
# @patch("uscodekit.configs.Config", new=MockConfig)
# def test_get_cached_database():
#     mock_data = [
#         {
#             "npa": "907",
#             "nxx": "200",
#             "npanxx": "907200",
#             "city": "Valdez",
#             "state": "Alaska",
#             "stateISO": "AK",
#             "country": "United States",
#             "countryISO": "US",
#             "zipCode": "99686",
#             "gmtOffset": "-9",
#             "gmtOffsetDST": "-8",
#             "dstObserved": "1",
#             "longitude": "-146.3572",
#             "timezone": {"name": "AKST", "offset": "UTC-9"},
#             "location": {"latitude": 61.1381, "longitude": -146.3572},
#         }
#     ]
#     with patch("builtins.open", mock_open(read_data=json.dumps(mock_data))):
#         result = get_cached_database()
#         assert result == mock_data


# @patch("uscodekit.configs.GeoConfig", new=MockGeoConfig)
# @patch("uscodekit.configs.Config", new=MockConfig)
# def test_geo_service_database(geo_service):
#     mock_data = [
#         {
#             "npa": "907",
#             "nxx": "200",
#             "npanxx": "907200",
#             "city": "Valdez",
#             "state": "Alaska",
#             "stateISO": "AK",
#             "country": "United States",
#             "countryISO": "US",
#             "zipCode": "99686",
#             "gmtOffset": "-9",
#             "gmtOffsetDST": "-8",
#             "dstObserved": "1",
#             "longitude": "-146.3572",
#             "timezone": {"name": "AKST", "offset": "UTC-9"},
#             "location": {"latitude": 61.1381, "longitude": -146.3572},
#         }
#     ]
#     with patch("builtins.open", mock_open(read_data=json.dumps(mock_data))):
#         result = geo_service.database
#         assert result == mock_data


@patch("uscodekit.configs.GeoConfig", new=MockGeoConfig)
@patch("uscodekit.configs.Config", new=MockConfig)
def test_get_phone_info(geo_service):
    mock_data = [
        {
            "npa": "907",
            "nxx": "200",
            "npanxx": "907200",
            "city": "Valdez",
            "state": "Alaska",
            "stateISO": "AK",
            "country": "United States",
            "countryISO": "US",
            "zipCode": "99686",
            "gmtOffset": "-9",
            "gmtOffsetDST": "-8",
            "dstObserved": "1",
            "longitude": "-146.3572",
            "timezone": {"name": "AKST", "offset": "UTC-9"},
            "location": {"latitude": 61.1381, "longitude": -146.3572},
        }
    ]
    with patch("builtins.open", mock_open(read_data=json.dumps(mock_data))):
        result = geo_service.get_phone_info("123")
        assert result == {}


# @patch("uscodekit.configs.GeoConfig", new=MockGeoConfig)
# @patch("uscodekit.configs.Config", new=MockConfig)
# def test_get_zip_code_info(geo_service):
#     mock_data = [
#         {
#             "zipCode": "99686",
#             "areaCode": "907",
#             "city": "Valdez",
#             "state": "Alaska",
#             "stateISO": "AK",
#             "location": {"latitude": 61.1381, "longitude": -146.3572},
#             "timezone": {"name": "AKST", "offset": "UTC-9"},
#         }
#     ]
#     with patch("builtins.open", mock_open(read_data=json.dumps(mock_data))):
#         result = geo_service.get_zip_code_info("99686")
#         assert result["city"] == "Valdez"
#         assert result["state"] == "Alaska"
#         assert result["stateISO"] == "AK"
#         assert result["location"]["latitude"] == 61.1381
#         assert result["location"]["longitude"] == -146.3572
#         assert result["timezone"]["name"] == "AKST"
#         assert result["timezone"]["offset"] == "UTC-9"
