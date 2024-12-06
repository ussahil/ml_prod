"""
This module provides functionality for preparing a dataset for ML model

It contains  functions to load data from database encode categorical columns and parse specific columns for future processing
"""

import re

import pandas as pd 
from loguru import logger

from model.pipeline.collection import load_data_from_db


def prepare_data():
  """
  Pre-Process the Dataset
  
  This involves leading the data,encoding categorical columns and parsing through the "garden" column
  
  Returns:
    pd.DataFrame:The processed dataset
  """
  logger.info('Starting Pre Process Pipeline')
  #1) Load in the data
  data = load_data_from_db()
  # 2) encode the dataset
  data_encoded = _encode_cat_cols(data)
  
  # parse the garden column
  df = _parse_garden_col(data_encoded)
  
  return df 
  
def _encode_cat_cols(data):
  """ 
  Encodes the categorical columns
  """
  cols = ['balcony','parking', 'furnished', 'garage', 'storage']
  
  logger.info('Encoding categorical columns {cols} ')
  
  data_encoded = pd.get_dummies(data,columns= cols,drop_first=True)
  
  col = ['balcony_yes','parking_yes', 'furnished_yes', 'garage_yes', 'storage_yes']
  
  data_encoded[col] = data_encoded[col].astype(int)
  return data_encoded

def _parse_garden_col(data):
  """ Makes garden column into int"""
  
  logger.info('Parsing Garden Column')
  
  if 'garden' not in data.columns:
      raise ValueError("The DataFrame does not contain a 'garden' column.")
    
    # Replace 'Not present' with 0 and extract numbers otherwise
  data['garden'] = data['garden'].apply(
        lambda x: 0 if x == 'Not present' else int(re.findall(r'\d+', x)[0])
    )
  return data


# Test
# df = prepare_data()
# print(df['garden'].unique())