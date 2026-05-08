from sys import prefix
from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix_set = {0: -1}
        max_len = 0
        count = 0
        for idx in range(len(nums)):
            count += -1 if nums[idx] == 0 else 1
            
            if count in prefix_set:

                max_len = max(max_len, idx - prefix_set[count])

            else:

                prefix_set[count] = idx

        return max_len


soln = Solution()


def test_case_1():
    assert soln.findMaxLength([0, 1]) == 2

def test_case_2():
    assert soln.findMaxLength([0, 1, 0]) == 2

def test_case_3():
    assert soln.findMaxLength([0, 0, 1, 0, 0, 0, 1, 1]) == 6