def find_smallest_index(arr):
    """Finds the index of the smallest element in an array.

    Args:
        arr (list): A list of integers.

    Returns:
        int: The index of the smallest element.
    """
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

# print(find_smallest_index([9,3,1,5,3]))

def selection_sort(arr):
    sorted_list = []

    for i in range(len(arr)):
        print(i)
        smallest_index = find_smallest_index(arr)
        sorted_list.append(arr.pop(smallest_index))

    return sorted_list

print(selection_sort([5, 3, 6, 2, 10]))