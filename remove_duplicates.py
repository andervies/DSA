import unittest


def remove_duplicates(nums):
    if not nums:
        return 0
    k = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            nums[k] = nums[i]
            k += 1

    return k


class TestRemoveDuplicates(unittest.TestCase):

    def test_basic_cases(self):
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        expected_nums = [0, 1, 2, 3, 4]

        k = remove_duplicates(nums)

        self.assertEqual(k, len(expected_nums))

        for i in range(k):
            self.assertEqual(expected_nums[i], nums[i])

    def test_edge_case_empty(self):
        nums = []
        expected_nums = []

        k = remove_duplicates(nums)

        self.assertEqual(k, len(expected_nums))

    def test_no_duplicates(self):
        nums = [1, 2, 3, 4]
        expected_nums = [1, 2, 3, 4]

        k = remove_duplicates(nums)

        self.assertEqual(k, len(expected_nums))

        for i in range(k):
            self.assertEqual(expected_nums[i], nums[i])

    def test_all_duplicates(self):
        nums = [2, 2, 2, 2]
        expected_nums = [2]

        k = remove_duplicates(nums)

        self.assertEqual(k, len(expected_nums))

        for i in range(k):
            self.assertEqual(expected_nums[i], nums[i])



if __name__ == "__main__":
    unittest.main()