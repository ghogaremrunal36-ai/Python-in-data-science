even = 0

for i in range(1, 6):
    n = int(input(f"Enter number {i}: "))

    if n % 2 == 0:
        even += 1

print("Even numbers =", even)
