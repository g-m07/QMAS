import pandas as pd
import statsmodels.formula.api as smf

df = pd.read_csv('mariokart.csv')

model = smf.ols('total_pr ~ wheels', data=df).fit()
print(model.summary())
print(f"\nIntercept: {model.params['Intercept']:.4f}")
print(f"Slope (wheels): {model.params['wheels']:.4f}")