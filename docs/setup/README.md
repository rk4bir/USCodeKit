# Documentation for Setup the data resources

## Overview

> This script provides utility functions to set up the configuration files required by the package. It checks for the existence of essential files (encryption key, geo database, and NAICS database) and assists in setting them up by copying and renaming files to their appropriate locations. You can download the resources [here](https://drive.google.com/drive/folders/1H0RMW-i2EYQaU3-F8DKPCxCXdyPOVie9?usp=sharing).

---

## Importing the setup module

```python
from uscodekit.setup import (
    setup_file_stats,
    setup_geo_database,
    setup_naics_database,
    setup_encryption_key,
    setup_all
)
```

## Functions

### 1. **`setup_file_stats`**

Checks the existence of configuration files and provides their status.

#### Parameters:

- `verbose` (bool, default=True): If `True`, prints the status of each file.

#### Returns:

- `Dict`: A dictionary indicating the presence of the files:
  - `"encryption_key"` (bool): `True` if the encryption key file exists.
  - `"geo_database"` (bool): `True` if the geo database file exists.
  - `"naics_database"` (bool): `True` if the NAICS database file exists.

---

### 2. **`setup_geo_database`**

Sets up the Geo database by copying a `.gz` file to the specified directory.

#### Parameters:

- `file_path` (str): Path to the `.gz` file.

#### Returns:

- `bool`: `True` if the setup is successful, `False` otherwise.

#### Raises:

- `ValueError`: If the provided file does not have a `.gz` extension.

#### Notes:

- If the Geo database is already set up, it will return `True` without duplicating efforts.
- Errors during the file copy process will be printed.

---

### 3. **`setup_naics_database`**

Sets up the NAICS database by copying a `.bin` file to the specified directory.

#### Parameters:

- `file_path` (str): Path to the `.bin` file.

#### Returns:

- `bool`: `True` if the setup is successful, `False` otherwise.

#### Raises:

- `ValueError`: If the provided file does not have a `.bin` extension.

#### Notes:

- If the NAICS database is already set up, it will return `True` without duplicating efforts.
- Errors during the file copy process will be printed.

---

### 4. **`setup_encryption_key`**

Sets up the encryption key by copying a `.key` file to the specified directory.

#### Parameters:

- `file_path` (str): Path to the `.key` file.

#### Returns:

- `bool`: `True` if the setup is successful, `False` otherwise.

#### Raises:

- `ValueError`: If the provided file does not have a `.key` extension.

#### Notes:

- If the encryption key is already set up, it will return `True` without duplicating efforts.
- Errors during the file copy process will be printed.

---

### 5. **`setup_all`**

Prompts the user for paths to the required files and sets them up.

#### Behavior:

- Prompts the user to provide file paths for:
  - Encryption key
  - Geo database
  - NAICS database
- Calls the respective setup functions for each file.

---

## Usage

1. **Check File Status:**

   ```python
   stats = setup_file_stats()
   print(stats)
   ```

   Output:

   ```plaintext
   Encryption key...OK
   Geo database...MISSING
   NAICS database...OK
   {'encryption_key': True, 'geo_database': False, 'naics_database': True}
   ```

2. **Set Up Geo Database:**

   ```python
   result = setup_geo_database("/path/to/geo_database.gz")
   print(result)  # True if successful
   ```

3. **Set Up NAICS Database:**

   ```python
   result = setup_naics_database("/path/to/naics_database.bin")
   print(result)  # True if successful
   ```

4. **Set Up Encryption Key:**

   ```python
   result = setup_encryption_key("/path/to/encryption_key.key")
   print(result)  # True if successful
   ```

5. **Set Up All Files:**
   ```python
   setup_all()
   ```
   This will prompt for file paths and set up all files interactively.

---

## Notes

- All configuration file paths must match their expected extensions.
- Error handling is in place to ensure robust execution and meaningful error messages.
- Ensure the required directory structure exists before running these setup functions.
