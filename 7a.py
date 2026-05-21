import pandas as pd
import numpy as np
import scipy.stats as stats

df = pd.read_csv('ncbirths.csv')

# Create binary premature variable: 1 if weeks < 37, else 0
df['premature'] = (df['weeks'] < 37).astype(int)

# Contingency table of habit vs premature
contingency = pd.crosstab(df['habit'], df['premature'])
contingency.columns = ['Not Premature (0)', 'Premature (1)']
print(contingency)

# Proportion of premature births in each group
prop_table = pd.crosstab(df['habit'], df['premature'], normalize='index')
prop_table.columns = ['Prop Not Premature', 'Prop Premature']
print(prop_table.round(4))