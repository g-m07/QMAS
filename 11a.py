import pandas as pd
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt

df = pd.read_csv('mariokart.csv')

# Preferred model from Q10 (without duration)
model = smf.ols('total_pr ~ cond + stock_photo + wheels', data=df).fit()

residuals = model.resid
fitted = model.fittedvalues

plt.figure(figsize=(8, 5))
plt.scatter(fitted, residuals, alpha=0.6)
plt.axhline(0, color='red', linestyle='--')
plt.xlabel('Fitted Values')
plt.ylabel('Residuals')
plt.title('Residuals vs Fitted Values')
plt.tight_layout()
plt.show()