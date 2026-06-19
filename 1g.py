numbers = [12, 45, 7, 89, 23, 56, 90, 34, 18, 67]

print("List:", numbers)

print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Average:", sum(numbers) / len(numbers))

ascending = sorted(numbers)
descending = sorted(numbers, reverse=True)

print("Ascending Order:", ascending)
print("Descending Order:", descending)

numbers.append(100)
numbers.pop(0)

print("Updated List:", numbers)
