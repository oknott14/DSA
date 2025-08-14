from collections import defaultdict
from typing import List


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        N = len(grid)
        island_idx = 2
        islands = defaultdict(int)

        def get_island_size(row: int, col: int):
            if row < 0 or col < 0 or N <= row or N <= col or grid[row][col] != 1:
                return

            islands[island_idx] += 1
            grid[row][col] = island_idx
            for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                get_island_size(row + dr, col + dc)

        def get_adj_islands(row, col):
            if row < 0 or col < 0 or N <= row or N <= col:
                return 0
            return grid[row][col]

        for row in range(N):
            for col in range(N):
                if grid[row][col] == 1:
                    get_island_size(row, col)
                    island_idx += 1

        if len(islands) == 1:
            return (
                islands[island_idx - 1]
                if islands[island_idx - 1] == N * N
                else 1 + islands[island_idx - 1]
            )
        max_size = 0
        used_islands = set()
        for row in range(N):
            for col in range(N):
                if grid[row][col] == 0:  # flippable
                    for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                        used_islands.add(get_adj_islands(row + dr, col + dc))

                    max_size = max(max_size, 1 + sum(islands[i] for i in used_islands))
                    used_islands.clear()

                else:
                    max_size = max(max_size, islands[grid[row][col]])
        return max_size


soln = Solution()


def test_case_1():
    assert soln.largestIsland([[1, 0], [0, 1]]) == 3


def test_case_2():
    assert soln.largestIsland([[1, 1], [1, 0]]) == 4


def test_case_3():
    assert soln.largestIsland([[1, 1], [1, 1]]) == 4
