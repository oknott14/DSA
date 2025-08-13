from typing import List


class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        diff = 0
        inc = {"X": 1, "O": -1, " ": 0}
        x_winner = o_winner = False
        row_sum = col_sum = 0

        for iter in range(3):
            for idx in range(3):
                diff += inc[board[iter][idx]]
                row_sum += inc[board[iter][idx]]
                col_sum += inc[board[idx][iter]]

            x_winner = x_winner or row_sum == 3 or col_sum == 3
            o_winner = o_winner or row_sum == -3 or col_sum == -3

            if x_winner and o_winner:
                return False
            row_sum = 0
            col_sum = 0

        return (
            (x_winner and diff == 1)
            or (o_winner and diff == 0)
            or (not (x_winner or o_winner) and (diff == 1 or diff == 0))
        )


soln = Solution()


def test_first_player_O():
    board = ["O  ", "   ", "   "]
    assert not soln.validTicTacToe(board)


def test_too_many_X():
    board = ["XOX", " X  ", "   "]
    assert not soln.validTicTacToe(board)


def test_good():
    board = ["XOX", "O O", "XOX"]
    assert soln.validTicTacToe(board)


def test_too_many_O():
    board = ["XOX", "OXO", "O  "]
    assert not soln.validTicTacToe(board)


def test_empty_board():
    board = ["   " for _ in range(3)]
    assert soln.validTicTacToe(board)


def test_x_wins():
    board = ["XXX", "   ", "OOO"]
    assert not soln.validTicTacToe(board)


def test_2_x_winner():
    assert soln.validTicTacToe(["XXX", "OOX", "OOX"])


def test_case_107():
    assert not soln.validTicTacToe(["XXX", "XOO", "OO "])


def test_case_108():
    assert not soln.validTicTacToe([
        "OXX", 
        "XOX", 
        "OXO"
        ])
