from typing import List
class Solution:
  def rob(self, nums: List[int]) -> int:
    if len(nums) < 2:
      return nums[0]
  
    tracker = [nums[0], 0]
    curr = nums[:2].copy()

    for idx in range(2, len(nums)):
      
      for i in [0, 1]:
        tmp = tracker[i]
        tracker[i] = curr[i]
        curr[i] = max(nums[idx] + tmp, tracker[i])
    
    return max(tracker[0], curr[1])

soln = Solution()

def test_case_1():
  input = [2,3,2]
  output = 3
  assert soln.rob(input) == output

def test_case_2():
  input = [1,2,3,1]
  output = 4
  assert soln.rob(input) == output

def test_case_3():
  input = [2,3,2,0,0,1,2,5,4]
  output = 10
  assert soln.rob(input) == output

def test_case_4():
  input = [2,3,4,0,1,8,1,4]
  output = 16
  assert soln.rob(input) == output

def test_case_5():
  input = [2,3,4,0,1,8,0,0]
  output = 14
  assert soln.rob(input) == output

def test_single_house():
  input = [1]
  output = 1
  assert soln.rob(input) == output

def test_2_houses():
  input = [1,2]
  output = 2
  assert soln.rob(input) == output