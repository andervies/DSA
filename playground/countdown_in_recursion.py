def countdown(i):
    """
    Recursively prints a countdown of integers starting from the given number.

    Args:
        i (int): The starting point of the countdown. Should be a non-negative integer.

    Returns:
        None

    Notes:
        This function uses recursion and may cause a stack overflow for very large inputs.
    """
    print(i)

    if i == 0:

        return
    else:
        countdown(i-1)

    # print("here " + str(i))

countdown(3)


