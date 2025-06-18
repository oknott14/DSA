from typing import List, Optional, Self


class TreeNode:
    def __init__(self, x, left: Optional[Self] = None, right: Optional[Self] = None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        def traverse(node: Optional[TreeNode], low: int, high: int) -> TreeNode:
            if low <= node.val <= high:
                return node
            elif node.val < low:
                return traverse(node.right, low, high)
            else:
                return traverse(node.left, low, high)

        return traverse(root, min(p.val, q.val), max(p.val, q.val))

    def build_tree(self, lst: List[int | None]) -> TreeNode:
        def build(index: int) -> TreeNode:
            if len(lst) <= index or lst[index] is None:
                return None
            else:
                return TreeNode(lst[index], build(2 * index + 1), build(2 * index + 2))

        return build(0)

    def find_node(self, root: TreeNode, val: int):
        node = root
        while node.val != val:
            if node.val < val:
                node = node.right
            else:
                node = node.left
        return node


soln = Solution()


def test_ancestor_is_p_or_q():
    root = soln.build_tree([2, 1])
    p = soln.find_node(root, 1)
    q = soln.find_node(root, 2)
    lca = soln.find_node(root, 2)
    assert soln.lowestCommonAncestor(root, p, q) == lca
    assert soln.lowestCommonAncestor(root, q, p) == lca


def test_ancestor_is_parent_of_p_and_q():
    root = soln.build_tree([2, 1, 3])
    p = soln.find_node(root, 1)
    q = soln.find_node(root, 3)
    lca = soln.find_node(root, 2)
    assert soln.lowestCommonAncestor(root, p, q) == lca
    assert soln.lowestCommonAncestor(root, q, p) == lca


def test_p_or_q_deeply_nested():
    root = soln.build_tree([5, 3, 9, 1, 2])
    p = soln.find_node(root, 1)
    q = soln.find_node(root, 9)
    lca = soln.find_node(root, 5)
    assert soln.lowestCommonAncestor(root, p, q) == lca
    assert soln.lowestCommonAncestor(root, q, p) == lca


def test_p_and_q_deeply_nested():
    root = soln.build_tree(
        [5, 3, 9, 1, 4, 6, 11, None, None, None, None, None, None, 10, 12]
    )
    p = soln.find_node(root, 4)
    q = soln.find_node(root, 12)
    lca = soln.find_node(root, 5)
    assert soln.lowestCommonAncestor(root, p, q) == lca
    assert soln.lowestCommonAncestor(root, q, p) == lca


def test_case_1():
    root = soln.build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    p = soln.find_node(root, 2)
    q = soln.find_node(root, 8)
    lca = soln.find_node(root, 6)
    assert soln.lowestCommonAncestor(root, p, q) == lca


def test_case_2():
    root = soln.build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    p = soln.find_node(root, 2)
    q = soln.find_node(root, 4)
    lca = soln.find_node(root, 2)
    assert soln.lowestCommonAncestor(root, p, q) == lca
