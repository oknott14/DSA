from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sCount = Counter(s)
        tCount = Counter(t)

        for char, count in sCount.items():
            if count != tCount[char]:
                return False
            
        return True


soln = Solution()


def test_case_1():
    s = "anagram"
    t = "nagaram"
    assert soln.isAnagram(s, t)


def test_case_2():
    s = "rat"
    t = "car"
    assert not soln.isAnagram(s, t)
