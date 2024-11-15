## Changelog

### Modified

- It seems that the provided file content is empty. If there were changes made to the `github/workflows/publish.yaml` file, please provide the specific details or a description of those changes, and I will help generate a meaningful changelog entry for you. (File: github/workflows/publish.yaml)
- ### Changelog Entry

- **Updated `.gitignore` file**:
  - Refined ignored patterns for `uscodekit/data/geo/` by specifying `.json`, `.gz`, and `.bin` file extensions.
  - Added new entries to ignore:
    - `data/` directory
    - `changelog.py` file (File: .gitignore)
- - Added a link to the "Resource Setup Guide" in the documentation table of contents. (File: docs/README.md)
- ### Changelog Entry

- **Refactored File Paths**: Updated file path and naming conventions for database-related files in `GeoConfig` and `NAICS2022Config` for consistency and clarity.

  - `GeoConfig`:
    - Changed `encrypted_database_fp` from "db.gz" to "geo.gz".
    - Adjusted `decompressed_data_fp` and `decompressed_json_fp` to "decompressed.geo.bin" and "decompressed.geo.json", respectively.
  - `NAICS2022Config`:
    - Renamed `encrypted_database_fp` from "database.bin" to "naics.bin".
    - Updated `search_data_fp` to "naics.json".

- **Enhanced Encryption Key Management**:
  - Introduced `root` and `encryption_key_name` attributes in `Config` for centralized management of encryption credentials.
  - Changed `encryption_key` reference to use `CREDS_DIR / "encryption.key"` for improved configurability.

This update standardizes configuration settings and simplifies the management of encryption keys and database files. (File: uscodekit/configs.py)

- ### Changelog Entry

- **Improved Phone Number Handling**: Updated the `phone_number_insight` function to enhance phone number processing. Introduced `cleaned_phone` and `prettify` steps before obtaining the area code, ensuring more accurate and formatted phone number data in the insights returned. (File: uscodekit/phone.py)
- ### Changelog Entry

- **Refactor:** Updated the method for retrieving the encryption key in the `get_database` function to use `Config.encryption_key_fp` instead of `Config.encryption_key`. This change clarifies the variable name, indicating that it is a file path. (File: uscodekit/services/geo.py)
- - **Updated NAICS2022Service Initialization and Database Search Logic**: Modified the initialization and database search operations in `NAICS2022Service` to check the existence of both the encryption key file and the encrypted database file before proceeding. This ensures that both files are present, improving the reliability of the service initialization and data retrieval processes. (File: uscodekit/services/naics.py)
- ### Changelog Entry

- **Improved Key Management for Encryption/Decryption Functions**: Updated the `decrypt` and `encrypt` functions in `jsonfile.py` to optionally accept an external key parameter. The functions now use the provided key if available, otherwise, they default to reading the encryption key from the file specified by `Config.encryption_key_fp`. This enhancement allows for more flexible and testable key management. Additionally, a minor import optimization was made by including `Any` from `typing`. (File: uscodekit/shared/jsonfile.py)

### Deleted

- Deleted file `uscodekit/data/naics/2022/database.bin`.

### Added

- Added file `uscodekit/data/naics/2022/naics.bin`.
