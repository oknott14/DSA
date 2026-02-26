from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        while nums[0] != nums[nums[0]]:
            temp = nums[0]
            nums[0] = nums[temp]
            nums[temp] = temp

        return nums[0]


soln = Solution()


def test_case_1():
    nums = [1, 3, 4, 2, 2]
    assert soln.findDuplicate(nums) == 2


# 1
def test_case_2():
    nums = [3, 1, 3, 4, 2]
    assert soln.findDuplicate(nums) == 3


def test_case_all_1_num():
    nums = [3, 3, 3, 3, 3]
    assert soln.findDuplicate(nums) == 3
