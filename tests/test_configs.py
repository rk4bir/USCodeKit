import pytest
from pathlib import Path

from uscodekit.configs import Config, DirConfig, GeoConfig, NAICS2022Config


def test_dir_config():
    assert DirConfig.root_dir == Path(__file__).resolve().parents[1]
    assert DirConfig.src_dir == DirConfig.root_dir / "uscodekit"
    assert DirConfig.data_dir == DirConfig.src_dir / "data"


def test_geo_config():
    assert GeoConfig.encrypted_database_filename == "geo.gz"
    assert GeoConfig.root == DirConfig.data_dir / "geo"
    assert GeoConfig.encrypted_database_fp == GeoConfig.root / "geo.gz"
    assert GeoConfig.decompressed_data_fp == GeoConfig.root / "decompressed.geo.bin"
    assert GeoConfig.decompressed_json_fp == GeoConfig.root / "decompressed.geo.json"


def test_naics2022_config():
    assert NAICS2022Config.edition == "2022"
    assert NAICS2022Config.root == DirConfig.data_dir / "naics/2022"
    assert NAICS2022Config.encrypted_database_filename == "naics.bin"
    assert NAICS2022Config.encrypted_database_fp == NAICS2022Config.root / "naics.bin"
    assert NAICS2022Config.search_data_fp == NAICS2022Config.root / "naics.json"


def test_config():
    assert Config.dir == DirConfig
    assert Config.geo == GeoConfig
    assert Config.root == DirConfig.src_dir / "creds"
    assert Config.encryption_key_name == "encryption.key"
    assert Config.encryption_key_fp == Config.root / "encryption.key"
    assert (
        Config.file_missing_message
        == "'''\nPlease contact the owner of this package for the \ngeo database and encryption key. To get original results.\nhttps://github.com/rk4bir\n'''"
    )
