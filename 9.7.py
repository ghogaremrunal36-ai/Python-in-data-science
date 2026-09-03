import pandas as pd


df = pd.read_csv("E:\mrunal\python in data science\student_performance (2).csv")


df["Marks"] = df[["English", "Mathematics", "Computer"]].mean(axis=1)


print("1. Average Marks:")
print(df["Marks"].mean())


print("\n2. Maximum Marks:")
print(df["Marks"].max())


print("\n3. Minimum Marks:")
print(df["Marks"].min())


print("\n4. Median Marks:")
print(df["Marks"].median())


print("\n5. Standard Deviation of Marks:")
print(df["Marks"].std())


print("\n6. Average Attendance:")
print(df["Attendance"].mean())


print("\n7. Number of Students:")
print(len(df))


print("\n8. Students who scored more than 75:")
print((df["Marks"] > 75).sum())
print("Mrunal Ghogare,S084")
