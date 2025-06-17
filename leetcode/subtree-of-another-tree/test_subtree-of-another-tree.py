# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(nodes: List[int | None], index: int = 0) -> TreeNode:
    if len(nodes) <= index:
        return None
    else:
        return TreeNode(
            nodes[index],
            build_tree(nodes, 2 * index + 1),
            build_tree(nodes, 2 * index + 1),
        )


class Solution:
    def isSubtree(self, root: Optional[TreeNode], sub_root: Optional[TreeNode]) -> bool:
        return self.hash_tree(sub_root) in self.hash_tree(root)

    def hash_tree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return "#"
        else:
            return f",{root.val}{self.hash_tree(root.left)}{self.hash_tree(root.right)}"


soln = Solution()


def test_two_empyt_tres():
    tree = TreeNode(None)
    assert soln.isSubtree(tree, tree)


def test_two_single_node_trees_equal():
    tree = TreeNode(1)
    assert soln.isSubtree(tree, tree)


def test_two_single_node_trees_not_equal():
    assert not soln.isSubtree(TreeNode(1), TreeNode(2))


def test_equal_single_node_sub_tree():
    tree = build_tree([3, 4, 5])
    sub_tree = TreeNode(4)

    assert soln.isSubtree(tree, sub_tree)


def test_not_equal_single_node_sub_tree():
    tree = build_tree([3, 4, 5])
    sub_tree = TreeNode(6)

    assert not soln.isSubtree(tree, sub_tree)


def test_sub_tree_equals_tree():
    tree = build_tree([1, 2, 3])
    assert soln.isSubtree(tree, tree)


def test_case_1():
    tree = build_tree([3, 4, 5, 1, 2])
    sub_tree = build_tree([4, 1, 2])

    assert soln.isSubtree(tree, sub_tree)


def test_case_2():
    tree = build_tree([3, 4, 5, 1, 2, None, None, None, None, 0])
    sub_tree = build_tree([4, 1, 2])

    assert not soln.isSubtree(tree, sub_tree)


def test_case_3():
    tree = build_tree([1, 1])
    sub_tree = TreeNode(1)
    assert soln.isSubtree(tree, sub_tree)


def test_case_4():
    assert not soln.isSubtree(TreeNode(12), TreeNode(2))
