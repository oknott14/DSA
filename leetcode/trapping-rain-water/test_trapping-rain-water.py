from typing import List


class Solution:
    def trap(self, heights: List[int]) -> int:
        height_locations = [(0, heights[0])]

        def get_height_idx(height: int):
            left = 0
            right = len(height_locations) - 1
            mid = (right - left) // 2

            while height_locations[left][0] < height:
                if height < height_locations[mid][0]:
                    left = mid
                else:
                    right = mid - 1
            return left

        def add_height(idx: int, height: int):
            pass

        for idx in range(1, len(heights)):
            height = heights[idx]

            if heights[idx - 1] < height:
                get_height_idx(height)

            add_height(idx, height)
        return 0


soln = Solution()


def test_case_1():
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    assert soln.trap(height) == 6


def test_case_2():
    height = [4, 2, 0, 3, 2, 5]
    assert soln.trap(height) == 9
