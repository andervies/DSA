from typing import List


def shuffle(nums: List[int], n: int) -> List[int]:
    n2 = []
    for i in range(n):
        n2.append(nums[i])
        n2.append(nums[n])
        n += 1

    return n2

shuffled_array = shuffle([1,2,3,4,5,6], 3)
print(shuffled_array)