from typing import List


class Solution:
    # 7ms beats 99%
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        dp = [0] * n
        dp[0] = grid[0][0]

        for idx in range(1, n):
            dp[idx] = grid[0][idx] + dp[idx - 1]

        for row in range(1, m):
            dp[0] += grid[row][0]

            for col in range(1, n):
                dp[col] = grid[row][col] + min(dp[col - 1], dp[col])

        return dp[-1]

    # 13ms beats 60%
    # def minPathSum(self, grid: List[List[int]]) -> int:
    #     m, n = len(grid), len(grid[0])

    #     dp = [[0] * n for _ in range(m)]
    #     dp[0][0] = grid[0][0]

    #     for idx in range(1, m):
    #         dp[idx][0] = grid[idx][0] + dp[idx - 1][0]

    #     for idx in range(1, n):
    #         dp[0][idx] = grid[0][idx] + dp[0][idx - 1]

    #     row = col = 1

    #     while row < m or col < n:
    #         row = min(row, m - 1)
    #         col = min(col, n - 1)
    #         dp[row][col] = grid[row][col] + min(dp[row - 1][col], dp[row][col - 1])

    #         for idx in range(row + 1, m):
    #             dp[idx][col] = grid[idx][col] + min(dp[idx - 1][col], dp[idx][col - 1])

    #         for idx in range(col + 1, n):
    #             dp[row][idx] = grid[row][idx] + min(dp[row - 1][idx], dp[row][idx - 1])

    #         row += 1
    #         col += 1

    #     return dp[m - 1][n - 1]

    # Beats 30ms beats 25%
    # def minPathSum(self, grid: List[List[int]]) -> int:
    #     m, n = len(grid), len(grid[0])

    #     dp = [[-1] * n for _ in range(m)]
    #     dp[0][0] = grid[0][0]

    #     for idx in range(1, m):
    #         dp[idx][0] = grid[idx][0] + dp[idx - 1][0]

    #     for idx in range(1, n):
    #         dp[0][idx] = grid[0][idx] + dp[0][idx - 1]

    #     def dfs(row: int, col: int):
    #         if dp[row][col] < 0:
    #             dp[row][col] = grid[row][col] + min(
    #                 dfs(row - 1, col), dfs(row, col - 1)
    #             )

    #         return dp[row][col]

    #     return dfs(m - 1, n - 1)


soln = Solution()


def test_case_1():
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    assert soln.minPathSum(grid) == 7


def test_case_2():
    grid = [[1, 2, 3], [4, 5, 6]]
    assert soln.minPathSum(grid) == 12


def test_single_row():
    grid = [[1, 1, 1, 1]]
    assert soln.minPathSum(grid) == 4


def test_path_of_0():
    grid = [
        [0, 1, 1, 1, 1, 1],
        [0, 0, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 1],
        [1, 0, 1, 0, 0, 0],
    ]

    assert soln.minPathSum(grid) == 0
