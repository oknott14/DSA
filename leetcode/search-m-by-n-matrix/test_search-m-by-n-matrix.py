from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        row = 0
        left, right = 0, n - 1
        mid = right // 2

        while row < m and target > matrix[row][right]:
            row += 1

        if m == row:
            return False

        while left < right and matrix[row][mid] != target:
            if target < matrix[row][mid]:
                right = mid
            else:
                left = mid + 1

            mid = (right + left) // 2

        return matrix[row][mid] == target


soln = Solution()


def test_case_1():
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 3
    assert soln.searchMatrix(matrix, target)


def test_case_2():
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 13
    assert not soln.searchMatrix(matrix, target)


def test_second_row():
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 16
    assert soln.searchMatrix(matrix, target)


def test_single_item():
    matrix = [[1]]
    target = 0
    assert not soln.searchMatrix(matrix, target)


def test_not_in_row():
    matrix = [[1, 3]]
    target = 2

    assert not soln.searchMatrix(matrix, target)
