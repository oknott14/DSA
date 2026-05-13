from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        if not len(nums):
            return [[]]

        next = self.subsets(nums[1:])
        results = [[nums[0]] for _ in range(len(next))]
        
        for idx in range(len(results)):
          results[idx].extend(next[idx])
        
        results.extend(next)

        return results


soln = Solution()


def test_case_1():
    assert soln.subsets([1, 2, 3]) == [
        [],
        [1],
        [2],
        [1, 2],
        [3],
        [1, 3],
        [2, 3],
        [1, 2, 3],
    ]


def test_case_2():
    assert soln.subsets([0]) == [[], [0]]
