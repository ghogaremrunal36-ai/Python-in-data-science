import pandas as pd


df = pd.read_excel("Stress_Dataset.xlsx")


print("Shape of Dataset:")
print(df.shape)


print("\nColumn Names:")
print(df.columns)


print("\nDataset Information:")
df.info()


print("\nStatistical Summary:")
print(df.describe())


print("\nMissing Values:")
print(df.isnull().sum())


print("\nUnique Values:")
print(df.nunique())
