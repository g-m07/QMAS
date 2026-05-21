import pandas as pd
import statsmodels.formula.api as smf

df = pd.read_csv('mariokart.csv')

# Fit multiple regression model
model_multi = smf.ols('total_pr ~ cond + stock_photo + duration + wheels', data=df).fit()
print(model_multi.summary())
print(f"\nCoefficients:\n{model_multi.params}")