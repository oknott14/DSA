from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pass


soln = Solution()


def test_case_1():
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    output = [3, 9, 20, None, None, 15, 7]


def test_case_single_node():
    preorder = [-1]
    inorder = [-1]
    output = [-1]
