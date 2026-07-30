import pandas as pd


df = pd.read_excel("Stress_Dataset.xlsx")


age = pd.Series(df["Age"])

print("Original Age Series")
print(age)


filtered_age = age[age > 20]

print("\nFiltered Age Series (Age > 20)")
print(filtered_age)
print("mrunal Ghogare,S084")
