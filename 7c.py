import pandas as pd
import numpy as np
import scipy.stats as stats

df = pd.read_csv('ncbirths.csv')

# Create premature variable needed for this question
df['premature'] = (df['weeks'] < 37).astype(int)

# Separate the two groups
smoker    = df[df['habit'] == 'smoker']['premature'].dropna()
nonsmoker = df[df['habit'] == 'nonsmoker']['premature'].dropna()

p1, n1 = smoker.mean(),    len(smoker)
p2, n2 = nonsmoker.mean(), len(nonsmoker)

# Standard error
se_diff = np.sqrt(p1*(1-p1)/n1 + p2*(1-p2)/n2)

# Two-proportion z-test (two-tailed, alpha = 0.05)
z_stat = (p1 - p2) / se_diff
p_val  = 2 * (1 - stats.norm.cdf(abs(z_stat)))

print(f"H0: p_smoker = p_nonsmoker  (no difference in prematurity rates)")
print(f"H1: p_smoker != p_nonsmoker  (two-tailed)")
print(f"z-statistic = {z_stat:.4f}")
print(f"p-value     = {p_val:.4f}")