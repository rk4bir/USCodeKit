from . import phone
from . import zip_code
from .services.naics import NAICS2022Service

naics2k22 = NAICS2022Service()


__all__ = [
    "naics2k22",
    "phone",
    "zip_code",
]
