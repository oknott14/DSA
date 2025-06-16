from typing import List, Optional
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
class Solution:
  def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    queue: List[TreeNode] = []
    
    def insert_left(node: TreeNode):
      queue.insert(0, node)
      while node.left:
        node = node.left
        queue.insert(0, node)
      
    
    insert_left(root)

    while 0 < k:
      curr = queue.pop(0)
      k -= 1
      if curr.right is not None:
        insert_left(curr.right)
      
    return curr.val

  def build_tree(self, tree_arr: List[int | None], index: int = 0) -> Optional[TreeNode]:
    if len(tree_arr) <= index or tree_arr[index] is None:
      return None
    else:
      return TreeNode(tree_arr[index], self.build_tree(tree_arr, 2 * index + 1), self.build_tree(tree_arr, 2 * index + 2))
soln = Solution()

def test_case_1():
  input = soln.build_tree([3,1,4,None,2])
  k = 1
  output = 1
  assert soln.kthSmallest(input, k) == output

def test_case_2():
  input = soln.build_tree([5,3,6,2,4,None,None,1])
  k = 3
  output = 3
  assert soln.kthSmallest(input, k) == output


def test_case_3():
  input = soln.build_tree([5,None,8,None, None, 6, 10, None, None, None, None, None, 7, 9, 11])
  k = 7
  output = 11
  assert soln.kthSmallest(input, k) == output

def test_case_4():
  input = soln.build_tree([5,None,8,None, None, 6, 10, None, None, None, None, None, 7, 9, 11])
  k = 1
  output = 5
  assert soln.kthSmallest(input, k) == output