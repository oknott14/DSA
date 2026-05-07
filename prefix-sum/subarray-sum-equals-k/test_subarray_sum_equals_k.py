from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        prefix_counts = {0: 1}
        found = 0
        for idx in range(len(nums)):
            prefix_sum += nums[idx]
            found += prefix_counts.get(prefix_sum - k, 0)
            prefix_counts[prefix_sum] = prefix_counts.get(prefix_sum, 0) + 1


        return found


soln = Solution()

def test_case_1():
    assert soln.subarraySum([1, 1, 1], 2) == 2

def test_case_2():
    assert soln.subarraySum([1, 2, 3], 3) == 2

def test_cast_3():

    assert soln.subarraySum([-1, -1, 1], 0) == 1
