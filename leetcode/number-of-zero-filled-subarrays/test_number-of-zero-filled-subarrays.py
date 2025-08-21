from typing import List


# 25ms beats 90%
def zeroFilledSubarray(nums: List[int]) -> int:
    total = 0
    consecutive = 0

    for num in nums:
        if num == 0:
            consecutive += 1
            total += consecutive
        else:
            consecutive = 0

    return total


# 35ms beats 53%
def zeroFilledSubarray1(nums: List[int]) -> int:
    num_subarrays = 0
    consecutive_zeros = 0

    for num in nums:
        if num == 0:
            consecutive_zeros += 1
        else:
            num_subarrays += (consecutive_zeros * (consecutive_zeros + 1)) // 2
            consecutive_zeros = 0
    num_subarrays += (consecutive_zeros * (consecutive_zeros + 1)) // 2
    return num_subarrays


def test_single_zero():
    assert zeroFilledSubarray([0]) == 1
    assert zeroFilledSubarray([1, 0, 1]) == 1


def test_no_zero():
    assert zeroFilledSubarray([1, 2, 3]) == 0
    assert zeroFilledSubarray([]) == 0


def test_two_zero():
    assert zeroFilledSubarray([0, 0]) == 3
    # 0 x 2
    # 00 x 1


def test_three_zero():
    assert zeroFilledSubarray([0, 0, 0]) == 6
    # 0 x 3
    # 00 x 2
    # 000 x 1


def test_four_zero():
    assert zeroFilledSubarray([0, 0, 0, 0]) == 10
    # 0 x 4
    # 00 x 3
    # 000 x 2
    # 0000 x 1
