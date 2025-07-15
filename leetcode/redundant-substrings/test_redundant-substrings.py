def redundant_substrings(s: str, a: int, b: int) -> int:
    vowels = set(["a", "e", "i", "o", "u"])
    V = 0
    C = 0
    v = 0
    c = 0

    if s[0] in vowels:
        V += 1
    else:
        C += 1

    substrings = 0
    for right in range(1, len(s)):
        if s[right] in vowels:
            V += 1
            if a == 1:
                substrings += 1
        else:
            C += 1
            if b == 1:
                substrings += 1
        v = V
        c = C
        for left in range(right):
            sub = s[left : right + 1]
            if a * v + b * c == 1 + right - left:
                # print(f"{s[left : right + 1]} | {v} | {c} | {1 + right - left}")
                substrings += 1

            if s[left] in vowels:
                v -= 1
            else:
                c -= 1
    return substrings


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
    assert redundant_substrings(word, a, b) == 20


def test_both_positive():
    word = "ababab"
    a = 1
    b = 1

    assert redundant_substrings(word, a, b) == 14


def test_negative_equal():
    word = "ababab"
    a = 1
    b = 1
