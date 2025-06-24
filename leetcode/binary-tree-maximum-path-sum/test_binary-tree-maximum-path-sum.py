from typing import List, Optional, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def calculate_sum(node: Optional[TreeNode]) -> Tuple[int, int]:
            if node is None:
                return (-1001, -1001)

            left_max, left_sum = calculate_sum(node.left)
            right_max, right_sum = calculate_sum(node.right)

            return (
                max(
                    node.val,
                    left_sum + right_sum + node.val,
                    left_max,
                    right_max,
                    left_sum,
                    right_sum,
                ),
                max(node.val, left_sum + node.val, right_sum + node.val),
            )

        return max(calculate_sum(root))

    def build_tree(
        self, tree_arr: List[int | None], index: int = 0
    ) -> Optional[TreeNode]:
        if len(tree_arr) <= index or tree_arr[index] is None:
            return None
        else:
            return TreeNode(
                tree_arr[index],
                self.build_tree(tree_arr, 2 * index + 1),
                self.build_tree(tree_arr, 2 * index + 2),
            )


soln = Solution()


def test_case_1():
    root = soln.build_tree([1, 2, 3])
    output = 6
    assert soln.maxPathSum(root) == output


def test_case_2():
    root = soln.build_tree([-10, 9, 20, None, None, 15, 7])
    output = 42
    assert soln.maxPathSum(root) == output


def test_sub_tree_larger_sum():
    root = soln.build_tree([1, 5, 1, 3, 7, 1, 0])
    output = 15
    assert soln.maxPathSum(root) == output


def test_negative_included_in_sum():
    root = soln.build_tree([5, -3, 2, 6, 4, 3, 1])
    output = 13
    assert soln.maxPathSum(root) == output


def test_single_node():
    root = soln.build_tree([5])
    output = 5
    assert soln.maxPathSum(root) == output


def test_single_negative_node():
    root = soln.build_tree([-5])
    output = -5
    assert soln.maxPathSum(root) == output


def test_all_negative_nodes():
    root = soln.build_tree([-5, -2, -1, -4, -10, -3, -45, -20])
    output = -1
    assert soln.maxPathSum(root) == output


def test_only_uses_single_sub_tree():
    root = soln.build_tree([-6, None, 3, None, None, 2])
    output = 5
    assert soln.maxPathSum(root) == output
