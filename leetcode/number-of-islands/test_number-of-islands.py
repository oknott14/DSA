from typing import List
class Solution:
  def numIslands(self, grid: List[List[str]]) -> int:
    m = len(grid)
    n = len(grid[0])
    islands = 0

    def dfs(i, j):
      if i < 0 or m <= i or j < 0 or n <= j or grid[i][j] == '0':
        return
      
      grid[i][j] = '0'

      for row, col in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        dfs(i + row, j + col)
      
    for i in range(m):
      for j in range(n):

        if grid[i][j] == '1':
          dfs(i, j)
          islands += 1

    return islands

    



soln = Solution()

def test_case_1():
  grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
  ]
  output = 1

  assert soln.numIslands(grid) == output
  
def test_case_2():
  grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
  ]
  output = 3
  assert soln.numIslands(grid) == output

def test_case_3():
  grid = [
    ["1"]
  ]
  output = 1
  assert soln.numIslands(grid) == output

def test_case_4():
  grid = [
    ["1","1","0","1","1"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["1","1","0","1","1"]
  ]
  output = 5
  assert soln.numIslands(grid) == output


def test_case_5():
  grid = [
    ["0","0","0","0","0"],
    ["0","0","0","0","0"],
    ["0","0","0","0","0"],
    ["0","0","0","0","0"]
  ]
  output = 0
  assert soln.numIslands(grid) == output