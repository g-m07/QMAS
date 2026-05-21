import pandas as pd
import statsmodels.formula.api as smf

df = pd.read_csv('mariokart.csv')

model = smf.ols('total_pr ~ wheels', data=df).fit()
print(f"R-squared: {model.rsquared:.4f}")
print(f"Adjusted R-squared: {model.rsquared_adj:.4f}")