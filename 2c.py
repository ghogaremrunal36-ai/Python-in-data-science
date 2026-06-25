original_list = ["TOC", "PYTHON", "Scala", "OS"]

copy1 = original_list[:]

copy2 = list(original_list)

copy3 = original_list.copy()

print("Original List:", original_list)
print("Copy using slicing:", copy1)
print("Copy using list():", copy2)
print("Copy using copy():", copy3)
