class Solution:
    # . -> any single character
    # * -> zero or more of prev char
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        for j in range(1, n + 1):
            if p[j - 1] == "*":
                dp[0][j] = dp[0][j - 2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] in {s[i - 1], "."}:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == "*":
                    dp[i][j] = dp[i][j - 2]
                    if p[j - 2] in {s[i - 1], "."}:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]

        return dp[m][n]


soln = Solution()


def test_case_1():
    assert not soln.isMatch("aa", "a")


def test_case_2():
    assert soln.isMatch("aa", "a*")


def test_case_3():
    assert soln.isMatch("ab", ".*")


def test_case_repeats_to_same_char():
    assert soln.isMatch("aaaaaaabc", "a*abc")
    assert soln.isMatch("abc", "a*abc")


def test_case_repeats_to_other_char():
    assert soln.isMatch("aaaaaabc", "a*bc")


def test_repeats_same():
    assert soln.isMatch("aaaa", "a*aa")


def test_start_then_dot():
    assert soln.isMatch("aaaaabc", "a*.bc")
    assert soln.isMatch("aaabbc", "a*.bc")


def test_case_many_same_repeats():
    assert soln.isMatch("aaa", "a*a*a*")
