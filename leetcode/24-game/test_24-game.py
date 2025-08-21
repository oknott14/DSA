from typing import List


class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        ops = [
            lambda x, y: x + y,
            lambda x, y: x * y,
            lambda x, y: x - y,
            lambda x, y: y - x,
        ]

        def solve(options: List[int]) -> bool:
            E = 1e-6
            if len(options) == 1:
                return abs(options[0] - 24) < E

            for i in range(len(options)):
                for j in range(i + 1, len(options)):
                    if i == j:
                        continue

                    nxt = [
                        options[idx]
                        for idx in range(len(options))
                        if idx != i and idx != j
                    ] + [0]

                    for op in ops:
                        nxt[-1] = op(options[i], options[j])
                        if solve(nxt):
                            return True

                    if E < options[i]:
                        nxt[-1] = options[j] / options[i]
                        if solve(nxt):
                            return True

                    if E < options[j]:
                        nxt[-1] = options[i] / options[j]
                        if solve(nxt):
                            return True

            return False

        return solve(cards)


soln = Solution()


def test_case_1():
    assert not soln.judgePoint24([1, 0, 5, 1])
