from collections import deque
from typing import List


def generateParenthesis(n: int) -> List[str]:
    queue = deque()
    queue.append(("(", 1))
    parens = []

    while queue:
        curr, used = queue.popleft()

        if used < n:
            queue.append((curr + "(", used + 1))

            if curr[-1] == "(" or len(curr) < 2 * used:
                queue.append((curr + ")", used))
        else:
            parens.append(curr + ")" * (2 * n - len(curr)))

    return parens


def test_case_1():
    generated = generateParenthesis(3)
    valid = set(["((()))", "(()())", "(())()", "()(())", "()()()"])

    assert len(generated) == len(valid)
    for s in generated:
        assert s in valid


def test_case_2():
    assert generateParenthesis(1) == ["()"]


def test_case_4():
    generated = set(generateParenthesis(4))
    valid = set(
        [
            "(((())))",
            "((()()))",
            "((())())",
            "((()))()",
            "(()(()))",
            "(()()())",
            "(()())()",
            "(())(())",
            "(())()()",
            "()((()))",
            "()(()())",
            "()(())()",
            "()()(())",
            "()()()()",
        ]
    )

    # assert len(valid) == len(generated)
    for s in generated:
        assert s in valid

    for s in valid:
        assert s in generated