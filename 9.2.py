import pandas as pd


df = pd.read_csv("E:\mrunal\python in data science\students (1).csv")




print("Student Dataset:")
print(df)


print("\nFirst 10 Records:")
print(df.head(10))


print("\nNumber of Students:")
print(len(df))


print("\nColumn Names:")
print(df.columns)


print("\nAverage Marks:")
print(df["Marks"].mean())


print("\nAverage Attendance:")
print(df["Attendance"].mean())
