from collections import deque
from typing import List

# class Solution:
#     def orangesRotting(self, grid: List[List[int]]) -> int:
#         m, n = len(grid), len(grid[0])
#         max_rotten = m * n + 1
#         distances = [[max_rotten] * n for _ in range(m)]
#         min_rotten = 0

#         def in_bounds(row: int, col: int) -> bool:
#             return 0 <= row and row < m and 0 <= col and col < n

#         def dfs(row: int, col: int) -> int:
#             if not in_bounds(row, col):
#                 return max_rotten
#             elif grid[row][col] == 0:
#                 return distances[row][col]
#             elif grid[row][col] == 2:
#                 distances[row][col] = 0
#                 return 0
#             else:
#                 grid[row][col] = 0
#                 distances[row][col] = 1 + min(
#                     dfs(row + dr, col + dc)
#                     for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]
#                 )
#                 grid[row][col] = 1

#                 return distances[row][col]


#         for row in range(m):
#             for col in range(n):
#                 if grid[row][col] == 1:
#                     min_rotten = max(dfs(row, col), min_rotten)
#                     if max_rotten <= min_rotten:
#                         return -1
#         return min_rotten
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def in_bounds(row: int, col: int) -> bool:
            return 0 <= row and row < m and 0 <= col and col < n

        rotten_oranges = deque()
        fresh_oranges = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 2:
                    rotten_oranges.append((row, col))
                    grid[row][col] = 0
                elif grid[row][col] == 1:
                    fresh_oranges += 1

        if len(rotten_oranges) == 0:
            return 0 if not fresh_oranges else -1

        minutes = -1
        while rotten_oranges:
            minutes += 1
            for _ in range(len(rotten_oranges)):
                row, col = rotten_oranges.popleft()

                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr = row + dr
                    nc = col + dc
                    if in_bounds(nr, nc) and grid[nr][nc] == 1:
                        rotten_oranges.append((nr, nc))
                        grid[nr][nc] = 2
                        fresh_oranges -= 1

        return minutes if not fresh_oranges else -1


soln = Solution()


def test_case_1():
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    assert soln.orangesRotting(grid) == 4


def test_case_2():
    grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
    assert soln.orangesRotting(grid) == -1


def test_case_3():
    grid = [[0, 2]]
    assert soln.orangesRotting(grid) == 0


def test_single_rotten_line():
    grid = [[1, 1, 1, 1, 2]]
    assert soln.orangesRotting(grid) == 4


def test_double_rotting_line():
    grid = [[2, 1, 1, 2]]
    assert soln.orangesRotting(grid) == 1


def test_2_islands():
    grid = [[2, 1, 1, 0], [1, 1, 0, 1], [1, 0, 1, 1], [0, 1, 1, 2]]

    assert soln.orangesRotting(grid) == 2


def test_case_305():
    grid = [
        [2, 2, 0, 1, 1, 1, 0, 2],
        [0, 0, 0, 2, 0, 1, 2, 2],
        [2, 2, 0, 1, 1, 2, 1, 0],
        [1, 2, 2, 2, 0, 1, 2, 1],
        [0, 0, 0, 2, 1, 1, 2, 0],
        [1, 2, 2, 2, 0, 0, 0, 0],
        [2, 2, 2, 1, 0, 0, 2, 1],
        [2, 0, 0, 2, 0, 1, 0, 1],
        [2, 2, 2, 1, 2, 1, 2, 1],
    ]

    assert soln.orangesRotting(grid) == 2


def test_case_286():
    grid = [
        [0, 2],
        [1, 1],
        [2, 0],
        [2, 2],
        [1, 0],
        [1, 1],
        [0, 1],
        [2, 2],
        [1, 2],
        [0, 2],
    ]

    assert soln.orangesRotting(grid) == 2
