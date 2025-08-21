# Amazon loads content to the front end based on various schedules.
# Write a method to determine the max load and time of max load for this content.

# Schedules are Tuples of (startTime, endTime)
from collections import deque
from typing import List, Tuple


def compute_max_load(schedules: List[Tuple[int, int]]) -> Tuple[int, int]:
    schedules = sorted(schedules)
    max_load_time = 0
    max_load = 0

    ends = deque()
    max_right = 0

    for start, end in schedules:
        if max_right < start:  # Interval is not overlapping with any previous
            ends.clear()
            max_right = end
            ends.append(end)
        else:
            curr = start - 1

            while curr < start and len(ends):
                curr = ends.popleft()

            if start <= curr:
                ends.appendleft(curr)

        if max_load < len(ends):
            max_load = len(ends)
            max_load_time = start
        ends.append(end)
        max_right = max(end, max_right)

    return max_load_time, max_load


def test_base_case():
    time, load = compute_max_load([(1, 2)])
    assert time == 1 or time == 2
    assert load == 1


def test_single_overlap():
    time, load = compute_max_load([(1, 2), (2, 3), (5, 6)])
    assert time == 2
    assert load == 2


def test_overlap_consumes_other():
    time, load = compute_max_load([(2, 3), (1, 4)])
    assert time == 3 or time == 2
    assert load == 2


def test_max_not_at_start_pos():
    time, load = compute_max_load([(1, 10), (1, 3), (2, 5), (2, 3), (2, 4)])
    assert time == 2
    assert load == 5
