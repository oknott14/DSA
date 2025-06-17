from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        in_idx = {inorder[idx]: idx for idx in range(len(inorder))}

        def build(
            pre_left: int, pre_right: int, in_left: int, in_right: int
        ) -> Optional[TreeNode]:
            if pre_right < pre_left:
                return None

            idx = in_idx[preorder[pre_left]]
            left_size = idx - in_left
            return TreeNode(
                preorder[pre_left],
                build(pre_left + 1, pre_left + left_size, in_left, idx - 1),
                build(pre_left + left_size + 1, pre_right, idx + 1, in_right),
            )

        return build(0, len(preorder) - 1, 0, len(inorder) - 1)

    def tree_to_arr(self, root: Optional[TreeNode]) -> List[int | None]:
        if not root:
            return []

        result = []
        queue = deque([(root, 0)])  # Store node and its index

        while queue:
            node, index = queue.popleft()

            while len(result) <= index:
                result.append(None)
            result[index] = node.val

            if node.left:
                queue.append((node.left, 2 * index + 1))
            if node.right:
                queue.append((node.right, 2 * index + 2))
        return result

    def run(self, preorder: List[int], inorder: List[int]) -> List[int | None]:
        tree = self.buildTree(preorder, inorder)
        return self.tree_to_arr(tree)


soln = Solution()


def test_base_balanced():
    preorder = [3, 9, 20]
    inorder = [9, 3, 20]
    output = [3, 9, 20]
    assert soln.run(preorder, inorder) == output


def test_base_right_only():
    preorder = [3, 20, 15, 23]
    inorder = [
        3,
        15,
        20,
        23,
    ]
    output = [3, None, 20, None, None, 15, 23]
    assert soln.run(preorder, inorder) == output


def test_base_left_only():
    preorder = [3, 9, 4, 7]
    inorder = [4, 9, 7, 3]
    output = [3, 9, None, 4, 7]
    assert soln.run(preorder, inorder) == output


def test_case_1():
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    output = [3, 9, 20, None, None, 15, 7]
    assert soln.run(preorder, inorder) == output


def test_case_single_node():
    preorder = [-1]
    inorder = [-1]
    output = [-1]
    assert soln.run(preorder, inorder) == output


def test_many_missing_children():
    preorder = [3, 9, 4, 7, 5, 2, 20, 15, 6, 23, 21, 30]
    inorder = [4, 9, 5, 7, 2, 3, 6, 15, 20, 21, 23, 30]
    output = [3, 9, 20, 4, 7, 15, 23, None, None, 5, 2, 6, None, 21, 30]
    assert soln.run(preorder, inorder) == output


def test_right_child_only():
    preorder = [3, 20, 15, 6, 4, 23, 21, 30]
    inorder = [3, 6, 15, 4, 20, 21, 23, 30]
    output = [3, None, 20, None, None, 15, 23, None, None, None, None, 6, 4, 21, 30]
    assert soln.run(preorder, inorder) == output


def test_tree_to_arr():
    tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    output = [3, 9, 20, None, None, 15, 7]
    assert soln.tree_to_arr(tree) == output
