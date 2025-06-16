from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
  def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    def traverse_orders(head: Optional[TreeNode], lst: List[List[int]] = [], level: int = 0) -> None:
      if head is None:
        return
      
      if level == len(lst):
        lst.append([])

      lst[level].append(head.val)
      level += 1
      traverse_orders(head.left, lst, level)
      traverse_orders(head.right, lst, level)
      
      return
    
    lst = []
    traverse_orders(root, lst)
    return lst


  def build_tree(self, tree_arr: List[int | None], index: int = 0) -> Optional[TreeNode]:
    if len(tree_arr) <= index or tree_arr[index] is None:
      return None
    else:
      return TreeNode(tree_arr[index], self.build_tree(tree_arr, 2 * index + 1), self.build_tree(tree_arr, 2 * index + 2))

soln = Solution()

def test_case_1():
  input = soln.build_tree([3,9,20,None,None,15,7])
  output = [[3], [9, 20], [15,7]]

  assert soln.levelOrder(input) == output

def test_case_2():
  input = soln.build_tree([3, 6, 10, 2, 4, 5, None, 1, 5, 7, None, 1, 2])
  output = [[3], [6,10], [2, 4, 5], [1, 5, 7, 1, 2]]

  assert soln.levelOrder(input) == output

def test_case_empty():
  input = soln.build_tree([])
  output = []

  assert soln.levelOrder(input) == output