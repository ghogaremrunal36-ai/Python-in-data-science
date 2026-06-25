
my_tuple = (10, 20, 30, 40, 50)
print("Original Tuple:", my_tuple)


print("First Element:", my_tuple[0])
print("Last Element:", my_tuple[-1])


print("Middle 3 Elements:", my_tuple[1:4])


tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concat_tuple = tuple1 + tuple2
print("Concatenated Tuple:", concat_tuple)


reversed_tuple = my_tuple[::-1]
print("Reversed Tuple:", reversed_tuple)


sample_tuple = (1, 2, 3, 2, 4, 2, 5)
count_element = sample_tuple.count(2)
print("Count of 2:", count_element)


index_element = sample_tuple.index(3)
print("Index of 3:", index_element)


element = 4
if element in sample_tuple:
    print(f"{element} exists in the tuple.")
else:
    print(f"{element} does not exist in the tuple.")


my_list = [100, 200, 300, 400]
converted_tuple = tuple(my_list)
print("Converted Tuple from List:", converted_tuple)


unsorted_tuple = (50, 10, 40, 20, 30)
sorted_tuple = tuple(sorted(unsorted_tuple))
print("Sorted Tuple:", sorted_tuple)


repeated_tuple = tuple1 * 3
print("Repeated Tuple:", repeated_tuple)


immutable_tuple = (1, 2, 3)

try:
    immutable_tuple[0] = 100  
except TypeError as e:
    print("Tuple is immutable. Error:", e)
