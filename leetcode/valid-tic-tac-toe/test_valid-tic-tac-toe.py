from typing import List


class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        diff = 0
        down = accross = 0
        cost = {"X": 1, "O": -1, " ": 0}
        x_wins = o_wins = False
        for iter in range(3):
            for idx in range(3):
                down += cost[board[idx][iter]]
                accross += cost[board[iter][idx]]

            diff += down
            x_wins = x_wins or down == 3 or accross == 3
            o_wins = o_wins or down == -3 or accross == -3
            down = accross = 0

        d1 = d2 = 0
        for idx in range(3):
            d1 += cost[board[idx][idx]]
            d2 += cost[board[idx][2 - idx]]

        x_wins = x_wins or d1 == 3 or d2 == 3
        o_wins = o_wins or d1 == -3 or d2 == -3

        return (0 <= diff <= 1) and (
            ((x_wins and diff == 1) or (o_wins and diff == 0) or not (x_wins or o_wins))
            and (not (x_wins and o_wins))
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
    assert not soln.validTicTacToe(["OXX", "XOX", "OXO"])
