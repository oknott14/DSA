from collections import deque
def isBalanced(s: str):
    # Write your code here
    brackets = {"{": "}", "(": ")", "[": "]"}
    open_brackets = deque()

    for bracket in s:
        if bracket in brackets:
            open_brackets.append(bracket)

        elif 0 == len(open_brackets) or brackets[open_brackets.pop()] != bracket:
            return "NO"

    return "NO" if len(open_brackets) else "YES"




def test_case_1():
    assert isBalanced('[{()}]') == 'YES'
