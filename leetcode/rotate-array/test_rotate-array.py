from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums) - 1
        for left, right in [(0, len(nums) - 1), (0, k - 1), (k, len(nums) - 1)]:
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1


soln = Solution()


def test_case_1():
    nums = [1, 2, 3, 4, 5, 6, 7]

    soln.rotate(nums, 3)
    assert nums == [5, 6, 7, 1, 2, 3, 4]


def test_case_2():
    nums = [-1, -100, 3, 99]
    soln.rotate(nums, 2)
    assert nums == [3, 99, -1, -100]


def test_case_3():
    nums = [1, 2, 3, 4, 5, 6, 7]
    soln.rotate(nums, 1)
    assert nums == [7, 1, 2, 3, 4, 5, 6]


def test_k_is_0():
    nums = [1, 2, 3, 4, 5, 6, 7]
    soln.rotate(nums, 0)
    assert nums == [1, 2, 3, 4, 5, 6, 7]
