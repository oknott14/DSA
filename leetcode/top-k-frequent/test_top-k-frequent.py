import collections
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = sorted(
            collections.Counter(nums).items(), key=lambda x: x[1], reverse=True
        )
        return [x[0] for x in counts[:k]]


soln = Solution()


def equals(nums: List[int], output: List[int]) -> bool:
    if len(nums) != len(output):
        return False

    for num in nums:
        if not num in output:
            return False

    return True


def test_case_1():
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    output = [1, 2]
    assert equals(soln.topKFrequent(nums, k), output)


def test_case_2():
    nums = [1]
    k = 1
    output = [1]
    assert equals(soln.topKFrequent(nums, k), output)


def test_case_3():
    nums = [1, 1, 1, 2, 2, 3, 4, 4, 4, 3, 1]
    k = 3
    output = [1, 2, 4]
    assert equals(soln.topKFrequent(nums, k), output)


def test_case_4():
    nums = [3, 0, 1, 0]
    k = 1
    output = [0]
    assert equals(soln.topKFrequent(nums, k), output)


def test_case_5():
    nums = [3, 0, 1, 0, -1, -1, -1]
    k = 1
    output = [-1]
    assert equals(soln.topKFrequent(nums, k), output)
