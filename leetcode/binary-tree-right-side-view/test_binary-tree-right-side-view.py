from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 0MS Beat 100% and 88%
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        right_side = []

        # Check the empty case
        if root is None:
            return right_side

        # Create BFS Queue
        queue = deque()
        queue.append(root)

        def add_to_queue(node: TreeNode):
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)

        while queue:
            # Pop Right Side of Queue (Right most child at level)
            curr = queue.popleft()

            # Add value as right most node at this level
            right_side.append(curr.val)

            # Number of nodes at this level
            level_nodes = len(queue)

            # Add Curr's children
            add_to_queue(curr)

            # Loop over all nodes at current level
            # Add right then left for each
            for _ in range(level_nodes):
                add_to_queue(queue.popleft())

        return right_side

    def build_tree(
        self, tree_arr: List[int | None], index: int = 0
    ) -> Optional[TreeNode]:
        if len(tree_arr) <= index or tree_arr[index] is None:
            return None
        else:
            return TreeNode(
                tree_arr[index] if tree_arr[index] is not None else 0,  # type: ignore
                self.build_tree(tree_arr, 2 * index + 1),
                self.build_tree(tree_arr, 2 * index + 2),
            )


soln = Solution()


def test_case_1():
    root = soln.build_tree([1, 2, 3, None, 5, None, 4])

    assert soln.rightSideView(root) == [1, 3, 4]


def test_case_2():
    root = soln.build_tree([1, 2, 3, 4, None, None, None, 5])
    assert soln.rightSideView(root) == [1, 3, 4, 5]


def test_case_3():
    root = soln.build_tree([1, None, 3])
    assert soln.rightSideView(root) == [1, 3]


def test_empyt_tree():
    assert soln.rightSideView(None) == []


def test_all_lefts():
    root = soln.build_tree([1, 2, None, 3, None, None, None, 4])
    assert soln.rightSideView(root) == [1, 2, 3, 4]
