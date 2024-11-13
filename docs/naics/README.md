# NAICS Code Documentation

> The North American Industry Classification System (NAICS) is the standard used by federal statistical agencies to classify business establishments for data collection, analysis, and publication related to the U.S. business economy. It allows for high comparability among business statistics in North America, grouping establishments based on production processes.

NAICS organizes codes in a hierarchical structure:

- **Sector**: 2-digit code
- **Subsector**: 3-digit code
- **Industry Group**: 4-digit code
- **NAICS Industry**: 5-digit code
- **National Industry**: 6-digit code

> **Note**: Some sectors cover ranges of 2-digit codes, such as Manufacturing (31-33), Retail Trade (44-45), and Transportation and Warehousing (48-49).

### Example

| Level             | NAICS Code | Title                                             |
| ----------------- | ---------- | ------------------------------------------------- |
| Sector            | 44-45      | Retail Trade                                      |
| Subsector         | 441        | Motor Vehicle and Parts Dealer                    |
| Industry Group    | 4412       | Other Motor Vehicle Dealers                       |
| NAICS Industry    | 44122      | Motorcycle, Boat, and Other Motor Vehicle Dealers |
| National Industry | 441222     | Boat Dealers                                      |

---

# NAICS2022 Overview

> A Python package for interacting with the NAICS 2022 database. It provides utilities for searching industry codes, retrieving details for specific codes, and generating hierarchical industry structures.

## Usage

### Importing the Module

```python
from uscodekit.services.naics import NAICS2022Service
```

## Functions

### `search(query: str, top_n: int = 10) -> list[dict]`

Searches the NAICS database for matches on both `code` and `title`, with results prioritized as exact matches, prefix matches, and partial matches.

- **Parameters:**

  - `query` (str): The term to match against the `code` and `title` fields.
  - `top_n` (int): Maximum number of results to return (default 10).

- **Returns:**
  - `list[dict]`: List of dictionaries matching the query, ranked by relevance.

#### Example

```python
from uscodekit.services.naics import search

results = search('Public Finance')
print(results)
```

Output:

```json
[
  { "code": "92113", "title": "Public Finance Activities" },
  { "code": "921130", "title": "Public Finance Activities" }
]
```

### `industry(code: str) -> dict | None`

Retrieves details for a specific NAICS code.

- **Parameters:**

  - `code` (str): The NAICS code to search for.

- **Returns:**
  - `dict | None`: Details of the code if found, otherwise `None`.

#### Example

```python
from uscodekit.services.naics import industry

result = industry('921130')
print(result)
```

Output:

```text
Public Finance Activities
```

### `industry_hierarchy(code: str) -> dict | None`

Generates the full industry hierarchy for a specified NAICS code.

- **Parameters:**

  - `code` (str): The NAICS code for which to generate the hierarchy.

- **Returns:**
  - `dict | None`: Dictionary representing the hierarchy if code is valid, otherwise `None`.

#### Example

```python
from uscodekit.services.naics import industry_hierarchy

hierarchy = industry_hierarchy('921130')
print(hierarchy)
```

Output:

```json
{
  "code": "921130",
  "title": "Public Finance Activities",
  "sector": {
    "code": "92",
    "title": "Public Administration"
  },
  "subsector": {
    "code": "921",
    "title": "Executive, Legislative, and Other General Government Support"
  },
  "industry_group": {
    "code": "9211",
    "title": "Executive, Legislative, and Other General Government Support"
  },
  "naics_industry": {
    "code": "92113",
    "title": "Public Finance Activities"
  },
  "national_industry": {
    "code": "921130",
    "title": "Public Finance Activities"
  }
}
```

3 digits example

```python
from uscodekit.services.naics import industry_hierarchy

hierarchy = industry_hierarchy('921')
print(hierarchy)
```

Output:

```json
{
  "code": "921",
  "title": "Executive, Legislative, and Other General Government Support",
  "sector": { "code": "92", "title": "Public Administration" },
  "subsector": {
    "code": "921",
    "title": "Executive, Legislative, and Other General Government Support"
  }
}
```

## Error Handling

Each function returns `None` if an error occurs, ensuring that unexpected input or server issues do not interrupt the application's flow.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contributing

Contributions are welcome! Submit a pull request with your changes. Ensure all tests pass before submission.
