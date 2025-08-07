from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        total_candies = len(ratings)
        candies = [0] * len(ratings)

        for idx in range(1, len(ratings)):
            if ratings[idx - 1] < ratings[idx]:
                candies[idx] = 1 + candies[idx - 1]
                total_candies += candies[idx]

        for idx in range(len(candies) - 2, -1, -1):
            if ratings[idx + 1] < ratings[idx] and candies[idx] <= candies[idx + 1]:
                total_candies -= candies[idx]
                candies[idx] = 1 + candies[idx + 1]
                total_candies += candies[idx]

        return total_candies


soln = Solution()


def test_case_1():
    assert soln.candy([1, 0, 2]) == 5


def test_case_2():
    assert soln.candy([1, 2, 2]) == 4


def test_case_3():
    assert soln.candy([1, 2, 2, 1]) == 6


def test_all_same_rating():
    assert soln.candy([1, 1, 1, 1, 1, 1, 1]) == 7


def test_increasing_ratings():
    assert soln.candy([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 45


def test_decreasing_ratings():
    assert soln.candy([9, 8, 7, 6, 5, 4, 3, 2, 1]) == 45


def test_middle_much_lower():
    assert soln.candy([1, 2, 3, 0, 4, 3, 2, 1]) == 17

def test_rises_then_same():
    assert soln.candy([1,2,2,2,2,2,1]) == 9