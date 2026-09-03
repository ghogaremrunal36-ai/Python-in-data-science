import pandas as pd

df = pd.read_csv("E:\mrunal\python in data science\students (1).csv")


print("Name and Marks:")
print(df[["Name", "Marks"]])


print("\nStudents scoring more than 75:")
print(df[df["Marks"] > 75])


print("\nStudents with attendance above 80:")
print(df[df["Attendance"] > 80])


print("\nFemale Students:")
print(df[df["Gender"] == "Female"])


print("\nBSc CS Students:")
print(df[df["Course"] == "BSc CS"])


print("\nStudents satisfying both conditions:")
print(df[(df["Marks"] > 75) & (df["Attendance"] > 80)])
