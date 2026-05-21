import pandas as pd
import numpy as np
import scipy.stats as stats

df = pd.read_csv('ncbirths.csv')

# Create premature variable needed for this question
df['premature'] = (df['weeks'] < 37).astype(int)

# Separate the two groups
smoker    = df[df['habit'] == 'smoker']['premature'].dropna()
nonsmoker = df[df['habit'] == 'nonsmoker']['premature'].dropna()

p1, n1 = smoker.mean(),    len(smoker)     # smoker proportion and size
p2, n2 = nonsmoker.mean(), len(nonsmoker)  # nonsmoker proportion and size

# Standard error for difference in proportions
se_diff = np.sqrt(p1*(1-p1)/n1 + p2*(1-p2)/n2)

# Critical value for 95% CI
z_crit = stats.norm.ppf(0.975)

# Confidence interval
ci_low  = (p1 - p2) - z_crit * se_diff
ci_high = (p1 - p2) + z_crit * se_diff

print(f"p_smoker    = {p1:.4f}  (n={n1})")
print(f"p_nonsmoker = {p2:.4f}  (n={n2})")
print(f"Difference  = {p1-p2:.4f}")
print(f"SE          = {se_diff:.4f}")
print(f"95% CI      = ({ci_low:.4f}, {ci_high:.4f})")