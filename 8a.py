import pandas as pd
import numpy as np
import scipy.stats as stats

df = pd.read_csv('ncbirths.csv')

# Mean and standard deviation of birth weight by habit group
summary = df.groupby('habit')['weight'].agg(
    n    = 'count',
    Mean = 'mean',
    SD   = 'std'
).round(4)

print(summary)