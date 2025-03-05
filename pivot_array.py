from typing import List


def pivotArray(nums: List[int], pivot: int) -> List[int]:
    lesser = []
    greater = []
    equal = []

    for i in nums:
        if i < pivot:
            lesser.append(i)
        elif i > pivot:
            greater.append(i)

        else:
            equal.append(i)

    return lesser + equal + greater


nums = [9, 12, 5, 10, 14, 3, 10]
pivot = 10
print(pivotArray(nums, pivot))

