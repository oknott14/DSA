from collections import defaultdict


class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """

    def length_of_longest_substring_k_distinct(self, s: str, k: int) -> int:
        # write your code here
        charMap = defaultdict[str, int]()
        left = 0
        right = 0
        while right < len(s):
            charMap[s[right]] = charMap.get(s[right], 0) + 1

            if len(charMap) > k:
                charMap[s[left]] = charMap.get(s[left], 0) - 1

                if charMap.get(s[left]) == 0:
                    charMap.pop(s[left])

                left += 1

            right = right + 1

        return len(s) - left


soln = Solution()


def test_case_1():
    assert soln.length_of_longest_substring_k_distinct("aabb", 2) == 4


def test_empty_string():
    assert soln.length_of_longest_substring_k_distinct("", 100) == 0


def test_k_one():
    assert soln.length_of_longest_substring_k_distinct("aaabb", 1) == 3

def test_k_zero():
    assert soln.length_of_longest_substring_k_distinct('aaaaaa', 0) == 0

def test_longest_with_k():
    assert soln.length_of_longest_substring_k_distinct("aabacbc", 2) == 4
