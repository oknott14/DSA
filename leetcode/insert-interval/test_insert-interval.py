from math import floor
from typing import List

class Solution:
  def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    soln: List[int] = []

    for [start, end] in intervals:
      if newInterval[1] < start:
        # no overlap [ni[0], ni[1], start, end] -> insert newInterval -> replace newInterval with curr
        soln.append((newInterval))
        newInterval = [start, end]
      elif end < newInterval[0]:
        # no overlap [start, end, ni[0], ni[1]] -> insert curr
        soln.append([start,end])
      elif newInterval[0] <= start and newInterval[1] <= end:
        # overlap [ni[0], start, ni[1], end] -> replace ni[1] with end
        newInterval[1] = end
      elif start <= newInterval[0] and end <= newInterval[1]:
        # overlap [start, ni[0], end, ni[1]] -> replace ni[0] with start
        newInterval[0] = start
      elif start <= newInterval[0] and newInterval[1] <= end:
        # overlap [start, ni[0], ni[1], end] -> replace newInterval with curr
        newInterval = [start, end]
      # else overlap[ni[0], start, end, ni[1]] -> do nothing

    if len(soln) == 0 or soln[len(soln)-1][1] < newInterval[0]:
      soln.append(newInterval)
    
    return soln
    
soln = Solution()

def compare_intervals(first: List[int], second: List[int]) -> bool:
   return first[0] == second[0] and first[1] == second[1]

def compare_lists(first: List[List[int]], second: List[List[int]]) -> bool:
  if (len(first) != len(second)):
    return False
  for index in range(len(first)):
    if (not compare_intervals(first[index], second[index])):
        return False
  return True

def test_inserts_new_without_merging_beginning():
  input = [[3,4]]
  newInterval = [1,2]
  output = [[1,2],[3,4]]
  
  assert compare_lists(output, soln.insert(input, newInterval))

def test_inserts_new_without_merging_middle():
  input = [[1,2],[5,6]]
  newInterval = [3,4]
  output = [[1,2],[3,4], [5,6]]
  
  assert compare_lists(output, soln.insert(input, newInterval))

def test_inserts_new_without_merging_end():
  input = [[1,2],[3,4]]
  newInterval = [5,6]
  output = [[1,2],[3,4], [5,6]]
  
  assert compare_lists(output, soln.insert(input, newInterval))

def test_inserts_new_with_merging_beginning():
  input = [[3,4],[5,6]]
  newInterval = [1,3]
  output = [[1,4], [5,6]]
  
  assert compare_lists(output, soln.insert(input, newInterval))

def test_inserts_new_with_merging_middle():
  input = [[1,2],[5,6]]
  newInterval = [2,4]
  output = [[1,4], [5,6]]
  
  assert compare_lists(output, soln.insert(input, newInterval))

def test_inserts_new_with_merging_end():
  input = [[1,2]]
  newInterval = [2,4]
  output = [[1,4]]
  
  assert compare_lists(output, soln.insert(input, newInterval))

def test_inserts_new_with_merging_multiple():
  input = [[1,2],[5,6]]
  newInterval = [2,5]
  output = [[1,6]]
  
  assert compare_lists(output, soln.insert(input, newInterval))

def test_inserts_new_with_merging_2_plus():
  input = [[1,2],[3,4],[5,6]]
  newInterval = [2,5]
  output = [[1,6]]
  
  assert compare_lists(output, soln.insert(input, newInterval))

def test_case_1():
  input = [[1,3],[6,9]]
  newInterval = [2,5]
  output = [[1,5],[6,9]]
  
  assert compare_lists(output, soln.insert(input, newInterval))

def test_case_2():
  input = [[1,2],[3,5],[6,7],[8,10],[12,16]]
  newInterval = [4,8]
  output = [[1,2],[3,10],[12,16]]

  assert compare_lists(output, soln.insert(input, newInterval))

def test_case_3():
  input = [[0,5],[8,9]]
  newInterval = [3,4]
  output = [[0,5],[8,9]]

  assert compare_lists(output, soln.insert(input, newInterval))
