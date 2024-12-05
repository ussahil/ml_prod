from preparation import prepare_data
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
import pickle as pk
from config import settings
from loguru import logger


def build_model():
  logger.info('Starting Building Model')
  pass
  # Load preprocess Dataset
  df = prepare_data()
  # Identify X and y
  X,y = get_X_y(df)
  #  Split the dataset
  X_train, X_test, y_train, y_test = split_train_split(X,y)
  # Train the dataset
  rf = train_model(X_train,y_train)
  # Evaluate the dataset
  score = evaluate_model(rf,X_test,y_test)
  # print(score)
  # Fine tune
  # Save as pickle file
  save_model(rf)

def get_X_y(data):
  X = data[['area','constraction_year','bedrooms','garden','balcony_yes','parking_yes','furnished_yes','garage_yes','storage_yes']]
  y = data.rent
  
  logger.info(f"Defining X and y Variable")
  return X , y 

def split_train_split(X,y):
   logger.info("Train and test split ")
   X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
   return X_train, X_test, y_train, y_test
 
def train_model(X_train,y_train):
  logger.info("Training the model with hyper parameters")
  
  model = RandomForestRegressor()
  grid_space = {'n_estimators': [100, 200, 300], 'max_depth': [3, 6, 9, 12]}
  
  grid = GridSearchCV(RandomForestRegressor(), param_grid=grid_space, cv=5, scoring = 'r2')
  model_grid = grid.fit(X_train, y_train)

  
  return  model_grid.best_estimator_


def evaluate_model(model,X_test,y_test):
  logger.info(f'Evaluating model performance. Score ={model.score(X_test,y_test)}')
  return model.score(X_test,y_test)


def save_model(model):
  logger.info(f'Saving the model to dir {settings.model_dir}/{settings.model_file_name}')
  
  pk.dump(model, open(f'{settings.model_dir}/{settings.model_file_name}', 'wb'))

# Test
build_model()
