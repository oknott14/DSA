from collections import defaultdict


def redundant_substrings(word: str, a: int, b: int) -> int:
    vowels = set(["a", "e", "i", "o", "u"])
    prefix_map = defaultdict(int)

    prefix_map[0] = 1

    vowel_count = 0
    consonant_count = 0
    result = 0

    for i in range(len(word)):
        if word[i] in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

        sig = (i + 1) - a * vowel_count - b * consonant_count

        result += prefix_map[sig]
        prefix_map[sig] += 1
    return result


def test_case_1():
    word = "abbacc"
    a = -1
    b = 2
    output = 5

    assert redundant_substrings(word, a, b) == output


def test_case_3():
    word = "akljfs"
    a = -2
    b = 1
    assert redundant_substrings(word, a, b) == 15


def test_both_positive():
    word = "ababab"
    a = 1
    b = 1

    assert redundant_substrings(word, a, b) == 21
