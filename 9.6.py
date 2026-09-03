import pandas as pd


df = pd.read_csv("E:\mrunal\python in data science\employee_salary.csv")


df["Result"] = df["Salary"].apply(
    lambda x: "High Salary" if x >= 50000 else "Low Salary"
)


def calculate_grade(salary):
    if salary >= 70000:
        return "A+"
    elif salary >= 60000:
        return "A"
    elif salary >= 50000:
        return "B"
    elif salary >= 40000:
        return "C"
    elif salary >= 30000:
        return "D"
    else:
        return "F"

df["Grade"] = df["Salary"].apply(calculate_grade)


print("Employee Dataset with Result and Grade:")
print(df)
print("mrunal ghogare, s084")
