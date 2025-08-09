from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return

        pivot = len(nums) - 2

        while 0 <= pivot and nums[pivot + 1] <= nums[pivot]:
            pivot -= 1

        swap = len(nums) - 1

        while pivot <= swap and nums[swap] <= nums[pivot]:
            swap -= 1

        nums[pivot], nums[swap] = nums[swap], nums[pivot]

        for i in range(pivot + 1, len(nums)):
            for j in range(pivot + 1, len(nums)):
                if nums[i] < nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]


soln = Solution()


def test_case_1():
    nums = [1, 2, 3]
    soln.nextPermutation(nums)
    assert nums == [1, 3, 2]


def test_case_2():
    nums = [3, 2, 1]
    soln.nextPermutation(nums)
    assert nums == [1, 2, 3]


def test_case_3():
    nums = [1, 1, 5]
    soln.nextPermutation(nums)
    assert nums == [1, 5, 1]


def test_case_2_3_1():
    nums = [2, 3, 1]
    soln.nextPermutation(nums)
    assert nums == [3, 1, 2]


def test_full_three_perm():
    nums = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1], [1, 2, 3]]

    for idx in range(len(nums) - 1):
        soln.nextPermutation(nums[idx])
        assert nums[idx] == nums[idx + 1]


def test_case_151():
    nums = [1, 5, 1]
    soln.nextPermutation(nums)
    assert nums == [5, 1, 1]
