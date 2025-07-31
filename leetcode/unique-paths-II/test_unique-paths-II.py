from typing import List


class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if 0 < grid[m - 1][n - 1] + grid[0][0]:
            return 0

        dp = {}
        dp[(m - 1, n - 1)] = 1

        for i in range(m - 2, -1, -1):
            if grid[i][n - 1] == 1:
                dp[(i, n - 1)] = 0
            else:
                dp[(i, n - 1)] = dp[(i + 1, n - 1)]

        for i in range(n - 2, -1, -1):
            if grid[m - 1][i] == 1:
                dp[(m - 1, i)] = 0
            else:
                dp[(m - 1, i)] = dp[(m - 1, i + 1)]

        def dfs(row: int, col: int):
            if (row, col) not in dp:
                if grid[row][col] == 1:
                    dp[(row, col)] = 0
                else:
                    dp[(row, col)] = dfs(row + 1, col) + dfs(row, col + 1)

            return dp[(row, col)]

        return dfs(0, 0)


soln = Solution()


def test_case_1():
    obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    assert soln.uniquePathsWithObstacles(obstacleGrid) == 2


def test_case_2():
    obstacleGrid = [[0, 1], [0, 0]]
    assert soln.uniquePathsWithObstacles(obstacleGrid) == 1


def test_case_obs_at_start():
    grid = [[1, 0]]
    assert soln.uniquePathsWithObstacles(grid) == 0


def test_case_obs_at_end():
    assert soln.uniquePathsWithObstacles([[0, 1]]) == 0


def test_single_path_many_obs():
    assert (
        soln.uniquePathsWithObstacles(
            [[0, 0, 1, 0, 0], [1, 0, 0, 1, 0], [0, 1, 0, 0, 0]]
        )
        == 1
    )


def test_cant_go_up():
    assert soln.uniquePathsWithObstacles([[0, 1, 0, 0, 0], [0, 0, 0, 1, 0]]) == 0
