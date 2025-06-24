from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        c_min = c_max = prices[0]
        for price in prices[1:]:
            if price < c_min:
                c_min = c_max = price
            elif c_max < price:
                c_max = price
                max_profit = max(max_profit, c_max - c_min)

        
        return max_profit


soln = Solution()


def test_case_1():
    prices = [7, 1, 5, 3, 6, 4]
    output = 5
    assert soln.maxProfit(prices) == output


def test_case_decreasing():
    prices = [7, 6, 4, 3, 1]
    output = 0
    assert soln.maxProfit(prices) == output


def test_increasing_value():
    prices = [1, 2, 3, 4]
    output = 3
    assert soln.maxProfit(prices) == output


def test_two_buy_periods():
    prices = [1, 2, 3, 4, 1, 2, 3, 4, 5, 6]
    output = 5
    assert soln.maxProfit(prices) == output


def test_flat_price():
    prices = [7] * 10
    output = 0
    assert soln.maxProfit(prices) == output
