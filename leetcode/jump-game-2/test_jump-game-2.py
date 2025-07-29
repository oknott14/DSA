from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        # Pointer Soln beats 50% -> 9ms
        N = len(nums)

        if N <= 1:
            return 0

        farthest = 0
        end = 0
        jumps = 0

        for idx in range(N):
            farthest = max(farthest, idx + nums[idx])

            if N - 1 <= farthest:
                return jumps + 1

            if idx == end:
                end = farthest
                jumps += 1

        return jumps
        # DP Soln Beats 26% 322ms
        # if len(nums) == 1:
        #     return 0

        # dp = [0] * len(nums)

        # for idx in range(len(nums) - 2, -1, -1):
        #     if nums[idx] == 0:
        #         dp[idx] = len(nums) + 1
        #     else:
        #         search = dp[idx + 1 : min(len(nums), idx + 1 + nums[idx])]
        #         dp[idx] = 1 + min(search)

        # return dp[0]


soln = Solution()


def test_case_1():
    nums = [2, 3, 1, 1, 4]
    assert soln.jump(nums) == 2


def test_case_2():
    nums = [2, 3, 0, 1, 4]
    assert soln.jump(nums) == 2


def test_single_length():
    nums = [0]
    assert soln.jump(nums) == 0


def test_single_jump():
    nums = [1, 0]
    assert soln.jump(nums) == 1


def test_best_reaches_after():
    nums = [2, 4, 5, 0, 0, 2, 0, 1]
    assert soln.jump(nums) == 2


def test_worst_case():
    nums = [1, 1, 1, 1]
    assert soln.jump(nums) == 3


def test_case_61():
    nums = [2, 1, 1, 1, 1]
    assert soln.jump(nums) == 3
