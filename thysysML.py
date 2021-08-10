import pandas as pd
from chefboost import Chefboost as cb
from sklearn.model_selection import train_test_split

# Using the pandas library, we read the .CSV file
df2 = pd.read_csv('Thyroid-Dataset.csv')

# Dropping unnecessary columns
df2 = df2.drop(['T3', 'T4', 'TSH'], axis=1)

#Checking for null rows
df2.where(df2.isnull() == True).count()

#Checking for duplicated rows
df2.duplicated().sum() #Output: 358
df2.loc[df2.duplicated(), :]

df2_double = df2 # With the duplicated rows

#Removing the duplicated rows
df2 = df2.drop_duplicates()

classes2 = df2['class'].unique()
#SO apparently to create the CHAID, i need the raw data as tables, not as an array
X = df2 #X just copies the table of df2
#Splitting the table into 70-30
X_train, X_test = train_test_split(X, test_size=0.3, random_state=42)
Y_train = X_train
Y_test = X_test

chaidModel = cb.load_model(file_name="chaidModel.pkl")
chaidModel

cb.evaluate(chaidModel,X_test,target_label="class",task='test')