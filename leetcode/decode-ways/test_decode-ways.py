class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0

        dp = [1, 1]
        last = int(s[0])
        curr = 0
        for idx in range(1, len(s)):
            curr = int(s[idx])

            if curr == 0:
                if not 0 < last < 3:
                    # cant decode invalid zero
                    return 0
                else:
                    # 10 or 20 is ok -> same amnt of ways
                    # reduce ways to prev value
                    last = dp[1]
                    dp[1] = dp[0]
                    dp[0] = last - dp[1]
            elif 0 < last < 3 and last * curr < 13:
                # 11 to 26 can be repped 2 ways
                last = dp[0]
                dp[0] = dp[1]
                dp[1] = dp[0] + last
            else:
                dp[0] = dp[1]

            last = curr
        return dp[1]


soln = Solution()


def test_case_1():
    input = "12"
    output = 2
    assert soln.numDecodings(input) == output


def test_case_2():
    input = "226"
    output = 3
    assert soln.numDecodings(input) == output


def test_case_3():
    assert soln.numDecodings("06") == 0


def test_case_4():
    assert soln.numDecodings("2351624105") == 8


def test_case_5():
    assert soln.numDecodings("1233442145345001234") == 0


def test_case_6():
    assert soln.numDecodings("270") == 0


def test_case_7():
    assert soln.numDecodings("2176") == 3


def test_case_8():
    assert soln.numDecodings("2101") == 1


def test_case_9():
    assert soln.numDecodings("1123") == 5


def test_case_10():
    input = "11231214"
    outputs = [1, 2, 3, 5, 5, 10, 15, 25]

    for idx in range(len(outputs)):
        assert soln.numDecodings(input[: idx + 1]) == outputs[idx]
