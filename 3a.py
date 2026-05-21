import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r'C:\Users\User\Downloads\loan50.csv')

# Frequency table
freq = df['homeownership'].value_counts().reset_index()
freq.columns = ['Homeownership', 'Count']
freq['Proportion'] = (freq['Count'] / len(df)).round(3)
print(freq)

# Bar chart
sns.countplot(data=df, x='homeownership', order=['rent', 'mortgage', 'own'], color='steelblue')
plt.title('Distribution of Homeownership')
plt.xlabel('Homeownership Status')
plt.ylabel('Count')
plt.tight_layout()
plt.show()