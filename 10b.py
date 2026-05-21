import pandas as pd
import statsmodels.formula.api as smf

df = pd.read_csv('mariokart.csv')

model_multi = smf.ols('total_pr ~ cond + stock_photo + duration + wheels', data=df).fit()

b_cond = model_multi.params['cond[T.used]']
b_wheels = model_multi.params['wheels']

print(f"Coefficient for cond (used vs new): {b_cond:.4f}")
print(f"Coefficient for wheels: {b_wheels:.4f}")