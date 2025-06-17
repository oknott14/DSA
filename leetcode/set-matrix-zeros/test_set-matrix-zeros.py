from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zero_rows = set()
        zero_cols = set()

        def reverse_zero_col(row, col):
            for r in range(row):
                matrix[r][col] = 0

        def reverse_zero_row(row, col):
            for c in range(col):
                matrix[row][c] = 0

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    if not row in zero_rows:
                        zero_rows.add(row)
                        reverse_zero_row(row, col)

                    if not col in zero_cols:
                        zero_cols.add(col)
                        reverse_zero_col(row, col)

                elif row in zero_rows or col in zero_cols:
                    matrix[row][col] = 0


soln = Solution()


def test_case_1():
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    output = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
    soln.setZeroes(matrix)
    assert str(matrix) == str(output)


def test_case_2():
    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    output = [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
    soln.setZeroes(matrix)
    assert str(matrix) == str(output)


def test_sets_row_of_zeros():
    matrix = [[0, 1]]
    output = [[0, 0]]
    soln.setZeroes(matrix)
    assert str(matrix) == str(output)


def test_sets_col_of_zeros():
    matrix = [[1, 0], [1, 1]]
    output = [[0, 0], [1, 0]]
    soln.setZeroes(matrix)
    assert str(matrix) == str(output)
