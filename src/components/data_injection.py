import os
import sys
from src.exception import CustomException

import pandas as pd 
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.logger import logging
@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'data.csv')
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    def initiate_data_ingestion(self):
        logging.info("Data Ingestion method starts")
        try:
            df=pd.read_csv('notebook/data/student.csv')
            logging.info('Dataset read as pandas DataFrame')
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            logging.info('Raw data saved to artifacts/data.csv')
            logging.info('Train test split initiated')
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            logging.info('Train test split completed')
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            logging.info('Train data saved to artifacts/train.csv')
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info('Test data saved to artifacts/test.csv')
            logging.info("Data Ingestion method completed")
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
                self.ingestion_config.raw_data_path
            )
        except Exception as e:
            raise CustomException(e, sys)
if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()
    print("Data Ingestion completed successfully.")