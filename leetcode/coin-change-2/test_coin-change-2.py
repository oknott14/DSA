from typing import List

# 1 <= coins.length <= 300
# 1 <= coins[i] <= 5000
# All the values of coins are unique.
# 0 <= amount <= 5000


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        amounts = [0] * (amount + 1)
        amounts[0] = 1

        for coin in coins:
            for idx in range(coin, amount + 1):
                amounts[idx] += amounts[idx - coin]

        return amounts[-1]


soln = Solution()


def test_case_1():
    amnt = 5
    coins = [1, 2, 5]
    output = 4
    assert soln.change(amnt, coins) == output


def test_case_2():
    amnt = 3
    coins = [2]
    output = 0
    assert soln.change(amnt, coins) == output


def test_case_3():
    amnt = 10
    coins = [10]
    output = 1
    assert soln.change(amnt, coins) == output


def test_case_14():
    amnt = 500
    coins = [3, 5, 7, 8, 9, 10, 11]
    output = 35502874
    assert soln.change(amnt, coins) == output


def test_custom_1():
    amnt = 6
    coins = [1, 2, 5]
    output = 5
    assert soln.change(amnt, coins) == output
