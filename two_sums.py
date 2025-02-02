from typing import List, Optional
import unittest

def two_sums(nums: List[int], target: int) -> Optional[List[int]]:
    """
    Returns a list of the indexes of two items in the nums list that add up to equal the target.
    Assumes that there is only one pair

    :param nums: List of integers
    :param target: Target integer
    :return: List of two indices or an empty list if none is found
    """
    nums_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in nums_map:
            return [nums_map[complement], i]
        nums_map[num] = i

    return []

print(two_sums([1, 2, 3, 4], 5))


class TestTwoSums(unittest.TestCase):

    def test_basic_cases(self):
        self.assertEqual(two_sums([12, 3, 4, 6, 8], 10), [2, 3])  # 4 + 6 = 10
        self.assertEqual(two_sums([1, 7, 3, 4], 5), [0, 3])  # 1 + 4 = 5
        self.assertEqual(two_sums([5, 7, 3, 2], 8), [0, 2])  # 5 + 3 = 8

    def test_no_solution(self):
        self.assertListEqual(two_sums([1, 2, 3], 7), [])  # No pairs sum to 7
        self.assertListEqual(two_sums([], 0), [])  # Empty list

    def test_negative_numbers(self):
        self.assertEqual(two_sums([-1, -7, -3, -4], -5), [0, 3])  # -1 + -4 = -5
        self.assertEqual(two_sums([-1, -2, -5, -4], -6), [0, 2])  # -1 + -5 = -6

    def test_duplicates(self):
        self.assertEqual(two_sums([3, 3], 6), [0, 1])  # Both elements are the same


if __name__ == '__main__':
    unittest.main()