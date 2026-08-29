import pandas as pd

#Load Dataset
df = pd.read_csv("Telco_Customer_Churn_Dataset.csv")

#remove duplicates
df = df.drop_duplicates()

# Fill missing values (example)
df = df.ffill()

# Standardize column names
df.columns = df.columns.str.lower().str.replace(" ", "_")

print(df.head())