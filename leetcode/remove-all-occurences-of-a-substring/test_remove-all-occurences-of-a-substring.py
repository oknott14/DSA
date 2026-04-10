class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = ""
        index = 0
        while index < len(s):
            stack = stack + s[index]
            while stack.endswith(part):
                stack = stack.removesuffix(part)
            index += 1
        return stack


soln = Solution()


def test_case_1():
    assert soln.removeOccurrences(s="daabcbaabcbc", part="abc") == "dab"


def test_case_2():
    assert soln.removeOccurrences(s="axxxxyyyyb", part="xy") == "ab"


def test_part_longer_than_s():
    assert soln.removeOccurrences("a", "abc") == "a"


def test_part_not_in_s():
    assert soln.removeOccurrences("abc", "d") == "abc"


def test_part_only_once():
    assert soln.removeOccurrences("aaaaaaaaaaaabc", "abc") == "aaaaaaaaaaa"


def test_full_removal():
    assert soln.removeOccurrences("aaaaaabbbbbb", "ab") == ""


def test_remove_two_in_row():
    assert soln.removeOccurrences("abcabc", "abc") == ""


def test_case_3():
    assert (
        soln.removeOccurrences(
            s="rrrzokrrrzoktbgnlerpstimuatbgnlerpstimuagdgtmfy",
            part="rrrzoktbgnlerpstimua",
        )
        == "gdgtmfy"
    )


def test_case_55():
    assert (
        soln.removeOccurrences(
            "kirkirkirpgpgpkirpgkirkirpgkirpgkikikirpgrpgrkirpkirpgkirpggpgpkikirpgrkirkirpgpgpggkikirpgrpggkirpgbkirpgthytpyimz",
            "kirpg",
        )
        == "bthytpyimz"
    )
