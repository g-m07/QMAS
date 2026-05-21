import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('mariokart.csv')

plt.figure(figsize=(8, 5))
sns.stripplot(data=df, x='wheels', y='total_pr', jitter=True, alpha=0.6)
plt.xlabel('Number of Wii Wheels')
plt.ylabel('Final Auction Price (USD)')
plt.title('Scatterplot of Wheels vs Total Price (with jitter)')
plt.tight_layout()
plt.show()