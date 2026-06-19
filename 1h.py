students = {
    "Mrunal": 85,
    "Shravani": 92,
    "Durva": 78,
    "Supriya": 88,
    "Kasturi": 95
}

for name, marks in students.items():
    print(name, ":", marks)

average = sum(students.values()) / len(students)

print("Class Average:", average)

top_student = max(students, key=students.get)

print("Highest Marks:")
print(top_student, "-", students[top_student])
