import pandas as pd
import statsmodels.formula.api as smf

df = pd.read_csv('mariokart.csv')

# Full model
m_full = smf.ols('total_pr ~ cond + stock_photo + duration + wheels', data=df).fit()

# Model without duration (test if it can be dropped)
m_no_duration = smf.ols('total_pr ~ cond + stock_photo + wheels', data=df).fit()

# Model without stock_photo
m_no_stock = smf.ols('total_pr ~ cond + duration + wheels', data=df).fit()

# Model with only cond and wheels (most parsimonious)
m_minimal = smf.ols('total_pr ~ cond + wheels', data=df).fit()

print("Model Comparison (Adjusted R²):")
print(f"  Full model (all 4 predictors):          Adj R² = {m_full.rsquared_adj:.4f}")
print(f"  Without duration:                        Adj R² = {m_no_duration.rsquared_adj:.4f}")
print(f"  Without stock_photo:                     Adj R² = {m_no_stock.rsquared_adj:.4f}")
print(f"  Minimal (cond + wheels only):            Adj R² = {m_minimal.rsquared_adj:.4f}")

print("\nFull model p-values:")
print(m_full.pvalues)