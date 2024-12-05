# Handling the data loading

import pandas as pd
from config.config import settings

from loguru import logger 

from  config.config import engine
from db.db_model import RentApartments
from sqlalchemy import select
# add a parameter for data path
def load_data(path =f"{settings.data_dir}/{settings.data_file_name}"):
  
  logger.info(f"Loading csv file at path {path}")
  
  """ Loads in the data"""
  return pd.read_csv(path)
# Test
def load_data_from_db():
  logger.info("Extracting the table from the database")
  query = select(RentApartments)
  return pd.read_sql(query,engine)