"""
This module provides functionality for managing a ML model

It contains the ModelService class,which handles loading and using a pre-trained ML model. The class offers methods to load a model from file , building it if it does not exist and to make predictions using the loaded model.
"""
import pickle as pk
from pathlib import Path

from loguru import logger

from config.config import settings
from model.pipeline.model import build_model


class ModalService:
  """
  A serive class for managing the ML model
  
  This class provides functionalility to load a ML model from a specified path but if it does not exist, then it builds it and then makes predictions using the loaded model
 
  Attributes:
    model:ML model managed by this service . Initially set to None

  Methods:
    __init__: Constructor that initializes the ModelService.
    load_mode: Loads the model from file or builds it if it does not exist.
    predict: Makes a prediction using the loaded model .
  """
  
  def __init__(self)-> None:
    """Initializes the ModelService with no model loaded"""
    self.model = None
    
    def load_model(self) -> None:
      """Loads the mode from a specified path, or builds it if does not exist"""
    logger.info(
      f'Checking the existence of model config at {settings.model_dir}/{settings.model_file_name}'
    )
    
    model_path = Path(f'{settings.model_dir}/{settings.model_file_name}')
    
    if not model_path.exists():
      logger.warning('Model at {settings.model_dir}/{settings.model_file_name} was not found -> Building {settings.model_file_name}')
    
      build_model()
    
    logger.info(f'Model exists config file loading')
    
    self.model = pk.load(open(f'{settings.model_dir}/{settings.model_file_name} ','rb'))
    print(self.model)
    # Model has been selected
  
    def predict(self,input_parameters:list)->list:
       """
    Makes a prediction using the loaded model.
    
    Takes input parameters and passes it to the model , which was loaded using a pickle file.
    
    Args:
      input_parameters (list): The input data for making a prediction
    Returns:
      list: The prediction result from the model
    """
    
    logger.info('Making Prediction')
    return self.model.predict([input_parameters])
  
