from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        calculated = {0: 1}
        subs = 0
        total = 0

        for num in nums:
            total += num

            if total - k in calculated:
                subs += calculated[total - k]

            calculated[total] = 1 + calculated.get(total, 0)

        return subs


soln = Solution()


def test_case_1():
    nums = [1, 1, 1]
    assert soln.subarraySum(nums, 2) == 2


def test_case_2():
    nums = [1, 2, 3]
    assert soln.subarraySum(nums, 3) == 2


def test_counts_self_n_times():
    nums = [2, 2, 2, 2]
    assert soln.subarraySum(nums, 2) == 4


def test_counts_self_and_0():
    nums = [0, 2, 0]
    assert soln.subarraySum(nums, 2) == 4


def test_counts_negative_correctionI():
    nums = [1, 2, 3, -4, 1, 3, 2]
    assert soln.subarraySum(nums, 2) == 5


def test_case_11():
    nums = [-1, -1, 1]
    assert soln.subarraySum(nums, 0) == 1
