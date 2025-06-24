import random


class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF  # Mask to get last 32 bits
        MAX_INT = 0x7FFFFFFF  # Max positive 32-bit intege

        x = a & MASK
        y = b & MASK

        while y != 0:
            car = (x & y) << 1
            x = x ^ y
            y = car & MASK

            print(f"x: {bin(x)}")
            print(f"y: {bin(y)}")

        return x if x <= MAX_INT else ~(x ^ MASK)


soln = Solution()


def test_case_1():
    assert soln.getSum(1, 2) == 3


def test_case_2():
    assert soln.getSum(3, 2) == 5


def test_case_single_negative():
    assert soln.getSum(1, -1) == 0


def test_case_double_negative():
    assert soln.getSum(-2, -2) == -4


def test_many():
    print(bin(976))
    a = list(range(-999, 1000))
    b = list(range(-999, 1000))

    random.shuffle(a)
    random.shuffle(b)

    for idx in range(len(a)):
        assert soln.getSum(a[idx], b[idx]) == a[idx] + b[idx]
