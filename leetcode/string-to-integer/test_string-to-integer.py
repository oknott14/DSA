class Solution:
    def myAtoi(self, s: str) -> int:
        result = 0
        negative = False
        idx = 0
        s = s.strip()
        nums = set(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])

        if len(s) == 0:
            return 0
        elif s[0] == "-":
            negative = True
            idx = 1
        elif s[0] == "+":
            idx = 1

        while idx < len(s) and s[idx] == "0":
            idx += 1

        while idx < len(s) and s[idx] in nums:
            result *= 10
            result += int(s[idx])
            idx += 1

        if negative:
            result *= -1
            result = max(-(2**31), result)
        else:
            result = min(2**31 - 1, result)

        return result


soln = Solution()


def test_case_1():
    assert soln.myAtoi("42") == 42


def test_case_2():
    assert soln.myAtoi("-042") == -42


def test_case_3():
    assert soln.myAtoi("1337c0d3") == 1337


def test_case_4():
    assert soln.myAtoi("0-1") == 0


def test_words_first_():
    assert soln.myAtoi("words and 123456") == 0


def test_out_of_range():
    high = 2**31
    assert soln.myAtoi(str(high)) == high - 1
    assert soln.myAtoi(str(-1 - high)) == -high
