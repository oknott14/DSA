from typing import Callable, Optional, List, Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


MAX_INT = 2**31
MIN_INT = -MAX_INT - 1


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate_bst(node: Optional[TreeNode], left: int, right: int) -> bool:
            if node is None:
                return True

            return (
                left < node.val < right
                and validate_bst(node.left, left, node.val)
                and validate_bst(node.right, node.val, right)
            )

        return validate_bst(root, MIN_INT, MAX_INT)

    def build_tree(self, tree_arr: List[int | None], index: int) -> TreeNode | None:
        if len(tree_arr) <= index or tree_arr[index] is None:
            return None
        else:
            return TreeNode(
                tree_arr[index],
                self.build_tree(tree_arr, 2 * index + 1),
                self.build_tree(tree_arr, 2 * index + 2),
            )

    def run(self, tree_arr: List[int | None]) -> bool:
        head = self.build_tree(tree_arr, 0)
        return self.isValidBST(head)


soln = Solution()


def test_case_1():
    input = [2, 1, 3]
    assert soln.run(input)


def test_case_2():
    input = [5, 1, 4, None, None, 3, 6]
    assert not soln.run(input)


def test_case_3():
    input = [-2147483648]
    assert soln.run(input)
