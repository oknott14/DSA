from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
  def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    
    def compare_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

      if p is None or q is None:
        return p is None and q is None
      else:
        return p.val == q.val and compare_tree(p.left, q.left) and compare_tree(p.right, q.right)

    return compare_tree(p, q)

  def build_tree(self, tree_arr: List[int | None], index: int) -> Optional[TreeNode]:
    if len(tree_arr) <= index or tree_arr[index] is None:
      return None
    else:
      return TreeNode(tree_arr[index], self.build_tree(tree_arr, 2 * index + 1), self.build_tree(tree_arr, 2 * index + 2))

  def run(self, tree_arr1: List[int | None], tree_arr2: List[int | None]) -> bool:
    head1 = self.build_tree(tree_arr1, 0)
    head2 = self.build_tree(tree_arr2, 0)

    return self.isSameTree(head1, head2)
  
soln = Solution()

def test_case_1():
  p = [1,2,3]
  q = [1,2,3]
  assert soln.run(p, q)

def test_case_2():
  p = [1,2,1]
  q = [1,1,2]
  assert not soln.run(p, q)