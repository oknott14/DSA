from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = 0
        max_sum = -1 - (10**4)

        for num in nums:
            curr_sum += num

            max_sum = max(max_sum, curr_sum)

            if curr_sum < 0:
                curr_sum = 0

        return max_sum


soln = Solution()


def test_sums_all_positive_integers():
    input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    output = 55

    assert soln.maxSubArray(input) == output


def test_returns_largest_of_all_negatives():
    input = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
    output = -1

    assert soln.maxSubArray(input) == output


def test_sums_positives_before_large_negative():
    input = [2, 2, -10, 2]
    output = 4

    assert soln.maxSubArray(input) == output


def test_sums_positives_after_large_negative():
    input = [2, 1, -10, 2, 2]
    output = 4

    assert soln.maxSubArray(input) == output


def test_includes_negative_if_sum_of_afterwards_is_larger():
    input = [1, 1, -3, 2, 2]
    output = 4

    assert soln.maxSubArray(input) == output


def test_case_1():
    input = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    output = 6

    assert soln.maxSubArray(input) == output


def test_case_2():
    input = [1]
    output = 1

    assert soln.maxSubArray(input) == output


def test_case_3():
    input = [5, 4, -1, 7, 8]
    output = 23

    assert soln.maxSubArray(input) == output
