from typing import List


def countGroups(related: List[str]):
    # Write your code here

    m = len(related)
    groups = 0
    visited = set()

    for i in range(m):
        if i not in visited:
            groups += 1
            visited.add(i)
        for gifted_from in range(m):
            if related[i][gifted_from] == "1":
                visited.add(gifted_from)
    return groups


def test_case_no_gifts():
    related = ['1000', '0100', '0010', '0001']
    assert countGroups(related) == 4

def test_case_far_gift():
    related = [
        '110001',
        '111000',
        '011100',
        '001100',
        '000010',
        '100001'
    ]
    assert countGroups(related) == 2