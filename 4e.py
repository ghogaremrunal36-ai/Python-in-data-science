import numpy as np

arr = np.array([10, 50, 30, 50, 20])


max_value = np.max(arr)


filter_arr = arr == max_value


result = arr[filter_arr]

print("Original Array:", arr)
print("Maximum Value:", max_value)
print("Filter Array:", filter_arr)
print("Filtered Maximum Value(s):", result)


print("Mrunal Ghogare, F084")
