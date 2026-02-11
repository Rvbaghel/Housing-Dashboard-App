import pandas as pd
from india_housing_datasets import load_housing,CITIES

def get_supported_cities():
    """
    Returns list of supported cities.
    """
    return CITIES


def load_city_data(city: str) -> pd.DataFrame:
    """
    Load housing data for a given city using india-housing-datasets library.

    Parameters:
    city (str): City name (e.g. 'mumbai', 'delhi')

    Returns:
    pd.DataFrame: Housing dataset
    """
    city = city.lower()

    if city not in CITIES:
        raise ValueError(f"City '{city}' is not supported.")

    df = load_housing(city)

    return df

