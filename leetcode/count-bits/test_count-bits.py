from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        bits = [1] * (n + 1)
        bits[0] = 0
        last_power = 0
        next_power = 2
        for i in range(n + 1):
            if i == next_power:
                last_power = next_power
                next_power *= 2
            else:
                bits[i] = bits[last_power] + bits[i - last_power]
        return bits


soln = Solution()


def test_case_1():
    assert soln.countBits(2) == [0, 1, 1]


def test_case_2():
    assert soln.countBits(5) == [0, 1, 1, 2, 1, 2]


def test_bits_11():
    assert soln.countBits(11)[11] == 3


def test_bits_128():
    assert soln.countBits(128)[128] == 1


def test_2_to_the_n():
    n = 10

    bits = soln.countBits(2**n)

    for i in range(1, 10):
        assert bits[2**i] == 1
