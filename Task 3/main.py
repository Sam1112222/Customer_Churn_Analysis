import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load dataset
df = pd.read_csv("Telco_Customer_Churn_Dataset.csv")

# #Summary Status
print(df.describe())

# #Histogram
df['MonthlyCharges'].hist()
plt.title("Monthly Charges Distribution")
plt.show()

# #Box plots

plt.boxplot(df['MonthlyCharges'])
plt.title("Box Plot of MonthlyCharges")
plt.show()

# Churn count
sns.countplot(x='Churn', data=df)
plt.title("Churn Distribution")
plt.show()