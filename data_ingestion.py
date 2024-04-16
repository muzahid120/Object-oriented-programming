import os 
import pandas as pd 
from sklearn.model_selection import train_test_split

class DataConfig:
    row_data_path:str=os.path.join('artforts','row_data.csv')
    train_data_path:str= os.path.join('artforts','trian.csv')
    test_data_path:str=os.path.join('artforts','test.csv')

class Data_Ingestion:
    def __init__(self):
        self.ingestion_config=DataConfig()

    def initial_dataingestion(self):
        df=pd.read_csv(r'C:\Users\SDS\Downloads\stud.csv')
        os.makedirs(os.path.dirname(self.ingestion_config.row_data_path),exist_ok=True)
        df.to_csv(self.ingestion_config.row_data_path,header=True,index=False)

        train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

        train_set.to_csv(self.ingestion_config.train_data_path,header=True,index=False)
        test_set.to_csv(self.ingestion_config.test_data_path,header=True,index=False)


obj=Data_Ingestion()
obj.initial_dataingestion()