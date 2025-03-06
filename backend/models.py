from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from database import Base

# Model
class CountryEconomy(Base):
    __tablename__ = 'country_economy'

    id = Column(Integer, primary_key=True, index=True)
    country_name = Column(String, index=True)
    gdp = Column(Float)
    inflation_rate = Column(Float)
    unemployment_rate = Column(Float)

# Any
