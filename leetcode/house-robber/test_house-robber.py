from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        if 2 < len(nums):
            nums[2] += nums[0]

            for idx in range(3, len(nums)):
                nums[idx] = max(nums[idx - 3] + nums[idx], nums[idx - 2] + nums[idx])

        return max(nums[-2], nums[-1])


soln = Solution()


def test_can_rob_one_house():
    nums = [1]
    output = 1
    assert soln.rob(nums) == output


def test_wont_rob_2_in_a_row():
    nums = [1, 1]
    output = 1
    assert soln.rob(nums) == output


def test_will_rob_spaced_by_1():
    nums = [2, 1, 1]
    output = 3
    assert soln.rob(nums) == output


def test_will_rob_spaced_by_n():
    nums = [2, 0, 0, 0, 1]
    output = 3
    assert soln.rob(nums) == output


def test_will_rob_many_spaced_by_1():
    nums = [1, 0, 1, 0, 1]
    output = 3
    assert soln.rob(nums) == output


def test_will_skip_2_houses():
    nums = [1, 0, 1, 4]
    output = 5
    assert soln.rob(nums) == output


def test_case_1():
    nums = [1, 2, 3, 1]
    output = 4

    assert soln.rob(nums) == output


def test_case_2():
    nums = [2, 7, 9, 3, 1]
    output = 12

    assert soln.rob(nums) == output
