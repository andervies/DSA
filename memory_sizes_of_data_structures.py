import sys

# Create a tuple and a set with the same elements
tuple_example = ("(", "[", "{")
set_example = {"(", "[", "{"}

# Check their memory usage
print("Memory size of tuple:", sys.getsizeof(tuple_example))
print("Memory size of set:", sys.getsizeof(set_example))
