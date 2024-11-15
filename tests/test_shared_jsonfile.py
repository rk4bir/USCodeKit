import os
import json
import pytest
from cryptography.fernet import Fernet
from uscodekit.shared.jsonfile import decrypt, encrypt, read_data, write_data

# Create a fake encryption key for testing
fake_key = Fernet.generate_key()
fake_key_path = "/tmp/fake_key.key"
with open(fake_key_path, "wb") as key_file:
    key_file.write(fake_key)

# Mock Config to use the fake encryption key


class MockConfig:
    encryption_key_fp = fake_key_path


@pytest.fixture
def mock_config(monkeypatch):
    monkeypatch.setattr("uscodekit.configs.Config", MockConfig)


@pytest.fixture
def sample_data():
    return {"name": "test", "value": 123}


@pytest.fixture
def encrypted_file_path():
    return "/tmp/encrypted_test.json"


@pytest.fixture
def json_file_path():
    return "/tmp/test.json"


def test_encrypt_decrypt(mock_config, sample_data, encrypted_file_path):
    encrypt(encrypted_file_path, sample_data)
    decrypted_data = decrypt(encrypted_file_path)
    assert decrypted_data == sample_data


def test_read_data(json_file_path, sample_data):
    with open(json_file_path, "w") as f:
        json.dump(sample_data, f)
    data = read_data(json_file_path)
    assert data == sample_data


def test_read_data_file_not_found():
    data = read_data("/tmp/non_existent_file.json")
    assert data is None


def test_write_data(json_file_path, sample_data):
    result = write_data(json_file_path, sample_data)
    assert result is True
    with open(json_file_path, "r") as f:
        data = json.load(f)
    assert data == sample_data


def test_write_data_file_not_found():
    result = write_data("/non_existent_directory/test.json", {"key": "value"})
    assert result is False
