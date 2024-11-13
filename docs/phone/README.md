<p align="center">
  <img src="../logo.png" alt="USCodeKit_logo" width="200"/>
</p>

# Phone Utility Functions Documentation

This documentation provides an overview of the `phone.py` utility functions, which handle validation, formatting, extraction, and insight retrieval for U.S. phone numbers. This utility is useful for developers looking to implement phone number processing in applications, ensuring consistent phone number handling across various formats.

---

## Table of Contents

- [Functions](#functions)
  - [is_valid_phone](#is_valid_phone)
  - [extract_phone_number](#extract_phone_number)
  - [extract_phone_numbers](#extract_phone_numbers)
  - [get_area_code](#get_area_code)
  - [cleaned_phone](#cleaned_phone)
  - [prettify](#prettify)
  - [phone_number_insight](#phone_number_insight)
- [Example Usage](#example-usage)
- [Contributing](#contributing)
- [License](#license)

---

## Functions

### `is_valid_phone`

```python
is_valid_phone(phone: str) -> bool
```

Validates if a string matches the U.S. phone number format. It supports various common formats and the optional U.S. country code `+1`.

- **Args**: `phone` (str): Phone number string to validate.
- **Returns**: `bool`: `True` if valid, `False` otherwise.

**Examples:**

```python
is_valid_phone("+1 (123) 456-7890")     # Returns: True
is_valid_phone("1 (123) 456-7890")      # Returns: False
is_valid_phone("(123) 456-7890")        # Returns: True
is_valid_phone("123 456-7890")          # Returns: True
is_valid_phone("123-456-7890")          # Returns: True
is_valid_phone("1234567890")            # Returns: True
is_valid_phone("+1 123 456-7890")       # Returns: True
is_valid_phone("1 123 456-7890")        # Returns: False
is_valid_phone("123456")                # Returns: False
is_valid_phone("123-45-7890")           # Returns: False
is_valid_phone("abc-def-ghij")          # Returns: False
```

---

### `extract_phone_number`

```python
extract_phone_number(text: str) -> str | None
```

Extracts the first matched valid U.S. phone number from a given text and formats them to `(XXX) XXX-XXXX`.

- **Args**: `text` (str): Text from which to extract phone number.
- **Returns**: `str or None`: formatted phone numbers or None if not matched any.

**Example:**

```python
extract_phone_number("Call (123) 456-7890 or 987-654-3210.")
# Returns: (123) 456-7890
```

```python
extract_phone_number("Call me")
# Returns: None
```

---

### `extract_phone_numbers`

```python
extract_phone_numbers(text: str) -> list[str]
```

Extracts all valid U.S. phone numbers from a given text and formats them to `(XXX) XXX-XXXX`.

- **Args**: `text` (str): Text from which to extract phone numbers.
- **Returns**: `list[str]`: List of formatted phone numbers.

**Example:**

```python
extract_phone_numbers("Call (123) 456-7890 or 987-654-3210.")
# Returns: ["(123) 456-7890", "(987) 654-3210"]
```

```python
extract_phone_numbers("Call me")
# Returns: []
```

---

### `get_area_code`

```python
get_area_code(phone: str) -> str
```

Extracts the area code from a U.S. phone number.

- **Args**: `phone` (str): Phone number to extract the area code from.
- **Returns**: `str`: The extracted area code.
- **Raises**: `AttributeError` if the phone number is invalid.

**Examples:**

```python
get_area_code("(123) 456-7890")         # Returns: "123"
get_area_code("123-456-7890")           # Returns: "123"
get_area_code("123456")                 # Raises: AttributeError
```

---

### `cleaned_phone`

```python
cleaned_phone(phone: str) -> str
```

Removes non-numeric characters from a phone number, returning a 10-digit U.S. phone number if valid.

- **Args**: `phone` (str): The phone number with possible non-numeric characters.
- **Returns**: `str`: Cleaned 10-digit phone number.
- **Raises**: `ValueError` if the cleaned number is not valid.

**Examples:**

```python
cleaned_phone("(123) 456-7890")         # Returns: "1234567890"
cleaned_phone("+1-123-456-7890")        # Returns: "1234567890"
cleaned_phone("123-45-789")             # Raises: ValueError
```

---

### `prettify`

```python
prettify(phone_str: str) -> str | None
```

Formats a U.S. phone number string into `(XXX) XXX-XXXX`. It supports 10-digit and 11-digit formats (11 with leading `1`).

- **Args**: `phone_str` (str): Phone number string to format.
- **Returns**: `str | None`: Formatted phone number or `None` if invalid.

**Examples:**

```python
prettify("1234567890")                  # Returns: "(123) 456-7890"
prettify("18234567890")                 # Returns: "(823) 456-7890"
prettify("123456")                      # Raises: ValueError
```

---

### `phone_number_insight`

```python
phone_number_insight(phone: str) -> dict
```

Retrieves insights based on a phone number, including area code and associated location details. Requires an area code lookup service (e.g., `CodeService`).

- **Args**: `phone` (str): The phone number to analyze.
- **Returns**: `dict`: A dictionary containing detailed information about the phone number.

**Example:**

```python
phone_number_insight("(617) 456-7890")
```

Returns:

```json
{
  "phone": "(617) 123-4567",
  "areaCode": "617",
  "city": "Cambridge",
  "state": "Massachusetts",
  "stateISO": "MA",
  "location": { "latitude": 42.372, "longitude": -71.1137 },
  "timezone": { "name": "EST", "offset": "UTC-5" }
}
```

---

## Example Usage

Below are examples demonstrating the functions’ flexibility and handling of multiple phone number formats.

```python
from uscodekit.phone import (
    is_valid_phone,
    format_phone_number,
    extract_phone_numbers,
    get_area_code,
    cleaned_phone,
    prettify,
    phone_number_insight,
)

# Validate various phone number formats
print(is_valid_phone("(123) 456-7890"))      # True
print(is_valid_phone("+1 123 456 7890"))     # True
print(is_valid_phone("12345"))               # False

# Format a valid phone number
print(format_phone_number("1234567890"))     # "(123) 456-7890"

# Extract multiple phone numbers from text
text = "Contact at (123) 456-7890, or 987-654-3210."
print(extract_phone_numbers(text))           # ["(123) 456-7890", "(987) 654-3210"]

# Get area code from a formatted phone number
print(get_area_code("(123) 456-7890"))       # "123"

# Clean phone number by removing non-numeric characters
print(cleaned_phone("+1 (123) 456-7890"))    # "1234567890"

# Prettify a raw phone number
print(prettify("1234567890"))                # "(123) 456-7890"

# Retrieve insights based on a phone number
info = phone_number_insight("(617) 456-7890")
print(info.get("city"))                      # "Cambridge"
print(info.get("timezone"))                  # {"name": "EST", "offset": "UTC-5"}
```

---

## Contributing

Contributions to enhance this utility are welcome! Please fork the repository, make improvements in a new branch, and submit a pull request.

---

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

---

This document provides a complete guide to the phone utility functions, covering validation, formatting, extraction, and retrieval of insights for effective handling of U.S. phone numbers.
