from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        N = len(nums) - 1
        jumps = 0
        farthest = 0
        jump_end = 0

        for idx in range(N):
            
            farthest = max(farthest, nums[idx] + idx)

            if idx == jump_end:
                
                jumps += 1
                jump_end = farthest

        return jumps

soln = Solution()


def test_case_1():

    assert soln.jump([2, 3, 1, 1, 4]) == 2


def test_case_2():
    assert soln.jump([2, 3, 0, 1, 4]) == 2

def test_1_short_many_long():
    
    assert soln.jump([3,5,1,1,4,1,1,1,1]) == 3