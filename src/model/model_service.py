
# 1. Pick up model
  # 1.1 if config file does  exist then load the trained model
  # 1.2 if config does not exist -> train model to get it
  # 2. Make Prediction
from model.pipeline.model import build_model
from pathlib import Path
import pickle as pk
from config.config import settings
from loguru import logger

class ModalService:
  def __init__(self):
    self.model = None
  def load_model(self):
    logger.info(f"Checking the existence of model config at {settings.model_dir}/{settings.model_file_name}")
    
    model_path = Path(f"{settings.model_dir}/{settings.model_file_name}")
    
    
    if not model_path.exists():
      logger.warning("Model at {settings.model_dir}/{settings.model_file_name} was not found -> Building {settings.model_file_name}")
      
      
      build_model()
    
    logger.info(f"Model exists config file loading")
    
    self.model = pk.load(open(f'{settings.model_dir}/{settings.model_file_name}','rb'))
    print(self.model)
    # Model has been selected
  
  def predict(self,input_parameters):
    logger.info('Making Prediction')
    return self.model.predict([input_parameters])
    
