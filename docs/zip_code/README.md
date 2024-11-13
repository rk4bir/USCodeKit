<p align="center">
  <img src="../logo.png" alt="USCodeKit_logo" width="200"/>
</p>

# ZIP Code Utility Functions

This module provides utilities for validating, formatting, extracting, and analyzing U.S. ZIP codes.

## Table of Contents

- [Functions](#functions)
  - [extract_zip_code](#extract_zip_code)
  - [extract_all_zip_codes](#extract_all_zip_codes)
  - [zip_code_insight](#zip_code_insight)

## Functions

### extract_zip_code

```python
extract_zip_code(text: str) -> str | None
```

Extracts the first U.S. ZIP code found in the text (supports 5-digit and ZIP+4 formats).

- **Args**: `text` (str): Text to search for ZIP code.
- **Returns**: `str | None`: Found ZIP code or None if none.

Example:

```python
extract_zip_code("ZIP codes like 12345 or 12345-6789 are valid.")  # "12345"
```

### extract_all_zip_codes

```python
extract_all_zip_codes(text: str) -> list[str]
```

Extracts all U.S. ZIP codes from the text.

- **Args**: `text` (str): Text to search for ZIP codes.
- **Returns**: `list[str]`: List of extracted ZIP codes.

Example:

```python
extract_all_zip_codes("We serve 12345 and 67890-1234.")  # ["12345", "67890-1234"]
```

### zip_code_insight

```python
zip_code_insight(zip_code: str) -> dict
```

Retrieves insights based on a ZIP code, including area code, city, state, location, and timezone.

- **Args**: `zip_code` (str): ZIP code for which information is retrieved.
- **Returns**: `dict`: Detailed information about the ZIP code.

Example:

```python
zip_code_insight("12345")
```

Output

```json
{
  "zipCode": "02138",
  "areaCode": "617",
  "city": "Cambridge",
  "state": "Massachusetts",
  "stateISO": "MA",
  "location": { "latitude": 42.372, "longitude": -71.1137 },
  "timezone": { "name": "EST", "offset": "UTC-5" }
}
```
