import pandas as pd

#Load Dataset
df = pd.read_csv("Telco_Customer_Churn_Dataset.csv")

#Load 10 rows
print(df.head(10))

# Data types
print(df.dtypes)

# Missing values
print(df.isnull().sum())