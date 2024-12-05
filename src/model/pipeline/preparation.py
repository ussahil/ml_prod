from model.pipeline.collection import load_data_from_db
import pandas as pd 
import re
from loguru import logger

def prepare_data():
  """Pre-Process the Dataset"""
  logger.info('Starting Pre Process Pipeline')
  #1) Load in the data
  data = load_data_from_db()
  # 2) encode the dataset
  data_encoded = encode_cat_cols(data)
  
  # parse the garden column
  df = parse_garden_col(data_encoded)
  
  return data_encoded
  
def encode_cat_cols(data):
  """ Encodes the categorical columns"""
  cols = ['balcony','parking', 'furnished', 'garage', 'storage']
  
  logger.info('Encoding categorical columns {cols} ')
  
  data_encoded = pd.get_dummies(data,columns= cols,drop_first=True)
  
  col = ['balcony_yes','parking_yes', 'furnished_yes', 'garage_yes', 'storage_yes']
  
  data_encoded[col] = data_encoded[col].astype(int)
  return data_encoded

def parse_garden_col(data):
  logger.info('Parsing Garden Column')
  """ Makes garden column into int"""
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