# data_file_name -> Path to our data source

# model_file_name -> The folder containing are model config files

# model_name -> The name of the model which we should use

from pydantic_settings import BaseSettings,SettingsConfigDict
from pydantic import DirectoryPath, FilePath
from sqlalchemy import create_engine
from loguru import logger 

class Settings(BaseSettings):
  model_config = SettingsConfigDict(env_file='config/.env',env_file_encoding='utf-8')
  
  data_file_name:str
  data_dir:str
  model_dir:str 
  model_file_name: str
  rent_apart_table_name:str
settings = Settings()
logger.add('logs/app.log',rotation="1 day",retention ="2 days" , compression = 'zip')


engine = create_engine('sqlite:///db/db.sqlite')
