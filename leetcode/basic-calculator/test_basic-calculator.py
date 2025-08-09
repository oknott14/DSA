from collections import deque


class Solution:
    def calculate(self, s: str) -> int:
        s = s.strip()
        stack = []
        left = 0
        curr = 0
        sign = 1
        for char in s:
            if char == " ":
                continue

            elif char.isdigit():
                curr *= 10
                curr += ord(char) - ord("0")
            elif char == "-" or char == "+":
                left += sign * curr
                curr = 0
                sign = 1 if char == "+" else -1
            elif char == "(":
                stack.append(left)
                stack.append(sign)
                left = 0
                curr = 0
                sign = 1
            else:  # char == )
                left += sign * curr
                left *= stack.pop()  # multiply by sign
                left = stack.pop() + left
                curr = 0
                sign = 1

        left += sign * curr
        return left

    # Beats 16% o(n)
    def calculate_slow(self, s: str) -> int:
        s = s.strip()
        ints = set(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
        queue = deque()
        idx = 0

        def add(x: int):
            return lambda y: x + y

        def sub(x: int):
            return lambda y: x - y

        left = add(0)
        right = 0

        while idx < len(s):
            if s[idx] == " ":
                idx += 1
                continue
            elif s[idx] in ints:
                right *= 10
                right += int(s[idx])
            elif s[idx] == "(":
                queue.append(left)
                left = add(0)
                right = 0
            elif s[idx] == ")":
                right = left(right)
                left = queue.pop()
            else:
                right = left(right)

                if s[idx] == "+":
                    left = add(right)

                elif s[idx] == "-":
                    left = sub(right)
                right = 0
            idx += 1
        return left(right)


soln = Solution()


def test_case_1():
    assert soln.calculate("1 + 1") == 2


def test_case_2():
    assert soln.calculate("2-1 + 2") == 3


def test_case_3():
    assert soln.calculate("(1+(4+5+2)-3)+(6+8)") == 23


def test_basic_add():
    assert soln.calculate("2 + 10") == 12


def test_basic_sub():
    assert soln.calculate("100 - 40") == 60


def test_basic_parens():
    assert soln.calculate("1 + (3 - 2)") == 2


def test_multi_parens():
    assert soln.calculate("(1 + 2) + (2 - 3)") == 2


def test_paren_to_negative():
    assert soln.calculate("1 + (-1 + 1)") == 1


def test_double_negative():
    assert soln.calculate("1 -(-1)") == 2
