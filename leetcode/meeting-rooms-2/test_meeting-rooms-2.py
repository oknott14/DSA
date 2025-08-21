from typing import List, Tuple


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class MinHeap:
    def __init__(self):
        self.heap_arr = []

    def push(self, num: int):
        self.heap_arr.append(num)

        idx = len(self.heap_arr) - 1
        parent = idx // 2

        while 0 <= idx and self.heap_arr[idx] < self.heap_arr[parent]:
            self.heap_arr[idx], self.heap_arr[parent] = (
                self.heap_arr[parent],
                self.heap_arr[idx],
            )
            idx = parent
            parent = idx // 2

    def pop(self):
        n = len(self.heap_arr) - 1
        self.heap_arr.append(self.heap_arr[n])
        self.heap_arr[0], self.heap_arr[n] = self.heap_arr[n], self.heap_arr[0]
        n-=1
        idx = 0

        while idx < n:
            child = (
                2 * idx + 1
                if self.heap_arr[2 * idx + 1] < self.heap_arr[2 * idx + 2]
                else 2 * idx + 2
            )

            if self.heap_arr[idx] < self.heap_arr[child]:
                break

            self.heap_arr[idx], self.heap_arr[child] = (
                self.heap_arr[child],
                self.heap_arr[idx],
            )

            idx = child

        self.heap_arr.pop()
        self.heap_arr.pop()

    def length(self):
        return len(self.heap_arr)

    def head(self):
        return self.heap_arr[0]


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda interval: interval.start)
        min_heap = MinHeap()

        for interval in intervals:
            if min_heap.length() and min_heap.head() <= interval.start:
                min_heap.pop()

            min_heap.push(interval.end)

        return min_heap.length()


soln = Solution()


def build_intervals(intervals: List[Tuple]) -> List[Interval]:
    return [Interval(start, end) for start, end in intervals]


def test_case_1():
    intervals = build_intervals([(0, 40), (5, 10), (15, 20)])
    assert soln.minMeetingRooms(intervals) == 2


def test_case_2():
    intervals = build_intervals([(0, 40)])
    assert soln.minMeetingRooms(intervals) == 1


def test_case_many_overlap():
    intervals = build_intervals([(0, 2), (1, 3), (2, 4)])
    assert soln.minMeetingRooms(intervals) == 2


def test_case_3():
    intervals = build_intervals(
        [
            (25, 579),
            (218, 918),
            (1281, 1307),
            (623, 1320),
            (685, 1353),
            (1308, 1358),
        ]
    )

    assert soln.minMeetingRooms(intervals) == 3
