from typing import List


def get_concatenation(nums: List[int]) -> List[int]:
        nums += nums
        return nums

print(get_concatenation([1,2,3]))
