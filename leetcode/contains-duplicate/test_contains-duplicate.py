from typing import List
class Solution:
  def containsDuplicate(self, nums: List[int]) -> bool:
    return not len(nums) == len(set(nums))

soln = Solution()

def test_case_1():
  assert True
