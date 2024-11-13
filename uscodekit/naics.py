from uscodekit.services.naics import NAICS2022Service


def search(query: str, top_n: int = 10) -> list[dict]:
    """
    Searches the NAICS database for matches on both 'code' and 'title' fields,
    prioritizing exact matches, prefix matches, and then partial matches.

    Parameters:
        query (str): The search query to match against both 'code' and 'title'.

    Returns:
        list: A sorted list of dictionaries matching the query, ranked by relevance.


    Example:
    >>> search('Public Finance') =>
    [
        {'code': '92113', 'title': 'Public Finance Activities'},
        {'code': '921130', 'title': 'Public Finance Activities'}
    ]
    """
    return NAICS2022Service().search(query, top_n)


def industry(code: str) -> str | None:
    """
    Retrieve a dictionary from the NAICS database that matches the given code.

    Args:
        code (str): The code to search for in the database.

    Returns:
        dict | None: The dictionary that matches the given code if found, otherwise None.


    Example:
    >>> industry('921130') =>
    {
        'code': '921130',
        'title': 'Public Finance Activities'
    }
    """
    try:
        d = NAICS2022Service().get(code)
        return d.get("title") if d else None
    except Exception as e:
        return None


def industry_hierarchy(code: str) -> dict | None:
    """
    Generates the industry hierarchy for a given NAICS code.

    Args:
        code (str): The NAICS code for which the hierarchy is to be generated.

    Returns:
        dict | None: A dictionary representing the industry hierarchy if the code is valid,
                     otherwise None if an error occurs.
        Example:
        {
            'code': '921130',
            'title': 'Public Finance Activities',
            'sector': {
                'code': '92',
                'title': 'Public Administration'
            },
            'subsector': {
                'code': '921',
                'title': 'Executive, Legislative, and Other General Government Support'
            },
            'industry_group': {
                'code': '9211',
                'title': 'Executive, Legislative, and Other General Government Support'
            },
            'naics_industry': {
                'code': '92113',
                'title': 'Public Finance Activities'
            },
            'national_industry': {
                'code': '921130',
                'title': 'Public Finance Activities'
            }
        }
    """
    try:
        d = NAICS2022Service()
        return d.generate_hierarchy(code)
    except Exception as e:
        return None
