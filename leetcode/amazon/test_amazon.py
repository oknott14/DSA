from typing import List


def getMaxServers(powers: List[int]):
    if len(powers) < 2:
        return 1 if abs(powers[0] - powers[1]) > 1 else 2

    powers = sorted(powers)
    max_servers = 0
    start = 0
    idx = 2
    while idx < len(powers):
        diff = powers[idx] - powers[idx - 2]
        if 1 < diff:
            start = idx - 1
        max_servers = max(max_servers, 1 + idx - start)
        idx += 1
    max_servers = max(max_servers, idx - start)
    return max_servers


def test_case_1():
    assert getMaxServers([3, 7, 5, 1, 5]) == 2


def test_after():
    assert getMaxServers([2, 2, 3]) == 3


def test_case_3():
    assert getMaxServers([2, 2, 3, 2, 1, 2, 2]) == 7


def test_case_all_same():
    assert getMaxServers([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 12


def test_long():
    assert getMaxServers([1, 1, 1, 1, 2, 2, 2, 2]) == 8


def test_long_with_borders():
    assert getMaxServers([0, 1, 1, 1, 1, 2, 2, 2, 2, 3]) == 10


def test_increasing():
    assert getMaxServers([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 2
