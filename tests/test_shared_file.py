import pytest
import shutil


from uscodekit.shared.file import copy_file_to_dir, rename_file


@pytest.fixture
def setup_files(tmp_path):
    # Create a temporary source file
    src_file = tmp_path / "source.txt"
    src_file.write_text("This is a test file.")

    # Create a temporary destination directory
    dest_dir = tmp_path / "dest"
    dest_dir.mkdir()

    yield src_file, dest_dir

    # Cleanup
    shutil.rmtree(tmp_path)


def test_copy_file_to_dir_success(setup_files):
    src_file, dest_dir = setup_files
    result = copy_file_to_dir(str(src_file), str(dest_dir))
    assert result is True
    assert (dest_dir / src_file.name).exists()


def test_copy_file_to_dir_file_not_found():
    result = copy_file_to_dir("non_existent_file.txt", "some_dir")
    assert result is False


def test_copy_file_to_dir_not_a_file(tmp_path):
    not_a_file = tmp_path / "not_a_file"
    not_a_file.mkdir()
    result = copy_file_to_dir(str(not_a_file), str(tmp_path))
    assert result is False


def test_rename_file_success(tmp_path):
    src_file = tmp_path / "source.txt"
    src_file.write_text("This is a test file.")
    new_name = tmp_path / "renamed.txt"
    result = rename_file(str(src_file), str(new_name))
    assert result is True
    assert new_name.exists()
    assert not src_file.exists()


def test_rename_file_not_found():
    result = rename_file("non_existent_file.txt", "new_name.txt")
    assert result is False
