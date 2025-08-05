from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        grids = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                num = board[row][col]

                if num == ".":
                    continue

                g_idx = 3 * (row // 3) + col // 3

                if num in rows[row] or num in cols[col] or num in grids[g_idx]:
                    return False

                rows[row].add(num)
                cols[col].add(num)
                grids[g_idx].add(num)
        return True

    # Memory Efficient beats 7%
    # def isValidSudoku(self, board: List[List[str]]) -> bool:
    #     col = set()
    #     row = set()
    #     grid = set()

    #     for iter in range(9):
    #         grid_row = 3 * (iter // 3)
    #         grid_col = 3 * (iter % 3)

    #         for idx in range(9):
    #             if board[iter][idx] != "." and board[iter][idx] in col:
    #                 return False
    #             else:
    #                 col.add(board[iter][idx])  # col

    #             if board[idx][iter] != "." and board[idx][iter] in row:
    #                 return False
    #             else:
    #                 row.add(board[idx][iter])

    #             grd = board[grid_row + idx // 3][grid_col + idx % 3]
    #             if grd != "." and grd in grid:
    #                 return False
    #             else:
    #                 grid.add(grd)
    #         row.clear()
    #         col.clear()
    #         grid.clear()
    #     return True


soln = Solution()


def test_case_1():
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]

    assert soln.isValidSudoku(board)


def test_case_2():
    board = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    assert not soln.isValidSudoku(board)


def test_invalid_by_row():
    board = [
        ["5", "3", ".", ".", "7", ".", ".", "3", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]

    assert not soln.isValidSudoku(board)


def test_invalid_by_col():
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "9"],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    assert not soln.isValidSudoku(board)
