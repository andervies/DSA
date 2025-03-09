import sys

# Create different data structures with the same elements
tuple_example = ("(", "[", "{")
set_example = {"(", "[", "{"}
array_example = ["(", "[", "{"]

# Check their memory usage
print("Memory size of tuple:", sys.getsizeof(tuple_example))
print("Memory size of set:", sys.getsizeof(set_example))
print("Memory size of array/list:", sys.getsizeof(array_example))