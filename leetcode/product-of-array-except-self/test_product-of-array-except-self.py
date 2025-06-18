# SIMPLE SOLN O(n) (2 passes)
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         ans = [1] * n

#         prod = 1
#         for i in range(n):
#             ans[i] = prod
#             prod *= nums[i]

#         prod = 1
#         for i in reversed(range(n)):
#             ans[i] *= prod
#             prod *= nums[i]

#         return ans

# O(n) But slow
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         size = len(nums)
#         mid = floor(len(nums) / 2)
#         ans = nums.copy()
#         l_inc = nums[0]
#         l_dec = nums[-1]

#         for idx in range(1, mid):
#             l_inc *= ans[idx]
#             l_dec *= ans[size - idx - 1]
#             ans[idx] = l_inc
#             ans[size - idx - 1] = l_dec

#         if size % 2:
#             ans[mid] = l_inc * l_dec
#             l_inc *= nums[mid]
#             l_dec *= nums[mid]

#         for idx in range(mid + size % 2, size - 1):
#             ans[idx] = ans[idx + 1] * l_inc
#             l_inc *= nums[idx]

#             ans[size - idx - 1] = ans[size - idx - 2] * l_dec
#             l_dec *= nums[size - idx - 1]

#         ans[0] = l_dec
#         ans[-1] = l_inc
#         return ans
from typing import List

# Fastest Soln O(n) 1 to 2 passes
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = 0
        prod = 1

        for num in nums:
            if num == 0:
                zeros += 1
            else:
                prod *= num

        ans = [0] * len(nums)

        if zeros == 1:
            ans[nums.index(0)] = prod
        elif zeros == 0:
            for idx in range(len(nums)):
                ans[idx] = prod // nums[idx]

        return ans


soln = Solution()


def test_base_case():
    nums = [1, 2]
    ans = [2, 1]
    assert soln.productExceptSelf(nums) == ans


def test_odd_length():
    nums = [1, 2, 3, 4, -3, -2, -1]
    ans = [-144, -72, -48, -36, 48, 72, 144]
    assert soln.productExceptSelf(nums) == ans


def test_no_div_by_zero():
    nums = [2, 3, 5, 0]
    ans = [0, 0, 0, 30]
    assert soln.productExceptSelf(nums) == ans


def test_case_1():
    nums = [1, 2, 3, 4]
    ans = [24, 12, 8, 6]
    assert soln.productExceptSelf(nums) == ans


def test_case_2():
    nums = [-1, 1, 0, -3, 3]
    ans = [0, 0, 9, 0, 0]
    assert soln.productExceptSelf(nums) == ans
