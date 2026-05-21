import pandas as pd
import numpy as np
import scipy.stats as stats

df = pd.read_csv('ncbirths.csv')

# Separate weight by habit group
smoker_w    = df[df['habit'] == 'smoker']['weight'].dropna()
nonsmoker_w = df[df['habit'] == 'nonsmoker']['weight'].dropna()

# Welch's two-sample t-test (does not assume equal variances)
t_stat, p_val_t = stats.ttest_ind(smoker_w, nonsmoker_w, equal_var=False)

# Welch-Satterthwaite degrees of freedom
s1, s2 = smoker_w.var(), nonsmoker_w.var()
m1, m2 = len(smoker_w), len(nonsmoker_w)
df_welch = (s1/m1 + s2/m2)**2 / ((s1/m1)**2/(m1-1) + (s2/m2)**2/(m2-1))

print(f"H0: mu_smoker = mu_nonsmoker  (no difference in mean birth weight)")
print(f"H1: mu_smoker != mu_nonsmoker  (two-tailed)")
print(f"t-statistic        = {t_stat:.4f}")
print(f"Degrees of freedom = {df_welch:.1f}")
print(f"p-value            = {p_val_t:.4f}")