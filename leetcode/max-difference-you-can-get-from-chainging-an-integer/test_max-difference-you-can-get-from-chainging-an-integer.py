from math import floor, log


class Solution:
    def maxDiff(self, num: int) -> int:
        p_ten = 10 ** floor(log(num, 10))
        rep_a = rep_b = num // p_ten
        a_swap = b_swap = 8
        diff = 0

        while 0 < p_ten:
            div = num // p_ten

            if div == rep_a: 
                diff += a_swap * p_ten

            elif div == rep_b:
                diff += b_swap * p_ten

            elif rep_b == 1 and 1 < div:
                rep_b = div
                b_swap = div 
                diff += b_swap * p_ten

            elif rep_a == 9 and div < 9:
                rep_a = div
                a_swap = 9 - div
                diff += a_swap * p_ten

            num -= div * p_ten
            p_ten //= 10
            
        return diff


soln = Solution()


def test_case_1():
    assert soln.maxDiff(555) == 888


def test_single_digit_always_8():
    for num in range(1, 10):
        assert soln.maxDiff(num) == 8


def test_replaces_only_leftmost_digit():
    assert soln.maxDiff(12131415) == 82808080


def test_replaces_only_1():
    assert soln.maxDiff(123456) == 820000

def test_rep_a_is_9():
    assert soln.maxDiff(9288) == 8700

def test_rep_a_is_1():
    assert soln.maxDiff(12345) == 82000

def test_all_1():
    assert soln.maxDiff(11111) == 88888

def test_all_9():
    assert soln.maxDiff(99999) == 88888