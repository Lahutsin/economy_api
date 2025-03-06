import requests

def get_world_bank_data(country_code: str, indicator: str):
    """
    World Bank API:
    
    :param country_code: US
    :param indicator: NY.GDP.MKTP.CD (GDP)
    :return: json
    """
    url = f'http://api.worldbank.org/v2/country/{country_code}/indicator/{indicator}?format=json'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if len(data) > 1:
            return data[1]
        else:
            return None
    else:
        response.raise_for_status()
