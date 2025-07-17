from typing import List, Tuple


class Solution:
    def trap(self, heights: List[int]) -> int:
        # 4ms -> beats 92%
        # O(n) -> checks each position at most twice
        trapped_water = 0
        left = max_left = 0
        right = max_right = len(heights) - 1

        while left < right:
            if heights[max_left] <= heights[max_right]:
                left += 1

                if heights[left] < heights[max_left]:
                    trapped_water += heights[max_left] - heights[left]
                else:
                    max_left = left
            else:
                right -= 1

                if heights[right] < heights[max_right]:
                    trapped_water += heights[max_right] - heights[right]
                else:
                    max_right = right

        return trapped_water

    def trap_2(self, heights: List[int]) -> int:
        # 21 mx -> beats 34%
        # O(n * d) where d is the avg difference in heights
        height_locs: List[Tuple[int, int]] = []
        trapped_water = 0

        for idx in range(len(heights)):
            if heights[idx] == 0:
                continue

            base_height = 0
            while len(height_locs) and height_locs[-1][0] <= heights[idx]:
                prev_height, height_at = height_locs.pop()
                trapped_water += (prev_height - base_height) * (idx - height_at)
                base_height = prev_height

            if (
                len(height_locs)
                and base_height < heights[idx]
                and heights[idx] < height_locs[-1][0]
            ):
                trapped_water += (heights[idx] - base_height) * (
                    idx - height_locs[-1][1]
                )

            height_locs.append((heights[idx], idx + 1))

        return trapped_water


soln = Solution()


def test_case_1():
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    assert soln.trap(height) == 6


def test_case_2():
    height = [4, 2, 0, 3, 2, 5]
    assert soln.trap(height) == 9


def test_case_215():
    height = [5, 5, 1, 7, 1, 1, 5, 2, 7, 6]
    assert soln.trap(height) == 23
