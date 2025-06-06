import collections
from typing import List
class Solution:
  def exist(self, board: List[List[str]], word: str) -> bool:
    m = len(board)
    n = len(board[0])
    visited = set([])
    hsh = lambda x,y: (n * x) + y
    def dfs(row: int, col: int, i: int):
      
      if hsh(row, col) in visited or row < 0 or m <= row or col < 0 or n <= col or board[row][col] != word[i]:
        return False
      elif i == len(word) - 1:
        return True
      
      visited.add((n * row) + col)
      
      for d_row, d_col in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        n_row, n_col = row + d_row, col + d_col
        if dfs(n_row, n_col, i + 1):
          return True
        
      visited.remove((n * row) + col)
      return False
    
    w_count = collections.Counter(word)
    b_count = collections.Counter()
    return any(dfs(r, c, 0) for r in range(m) for c in range(n))
  
soln = Solution()

def test_case_1():
  board = [
    ["A","B","C","E"],
    ["S","F","C","S"],
    ["A","D","E","E"]
  ]
  word = "ABCCED"
  assert soln.exist(board, word)

def test_case_2():
  board = [
    ["A","B","C","E"],
    ["S","F","C","S"],
    ["A","D","E","E"]
  ]
  word = "SEE"
  assert soln.exist(board, word)

def test_case_2_5():
  board = [
    ["A","B","C","E"],
    ["S","F","C","S"],
    ["A","D","E","E"]
  ]
  word = "ABCB"
  assert not soln.exist(board, word)

def test_case_3():
  board = [['a','b','c','d','e']]  
  word = "abcde"
  assert soln.exist(board, word)

def test_case_3():
  board = [[]]  
  word = "a"
  assert not soln.exist(board, word)

def test_case_4():
  board = [["a","a","a","a"],["a","a","a","a"],["a","a","a","a"]]
  word = 'aaaaaaaaaaaaa'
  assert not soln.exist(board, word)

def test_case_5():
  board = [["a","b"],["c","d"]]
  word = 'acdb'
  assert soln.exist(board, word)

def test_case_6():
  board = [
    ["C","A","A"],
    ["A","A","A"],
    ["B","C","D"]
  ]
  word = 'AAB'
  assert soln.exist(board, word)

def test_case_7():
  board = [
    ["a","a"],
    ["a","a"],
    ["A","A"]
  ]
  word = 'aaaAAa'
  assert soln.exist(board, word)