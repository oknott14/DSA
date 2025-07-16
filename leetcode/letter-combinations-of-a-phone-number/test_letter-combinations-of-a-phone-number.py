from string import ascii_lowercase
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)

        if n == 0:
            return []

        def get_len(digit: int):
            return 3 if digit != 7 and digit != 9 else 4

        def get_position(digit: int):
            if digit <= 7:
                return 3 * (digit - 2)
            else:
                return 19 + (digit - 8) * 3

        letters = list(ascii_lowercase)
        positions = [0] * n
        divisors = [0] * n
        lens = [0] * n
        num_combinations = 1
        divisor = 1
        for idx in range(1, n + 1):
            digit = int(digits[n - idx])
            lens[n - idx] = get_len(digit)
            num_combinations *= lens[n - idx]
            positions[n - idx] = get_position(digit)
            divisors[n - idx] = divisor
            divisor *= get_len(digit)

        combinations = [""] * num_combinations
        for idx in range(len(combinations)):
            for d_idx in range(n):
                combinations[idx] += letters[
                    positions[d_idx] + (idx // divisors[d_idx]) % lens[d_idx]
                ]
        return combinations


soln = Solution()


def test_case_1():
    digits = "23"
    output = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    assert soln.letterCombinations(digits) == output


def test_empty():
    digits = ""
    output = []
    assert soln.letterCombinations(digits) == output


def test_7():
    assert soln.letterCombinations("7") == ["p", "q", "r", "s"]


def test_with_7():
    assert soln.letterCombinations("273") == [
        "apd",
        "ape",
        "apf",
        "aqd",
        "aqe",
        "aqf",
        "ard",
        "are",
        "arf",
        "asd",
        "ase",
        "asf",
        "bpd",
        "bpe",
        "bpf",
        "bqd",
        "bqe",
        "bqf",
        "brd",
        "bre",
        "brf",
        "bsd",
        "bse",
        "bsf",
        "cpd",
        "cpe",
        "cpf",
        "cqd",
        "cqe",
        "cqf",
        "crd",
        "cre",
        "crf",
        "csd",
        "cse",
        "csf",
    ]

def test_nums():
    assert '88' < '99'
    assert '88' < '89'