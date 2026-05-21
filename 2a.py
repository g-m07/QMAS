import pandas as pd

df = pd.read_csv(r'C:\Users\User\Downloads\loan50.csv')

stats = {
    'Mean':               df['interest_rate'].mean(),
    'Median':             df['interest_rate'].median(),
    'Standard Deviation': df['interest_rate'].std(),
    'IQR':                df['interest_rate'].quantile(0.75) - df['interest_rate'].quantile(0.25)
}

summary = pd.DataFrame(stats, index=['interest_rate']).T.rename(columns={'interest_rate': 'Value'})
summary['Value'] = summary['Value'].round(2)
print(summary)