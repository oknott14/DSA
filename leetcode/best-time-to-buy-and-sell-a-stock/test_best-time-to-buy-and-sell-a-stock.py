from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        for idx in range(1, len(prices)):
            if prices[idx - 1] < prices[idx]:
                max_profit += prices[idx] - prices[idx - 1]

        return max_profit


soln = Solution()


def test_case_1():
    assert soln.maxProfit([7, 1, 5, 3, 6, 4]) == 7


def test_case_2():
    assert soln.maxProfit([1, 2, 3, 4, 5]) == 4


def test_case_3():
    assert soln.maxProfit([7, 6, 4, 3, 1]) == 0


def test_all_equal():
    assert soln.maxProfit([1, 1, 1, 1, 1]) == 0


def test_gets_biggest_diff():
    assert soln.maxProfit([1, 2, 3, 4, 5, 5, 3, 2, 1, 2, 3, 4, 5, 6]) == 9

def test_peak_then_valley():
    assert soln.maxProfit([1,2,3,2,3,4,5]) == 5