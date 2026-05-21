import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("loan50.csv")

plt.figure(figsize=(8, 6))

sns.boxplot(
    data=df,
    x="homeownership",
    y="interest_rate",
    order=["mortgage", "own", "rent"],
    hue="homeownership",       # ← added
    legend=False,              # ← added
    palette="Set2"
)

plt.title("Distribution of Interest Rate by Homeownership Status", fontsize=14)
plt.xlabel("Homeownership Status", fontsize=12)
plt.ylabel("Interest Rate (%)", fontsize=12)
plt.tight_layout()
plt.show()

summary = df.groupby("homeownership")["interest_rate"].agg(
    count="count",
    mean="mean",
    median="median",
    std="std",
    q1=lambda x: x.quantile(0.25),
    q3=lambda x: x.quantile(0.75)
).round(2)

print(summary)