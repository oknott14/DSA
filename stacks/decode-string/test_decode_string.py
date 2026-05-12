import re


class Solution:
    number_regex = re.compile("\d+")

    def decodeString(self, s: str) -> str:
        stack = []

        def is_number(c):

            return re.match(self.number_regex, c)

        result = ""
        for char in s:
            if is_number(char):
                if stack and is_number(stack[-1]):
                    stack[-1] += char
                else:
                    stack.append(char)  # add number to count reps
            elif char == "[":
                stack.append("")  # add empty start of repeating string
            elif char == "]":
                repeating = stack.pop()
                times = int(stack.pop())
                rep_string = ""
                for _ in range(times):
                    rep_string += repeating

                if len(stack):
                    stack[-1] += rep_string
                else:
                    result += rep_string
            elif len(stack):
                stack[-1] += char
            else:
                result += char

        return result


soln = Solution()

def test_case_1():
    assert soln.decodeString(s="3[a]2[bc]") == "aaabcbc"


def test_case_2():
    assert soln.decodeString(s="3[a2[c]]") == "accaccacc"


def test_case_3():
    assert soln.decodeString(s="2[abc]3[cd]ef") == "abcabccdcdcdef"


def test_2_digit_number():
    assert soln.decodeString("10[a]") == "".join(["a"] * 10)
