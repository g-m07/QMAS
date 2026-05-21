import pandas as pd
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import scipy.stats as stats

df = pd.read_csv('mariokart.csv')

model = smf.ols('total_pr ~ cond + stock_photo + wheels', data=df).fit()
residuals = model.resid

stats.probplot(residuals, dist="norm", plot=plt)
plt.title('Normal Q-Q Plot of Residuals')
plt.tight_layout()
plt.show()

# Print the largest residuals to identify unusual observations
print("Largest residuals:")
print(residuals.abs().sort_values(ascending=False).head(5))