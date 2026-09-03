import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"D:\FYCS\python i data science\employee_salary.csv")

plt.figure(figsize=(10, 6))
plt.bar(df["Name"], df["Salary"])
plt.xlabel("Employee Name")
plt.ylabel("Salary")
plt.title("Employee Names and Salary")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(df["Name"], df["Salary"], marker="o")
plt.xlabel("Employee Name")
plt.ylabel("Salary")
plt.title("Employee Names and Salary")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 6))
plt.hist(df["Salary"], bins=5, edgecolor="black")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")
plt.title("Distribution of Employee Salary")
plt.tight_layout()
plt.show()

department_count = df["Department"].value_counts()

plt.figure(figsize=(8, 8))
plt.pie(
    department_count,
    labels=department_count.index,
    autopct="%1.1f%%"
)
plt.title("Number of Employees in Each Department")
plt.show()
