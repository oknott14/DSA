from tkinter import N
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
  def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    
    def invert_tree(node: Optional[TreeNode]) -> Optional[TreeNode]:
      if node is None:
        return None
      else:
        left = invert_tree(node.right)
        node.right = invert_tree(node.left)
        node.left = left
        return node

    return invert_tree(root)

  def build_tree(self, tree_arr: List[int | None], index: int) -> Optional[TreeNode]:
    if len(tree_arr) <= index or tree_arr[index] is None:
      return None
    else:
      return TreeNode(tree_arr[index], self.build_tree(tree_arr, 2 * index + 1), self.build_tree(tree_arr, 2 * index + 2))

  def tree_to_list(self, head: Optional[TreeNode], index: int, arr: List[int | None]) -> List[int | None]:
    if head is None:
      arr[index] = None
    else:
      arr[index] = head.val
      self.tree_to_list(head.left, 2 * index + 1, arr)
      self.tree_to_list(head.right, 2 * index + 2, arr)



  def run(self, tree_arr: List[int | None]) -> List[int | None]:
    head = self.build_tree(tree_arr, 0)
    inverted = self.invertTree(head)
    inv_list = [None] * len(tree_arr)
    self.tree_to_list(inverted, 0, inv_list)
    return inv_list
  
soln = Solution()

def test_case_1():
  input = [4,2,7,1,3,6,9]
  output = [4,7,2,9,6,3,1]
  assert soln.run(input) == output

def test_case_2():
  input = [2,1,3]
  output = [2,3,1]
  assert soln.run(input) == output