class Solution:
    min_num = -(2**31)
    max_num = (2**31) - 1

    def reverse(self, x: int) -> int:
        neg = 1 if 0 < x else -1
        x = abs(x)
        rev = 0

        while 0 < x:
            rem = x % 10
            x //= 10

            rev = (rev * 10) + rem

        rev *= neg
        if rev < self.min_num or self.max_num < rev:
            return 0

        return rev

    # def reverse(self, x: int) -> int:
    #     neg = 1 if 0 < x else -1

    #     x = int(str(abs(x))[::-1]) * neg

    #     if x < self.min_num or self.max_num < x:
    #         return 0

    #     return x


soln = Solution()


def test_case_1():
    assert soln.reverse(123) == 321


def test_case_2():
    assert soln.reverse(-123) == -321


def test_case_3():
    assert soln.reverse(120) == 21


def test_case_lower_bound():
    assert soln.reverse(-(2**31)) == 0


def test_case_upper_bound():
    assert soln.reverse((2**31) - 1) == 0


def test_reverse_to_upper_bound():
    assert soln.reverse(-8463847412) == -(2**31)


def test_case_1037():
    assert soln.reverse(1534236469) == 0


def test_case_1037_2():
    assert soln.reverse(-1534236469) == 0
