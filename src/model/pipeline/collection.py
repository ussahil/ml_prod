"""
This module provides ways to load from a database.

It includes a function to extract data from RentApartments table in the database and then load into pandas DataFrame
"""

import pandas as pd
from loguru import logger 

from db.db_model import RentApartments
from sqlalchemy import select

from config.config import settings
from  config.config import engine
# add a parameter for data path
def load_data(path =f"{settings.data_dir}/{settings.data_file_name}"):
  
  logger.info(f"Loading csv file at path {path}")
  
  """ Loads in the data"""
  return pd.read_csv(path)
# Test
def load_data_from_db()->pd.DataFrame:
  """
  Extract the entire RentApartments table from the Database
  
  Returns:
    pd.DataFrame:DataFrame conatining the RentApartments data
  """
  logger.info("Extracting the table from the database")
  query = select(RentApartments)
  return pd.read_sql(query,engine)