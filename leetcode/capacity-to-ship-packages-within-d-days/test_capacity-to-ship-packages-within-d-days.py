from math import ceil
from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        max_weight = max(weights)
        sum_weight = sum(weights)
        left = max(max_weight, ceil(sum_weight / days))
        right = min(left + max_weight, ceil(len(weights) / days) * max_weight)

        def ships_in(capac: int):
            days = 1
            space = capac

            for w in weights:
                if space - w < 0:
                    space = capac - w
                    days += 1
                else:
                    space -= w
            return days

        while left <= right:
            mid = (left + right) // 2

            if ships_in(mid) <= days:
                right = mid - 1
            else:
                left = mid + 1

        return left

    # Very slow
    # def shipWithinDays(self, weights: List[int], days: int) -> int:
    #     ps = [0] * (1 + len(weights))
    #     capacity = weights[0]

    #     for idx in range(len(weights)):
    #         ps[idx + 1] = ps[idx] + weights[idx]
    #         capacity = max(capacity, weights[idx])

    #     if len(weights) <= days:
    #         return capacity

    #     next_capacity = capacity
    #     groups = [0] * (days + 1)  # Pointers to the end of each group
    #     while groups[-1] < len(weights):
    #         capacity = next_capacity
    #         next_capacity = ps[-1]
    #         for group in range(1, len(groups)):
    #             # If iterated past => set it to 1 + last group
    #             groups[group] = max(groups[group - 1] + 1, groups[group])

    #             while (
    #                 groups[group] < len(ps)
    #                 and ps[groups[group]] - ps[groups[group - 1]] <= capacity
    #             ):
    #                 groups[group] += 1

    #             if groups[group] < len(ps):
    #                 next_capacity = min(
    #                     next_capacity, ps[groups[group]] - ps[groups[group - 1]]
    #                 )

    #             groups[group] -= 1

    #     return capacity


soln = Solution()


def test_case_1():
    weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    days = 5
    assert soln.shipWithinDays(weights, days) == 15


def test_case_2():
    weights = [3, 2, 2, 4, 1, 4]
    days = 3
    assert soln.shipWithinDays(weights, days) == 6


def test_case_3():
    weights = [1, 2, 3, 1, 1]
    days = 4
    assert soln.shipWithinDays(weights, days) == 3


# def test_balanced_load():
#     weights = []
#     days = 3
#     assert soln.shipWithinDays(weights, days) ==
