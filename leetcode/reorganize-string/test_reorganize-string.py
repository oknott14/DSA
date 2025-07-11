import heapq
from collections import Counter


class Solution:
    def reorganizeString(self, s: str) -> str:
        soln = [""] * len(s)

        heap = [(-count, char) for char, count in Counter(s).items()]
        heapq.heapify(heap)

        if -heap[0][0] > (len(s) + 1) // 2:
            return ""

        inserted = 0
        while heap:
            count, char = heapq.heappop(heap)
            soln[inserted] = char
            inserted += 1

            if heap:
                nxt_count, nxt_char = heapq.heappop(heap)
                soln[inserted] = nxt_char
                inserted += 1
                if nxt_count < -1:
                    heapq.heappush(heap, (nxt_count + 1, nxt_char))
            if count < -1:
                heapq.heappush(heap, (count + 1, char))

        return "".join(soln)


# import math
# from collections import Counter


# class Solution:
#     def reorganizeString(self, s: str) -> str:
#         soln = [""] * len(s)
#         char_counts = Counter(s).most_common()

#         max_char, max_count = char_counts[0]

#         if math.ceil(len(s) / 2) < max_count:
#             return ""

#         idx = 0
#         while 0 < max_count:
#             soln[idx] = max_char
#             idx += 2
#             max_count -= 1

#         for char, count in char_counts[1:]:
#             while 0 < count:
#                 if len(soln) <= idx:
#                     idx = 1

#                 soln[idx] = char
#                 idx += 2
#                 count -= 1

#         return "".join(soln)

soln = Solution()


def check_string(s: str) -> bool:
    return 0 < len(s) and not any(s[idx] == s[idx - 1] for idx in range(1, len(s)))


def test_case_1():
    assert check_string(soln.reorganizeString("aab"))


def test_unique_chars():
    assert check_string(soln.reorganizeString("abcdefg"))


def test_case_2():
    assert soln.reorganizeString("aaab") == ""


def test_case_many_replacements():
    assert check_string(soln.reorganizeString("aaabb"))


def test_replaces_diff_chars():
    assert check_string(soln.reorganizeString("aaabc"))
    assert check_string(soln.reorganizeString("aabac"))


def test_replaces_from_before():
    assert check_string(soln.reorganizeString("baa"))
    assert check_string(soln.reorganizeString("bcdaaa"))


def test_case_56():
    assert check_string(soln.reorganizeString("ogccckcwmbmxtsbmozli"))


def test_case_64():
    assert check_string(soln.reorganizeString("aabbcc"))
