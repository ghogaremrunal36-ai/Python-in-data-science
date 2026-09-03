import pandas as pd


df = pd.read_csv("E:\mrunal\python in data science\sales (1).csv")


print("1. Missing Values:")
print(df.isnull())


print("\n2. Count of Missing Values:")
print(df.isnull().sum())


average_price = df["Price"].mean()
df["Price"] = df["Price"].fillna(average_price)


average_sales = df["Sales"].mean()
df["Sales"] = df["Sales"].fillna(average_sales)


print("\n5. Cleaned Dataset:")
print(df)
print("Mrunal Ghogare, S084")
