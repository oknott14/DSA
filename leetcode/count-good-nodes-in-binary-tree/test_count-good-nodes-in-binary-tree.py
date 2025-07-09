from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def traverse(node: Optional[TreeNode], max_in_path: int):
            if node is None:
                return 0

            max_in_path = max(node.val, max_in_path)

            return (
                (1 if max_in_path == node.val else 0)
                + traverse(node.left, max_in_path)
                + traverse(node.right, max_in_path)
            )

        return traverse(root, root.val - 1)

    def build_tree(
        self, tree_arr: List[int | None], index: int = 0
    ) -> Optional[TreeNode]:
        if len(tree_arr) <= index or tree_arr[index] is None:
            return None
        else:
            return TreeNode(
                tree_arr[index] or 0,
                self.build_tree(tree_arr, 2 * index + 1),
                self.build_tree(tree_arr, 2 * index + 2),
            )


soln = Solution()


def test_case_1():
    assert True
