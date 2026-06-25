
numbers = [12, 45, 7, 89, 34]
largest = max(numbers)
print("Largest Number:", largest)


duplicate_list = [1, 2, 3, 2, 4, 5, 1, 6]
unique_list = list(set(duplicate_list))
print("List after removing duplicates:", unique_list)


num_list = [10, 15, 20, 25, 30, 35, 40]
even_count = 0
for num in num_list:
    if num % 2 == 0:
        even_count += 1
print("Number of even numbers:", even_count)


user_numbers = []
print("\nEnter 5 numbers:")
for i in range(5):
    n = int(input(f"Enter number {i+1}: "))
    user_numbers.append(n)

print("Entered List:", user_numbers)


def calculate_average(lst):
    return sum(lst) / len(lst)

average = calculate_average(user_numbers)
print("Average of entered numbers:", average)


text = "Python"
char_list = list(text)
print("List of Characters:", char_list)


words = ["Python", "is", "easy", "to", "learn"]
joined_string = " ".join(words)
print("Joined String:", joined_string)
