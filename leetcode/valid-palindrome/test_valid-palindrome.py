class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
        ans = "".join([ch for ch in s.lower() if ch in alpha])

        left = 0
        right = len(ans) - 1

        while left < right:
            if ans[left] != ans[right]:
                return False

            left += 1
            right -= 1

        return True


soln = Solution()


def test_case_1():
    assert soln.isPalindrome("A man, a plan, a canal: Panama")


def test_case_2():
    assert not soln.isPalindrome("race a car")


def test_case_3():
    assert soln.isPalindrome(" ")


def test_case_4():
    assert soln.isPalindrome("race car")


def test_all_replaceable():
    assert soln.isPalindrome("!@#$%^&*(),./<>?;:'\"[{}]-_=+\|`~ ")


def test_single_num_single_char():
    assert not soln.isPalindrome("0P")
