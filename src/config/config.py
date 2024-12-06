"""
This module sets up the application configuration

It utlizes Pydantic's BasicSettings for configuration management, allowing setting to be read from environment variable and .env file
"""

from loguru import logger
from pydantic_settings import BaseSettings,SettingsConfigDict
from pydantic import DirectoryPath, FilePath
from sqlalchemy import create_engine
 

class Settings(BaseSettings):
  """
  Configuration setting for the application
  
  Attributes:
    model_config (SettingsConfigDict()): Model config,loaded from .env file
    model_path: (Directory Path): Filesystem path to model
    model_name (str): Name of the ML model
    db_con_str(str): Database connection string
    rent_apart_table_name : Name of the rental apartment table in DB
  """
  model_config = SettingsConfigDict(env_file='config/.env',env_file_encoding='utf-8')
  
  data_file_name:str
  data_dir:str
  model_dir:str 
  model_file_name: str
  rent_apart_table_name:str

# Initialize settings
settings = Settings()
logger.add('logs/app.log',rotation="1 day",retention ="2 days" , compression = 'zip')


engine = create_engine('sqlite:///db/db.sqlite')
