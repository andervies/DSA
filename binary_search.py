def binary_search(arr, element):
    """
    Searches for an element in a sorted array using binary search.

    Args:
        arr (list): A sorted list of integers.
        element (int): The integer to search for in the array.

    Returns:
        int or None: The index of the element if found; None if it does not exist in the array.

    Raises:
        ValueError: If the input array is not sorted.
    """

    ## Raise valueError if array is not sorted

    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        guess = arr[mid]
        if guess == element:
            return mid
        elif guess > element:
            high = mid - 1
        else:
            low = mid + 1

    return None

print(binary_search([1,2,3,4,5,6,7,8,9,10], 10))