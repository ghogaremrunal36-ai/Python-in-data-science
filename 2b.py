nested_tuple = (
("Python ", 310),
("Operating System", 345),
("Theory of computation", 333)
)

sorted_subjects = sorted(nested_tuple, key=lambda x: x[1])
print("Sorted Subjects (by subject code):", sorted_subjects)
