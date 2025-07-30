from math import ceil
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not len(nums):
            return [-1, -1]

        left = 0
        right = len(nums) - 1
        mid = right // 2

        # Binary Search to find Occurance
        while left < right and nums[mid] != target:
            if nums[mid] < target:
                left = mid + 1
            elif target < nums[mid]:
                right = mid

            mid = (right + left) // 2

        if left == right:  # Not found or single occurance
            return [mid, mid] if nums[mid] == target else [-1, -1]

        found_left = found_right = mid

        mid = (left + found_left) // 2

        # Binary on left side
        while nums[left] != target:
            if nums[mid] == target:
                found_left = mid
            else:
                left = mid + 1
            mid = (left + found_left) // 2

        mid = (found_right + right) // 2

        while nums[right] != target:
            if nums[mid] == target:
                found_right = mid
            else:
                right = mid - 1

            mid = ceil((found_right + right) / 2)

        return [left, right]


soln = Solution()


def test_case_1():
    nums = [5, 7, 7, 8, 8, 10]
    target = 8

    assert soln.searchRange(nums, target) == [3, 4]


def test_case_2():
    nums = [5, 7, 7, 8, 8, 10]
    target = 6

    assert soln.searchRange(nums, target) == [-1, -1]


def test_empty_case():
    assert soln.searchRange([], 10) == [-1, -1]


def test_single_number():
    assert soln.searchRange([0, 1, 3], 1) == [1, 1]


def test_all_1_number():
    assert soln.searchRange([1, 1, 1, 1, 1, 1], 1) == [0, 5]
