import pandas as pd


df = pd.read_excel("Stress_Dataset.xlsx")


data = dict(zip(df["Gender"], df["Age"]))


series = pd.Series(data)

print("Pandas Series from Dictionary")
print(series)
print("mrunal Ghogare, S084")
