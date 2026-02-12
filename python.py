import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("python.csv")

print("Data:")
print(df)

print("\nAverage Sales:", df["Sales"].mean())
print("Max Sales:", df["Sales"].max())

sns.barplot(x="Month", y="Sales", data=df)
plt.title("Monthly Sales")
plt.show()