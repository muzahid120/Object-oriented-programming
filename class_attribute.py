import os 
import pandas as pd
from sklearn.model_selection import train_test_split 


train=os.path.join("jahid",'train.csv')
test=os.path.join("jahid",'test.csv')
raw_data_path=os.path.join("jahid",'raw_data.csv')

test_data_dir=os.path.dirname(test)

os.makedirs(test_data_dir,exist_ok=True)


df=pd.read_csv(r'C:\Users\SDS\Downloads\stud.csv')

df.to_csv(raw_data_path,header=True,index=False)

train_data,test_data=train_test_split(df,test_size=0.2,random_state=42)
test_data.to_csv(test,header=True,index=False)
train_data.to_csv(train,header=True,index=False)


