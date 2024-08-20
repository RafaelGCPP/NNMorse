
from prefixes import ITU_PREFIX_DATABASE, ITU_COUNTRY_DATABASE
import random
from typing import Optional

def generate_random_callsign(country: Optional[str] = None) -> str:
    """
    Generates a random callsign using a prefix from the ITU prefix database,
    a random digit, and a random combination of 1 to 3 uppercase letters.

    Args:
        country (str, optional): The country for which the callsign should be generated. Defaults to None.

    Returns:
        str: The generated callsign.
    """
    if country is None:
        prefix = random.choice(list(ITU_PREFIX_DATABASE.keys()))
    else:
        prefixes = ITU_COUNTRY_DATABASE.get(country, [])
        prefix = random.choice(list(prefixes))
        
    digit = random.randint(0, 9)
    letters = ''.join(random.choices(' ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=3)).replace(' ', '')
    callsign = f"{prefix}{digit}{''.join(letters)}"
    return callsign
