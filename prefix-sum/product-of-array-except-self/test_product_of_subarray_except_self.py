from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)

        if N <= 1:
            return [0]

        prefix_prod_left = [1] * len(nums)
        prefix_prof_right = [1] * len(nums)
        prefix_prod_left[0] = nums[0]
        prefix_prof_right[-1] = nums[-1]
        for idx in range(1, len(nums)):
            prefix_prod_left[idx] = prefix_prod_left[idx - 1] * nums[idx]
            prefix_prof_right[N - 1 - idx] = (
                prefix_prof_right[N - idx] * nums[N - 1 - idx]
            )

        prods = [0] * len(nums)
        prods[0] = prefix_prof_right[1]
        prods[-1] = prefix_prod_left[N - 2]
        for idx in range(1, len(nums) - 1):
            prods[idx] = prefix_prod_left[idx - 1] * prefix_prof_right[idx + 1]
        return prods


soln = Solution()


def test_case_1():
    assert soln.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]


def test_case_2():
    assert soln.productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
