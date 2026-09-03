import pandas as pd


df = pd.read_csv("D:\FYCS\python i data science\employee_salary.csv")


print("1. Number of Employees in Each Department:")
print(df.groupby("Department").size())


print("\n2. Average Salary for Each Department:")
print(df.groupby("Department")["Salary"].mean())


print("\n3. Maximum Salary for Each Department:")
print(df.groupby("Department")["Salary"].max())


print("\n4. Average Experience for Each Department:")
print(df.groupby("Department")["Experience"].mean())
