from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = nums[0]
        idx = 1

        while idx <= farthest < len(nums) - 1:
            farthest = max(idx + nums[idx], farthest)
            idx += 1

        return len(nums) - 1 <= farthest


soln = Solution()


def test_case_1():
    assert soln.canJump([2, 3, 1, 1, 4])


def test_case_2():
    assert not soln.canJump([3, 2, 1, 0, 4])

def test_case_3():
    assert soln.canJump([1,2,3])