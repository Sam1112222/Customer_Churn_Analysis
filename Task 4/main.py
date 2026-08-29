import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('Telco_Customer_Churn_Dataset.csv')

# create tenure groups
bins = [0,12,36,100]
labels = ['0-12 Months', '12-36 Months', '36+ Months']
df['tenure_groups'] = pd.cut(df['tenure'], bins=bins, labels=labels)


#pie-chart for tenure groups
df['tenure_groups'].value_counts().plot.pie(autopct='%1.1f%%')
plt.title("Customer distribution based on tenure groups")
plt.show()

#bar-charts

avg_charges = df.groupby('tenure_groups')['MonthlyCharges'].mean()
avg_charges.plot(kind='bar',color = 'skyblue')
plt.title("Average Monthly Charges by Tenure Groups")
plt.xlabel("Tenure Groups")
plt.ylabel("Average Monthly Charges")
plt.show()