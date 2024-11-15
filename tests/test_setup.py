import os
import pytest
from unittest.mock import patch, MagicMock
from uscodekit.configs import Config, NAICS2022Config, GeoConfig
from uscodekit.setup import (
    setup_file_stats,
    setup_geo_database,
    setup_naics_database,
    setup_encryption_key,
)


@pytest.fixture
def mock_config_paths():
    original_encryption_key_fp = Config.encryption_key_fp
    original_geo_database_fp = GeoConfig.encrypted_database_fp
    original_naics_database_fp = NAICS2022Config.encrypted_database_fp
    original_config_root = Config.root
    original_geo_root = GeoConfig.root
    original_naics_root = NAICS2022Config.root

    Config.encryption_key_fp = "/mock/path/encryption.key"
    GeoConfig.encrypted_database_fp = "/mock/path/geo.gz"
    NAICS2022Config.encrypted_database_fp = "/mock/path/naics.bin"
    Config.root = "/mock/path"
    GeoConfig.root = "/mock/path"
    NAICS2022Config.root = "/mock/path"

    yield

    Config.encryption_key_fp = original_encryption_key_fp
    GeoConfig.encrypted_database_fp = original_geo_database_fp
    NAICS2022Config.encrypted_database_fp = original_naics_database_fp
    Config.root = original_config_root
    GeoConfig.root = original_geo_root
    NAICS2022Config.root = original_naics_root


@patch("os.path.isfile")
def test_setup_file_stats(mock_isfile, mock_config_paths):
    mock_isfile.side_effect = lambda x: x in [
        Config.encryption_key_fp,
        GeoConfig.encrypted_database_fp,
        NAICS2022Config.encrypted_database_fp,
    ]
    stats = setup_file_stats(verbose=False)
    assert stats["encryption_key"] is True
    assert stats["geo_database"] is True
    assert stats["naics_database"] is True


@patch("os.path.isfile")
def test_setup_file_stats_missing_files(mock_isfile, mock_config_paths):
    mock_isfile.return_value = False
    stats = setup_file_stats(verbose=False)
    assert stats["encryption_key"] is False
    assert stats["geo_database"] is False
    assert stats["naics_database"] is False


@patch("uscodekit.setup.copy_file_to_dir")
@patch("uscodekit.setup.rename_file")
@patch("os.path.isfile")
def test_setup_geo_database(mock_isfile, mock_rename, mock_copy, mock_config_paths):
    mock_isfile.return_value = False
    result = setup_geo_database("/mock/path/geo.gz")
    assert result is True
    mock_copy.assert_called_once_with("/mock/path/geo.gz", GeoConfig.root)
    mock_rename.assert_called_once_with(
        old_name="/mock/path/geo.gz", new_name=GeoConfig.encrypted_database_fp
    )


@patch("os.path.isfile")
def test_setup_geo_database_already_exists(mock_isfile, mock_config_paths):
    mock_isfile.side_effect = lambda x: x == GeoConfig.encrypted_database_fp
    result = setup_geo_database("/mock/path/geo.gz")
    assert result is True


@patch("uscodekit.setup.copy_file_to_dir")
@patch("uscodekit.setup.rename_file")
@patch("os.path.isfile")
def test_setup_naics_database(mock_isfile, mock_rename, mock_copy, mock_config_paths):
    mock_isfile.return_value = False
    result = setup_naics_database("/mock/path/naics.bin")
    assert result is True
    mock_copy.assert_called_once_with("/mock/path/naics.bin", NAICS2022Config.root)
    mock_rename.assert_called_once_with(
        old_name="/mock/path/naics.bin", new_name=NAICS2022Config.encrypted_database_fp
    )


@patch("os.path.isfile")
def test_setup_naics_database_already_exists(mock_isfile, mock_config_paths):
    mock_isfile.side_effect = lambda x: x == NAICS2022Config.encrypted_database_fp
    result = setup_naics_database("/mock/path/naics.bin")
    assert result is True


@patch("uscodekit.setup.copy_file_to_dir")
@patch("uscodekit.setup.rename_file")
@patch("os.path.isfile")
def test_setup_encryption_key(mock_isfile, mock_rename, mock_copy, mock_config_paths):
    mock_isfile.return_value = False
    result = setup_encryption_key("/mock/path/encryption.key")
    assert result is True
    mock_copy.assert_called_once_with("/mock/path/encryption.key", Config.root)
    mock_rename.assert_called_once_with(
        old_name="/mock/path/encryption.key", new_name=Config.encryption_key_fp
    )


@patch("os.path.isfile")
def test_setup_encryption_key_already_exists(mock_isfile, mock_config_paths):
    mock_isfile.side_effect = lambda x: x == Config.encryption_key_fp
    result = setup_encryption_key("/mock/path/encryption.key")
    assert result is True
