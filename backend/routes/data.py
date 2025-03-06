from fastapi import APIRouter
from services import world_bank

router = APIRouter()

@router.get("/economy/{country}/{indicator}")
def get_economy_data(country: str = 'US', indicator: str = 'NY.GDP.MKTP.CD'):
    # Get data from API
    world_bank_data = world_bank.get_world_bank_data(country_code=country, indicator=indicator)
    
    # Processing...
    return {
        "World Bank": world_bank_data
    }
