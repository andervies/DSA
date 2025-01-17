def linear_search(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1

# Example
array = [10, 20, 30, 40, 50]
target_value = 30
result = linear_search(array, target_value)

if result != -1:
    print(f"Target found at index: {result}")
else:
    print("Target not found.")
