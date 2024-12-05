from model.model_service import ModalService
from loguru import logger

@logger.catch
def main():
  # Test
  ml_svc = ModalService()
  ml_svc.load_model()

# Check
  pred = ml_svc.predict([85, 2015, 2, 20, 1, 1, 0, 0, 1])
  logger.info(f"Prediction is {pred}")
  
if __name__ =='__main__':
  main()