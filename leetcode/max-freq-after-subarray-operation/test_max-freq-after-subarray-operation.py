from collections import defaultdict
from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        first = defaultdict(int)
        last = defaultdict(int)
        freq = defaultdict(int)

        max_freq = 0
        # Prefix Sum of 1s in nums
        ps = [0] * len(nums)
        if nums[0] == k:
            ps[0] = 1

        first[nums[0]] = 0
        for idx in range(1, len(nums)):
            ps[idx] = ps[idx - 1]

            if nums[idx] == k:
                ps[idx] += 1
            elif nums[idx] not in first:
                first[nums[idx]] = idx

        for idx in range(len(nums)):
            val = nums[idx]

            if val == k:
                continue

            freq[val] += 1
            last[val] = idx

            k_between = ps[last[val]] - ps[first[val]]
            net_total = freq[val] - k_between

            if net_total <= 0:
                first[val] = idx
                freq[val] = 1

            max_freq = max(max_freq, net_total)

        return max_freq + ps[-1]


soln = Solution()


def test_case_1():
    nums = [1, 2, 3, 4, 5, 6]
    k = 1
    assert soln.maxFrequency(nums, k) == 2


def test_case_2():
    nums = [10, 2, 3, 4, 5, 5, 4, 3, 2, 2]
    k = 10
    assert soln.maxFrequency(nums, k) == 4


def test_k_is_most_common():
    nums = [1, 1, 1, 2, 1, 1, 1]
    k = 1
    assert soln.maxFrequency(nums, k) == len(nums)


def test_k_in_middle():
    assert soln.maxFrequency([2, 1, 2], 1) == 2


def test_many_ones_between():
    assert soln.maxFrequency([1, 2, 2, 4, 4, 1, 4, 1, 4], 1) == 5


def test_2_same():
    assert soln.maxFrequency([2, 2], 9) == 2


def test_case_739():
    nums = [10, 9, 2, 4, 6, 4, 2, 1, 2]
    k = 4
    assert soln.maxFrequency(nums, k) == 4


def test_all_k():
    assert soln.maxFrequency([1, 1, 1, 1, 1], 1) == 5
