import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('Telco_Customer_Churn_Dataset.csv')
#tenure-groups
bins = [0,12,36,100]
labels = ['0-12 Months', '12-36 Months', '36+ Months']
df['tenure_groups'] = pd.cut(df['tenure'], bins=bins, labels=labels)

#churn by gender
print(pd.crosstab(df['gender'],df['Churn'],normalize='index'))

#churn by contract
print(pd.crosstab(df['Contract'],df['Churn'],normalize='index'))

#churn by payment method
print(pd.crosstab(df['PaymentMethod'],df['Churn'],normalize='index'))


#countplot by contact types
sns.countplot(x='tenure_groups', hue='Churn', data=df)
plt.title("Churn by Contact types")
plt.show()

#countplot by contract types
sns.countplot(x='tenure_groups', hue='Churn', data=df)
plt.title("Churn by Contract types")
plt.show()