class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text2) < len(text1):
            text1, text2 = text2, text1

        lens = [0] * len(text1)
        longest = 0

        for char in text2:
            max_before = 0

            for i in range(len(lens)):
                if max_before < lens[i]:
                    max_before = lens[i]
                elif text1[i] == char:
                    lens[i] = 1 + max_before

                    longest = max(longest, lens[i])
        return longest


soln = Solution()


def test_case_1():
    text1 = "abcde"
    text2 = "ace"
    assert soln.longestCommonSubsequence(text1, text2) == 3
    assert soln.longestCommonSubsequence(text2, text1) == 3


def test_case_2():
    text1 = "abc"
    text2 = "abc"
    assert soln.longestCommonSubsequence(text1, text2) == 3
    assert soln.longestCommonSubsequence(text2, text1) == 3


def test_case_3():
    text1 = "abc"
    text2 = "def"
    assert soln.longestCommonSubsequence(text1, text2) == 0
    assert soln.longestCommonSubsequence(text2, text1) == 0


def test_finds_sub_at_pg1():
    text1 = "abacadaeaf"
    text2 = "fescbcdef"
    assert soln.longestCommonSubsequence(text1, text2) == 5


def test_finds_longest_sub_when_there_are_2():
    text1 = "abczzzzefsdtabcdef"
    text2 = "abcdefzzef"
    assert soln.longestCommonSubsequence(text1, text2) == 7


def test_cannot_find_reversed_sub():
    text1 = "abcdef"
    text2 = text1[::-1]
    assert soln.longestCommonSubsequence(text1, text2)
