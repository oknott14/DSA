class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n]

        for row in range(1, m):
            dp.append([0] * n)
            dp[row][0] = 1
            for col in range(1, n):
                dp[row][col] = dp[row - 1][col] + dp[row][col - 1]
        return dp[m - 1][n - 1]


soln = Solution()


def test_base_case():
    assert soln.uniquePaths(1, 1) == 1


def test_long_single_row():
    assert soln.uniquePaths(1, 20) == 1


def test_long_single_col():
    assert soln.uniquePaths(20, 1) == 1


def test_2x2():
    assert soln.uniquePaths(2, 2) == 2


def test_3x3():
    assert soln.uniquePaths(3, 3) == 6


def test_4x3():
    assert soln.uniquePaths(4, 3) == 10


def test_communitive():
    assert soln.uniquePaths(4, 3) == soln.uniquePaths(3, 4)


def test_4x4():
    assert soln.uniquePaths(4, 4) == 20


def test_case_1():
    assert soln.uniquePaths(3, 7) == 28


def test_case_2():
    assert soln.uniquePaths(3, 2) == 3


def test_5x5():
    assert soln.uniquePaths(5, 5) == 70
