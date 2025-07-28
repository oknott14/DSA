from typing import List, Optional, Tuple


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None

        end = head
        group = 0

        while group < k and end is not None:
            end = end.next
            group += 1

        start = ListNode(0, head)
        curr_start = start

        def reverse_to(
            start: ListNode, end: Optional[ListNode]
        ) -> Tuple[Optional[ListNode], Optional[ListNode], int]:
            curr = start.next
            nxt = end
            reversed = 0
            while curr.next is not None and curr.next != end:  # type: ignore
                temp = curr.next
                curr.next = curr.next.next
                temp.next = curr_start.next
                curr_start.next = temp

                if nxt is not None:
                    nxt = nxt.next
                    reversed += 1
            if nxt is not None:
                nxt = nxt.next
                reversed += 1
            return (curr, nxt, reversed)

        while end is not None:
            curr_start, end, group = reverse_to(curr_start, end)

        if group == k:
            reverse_to(curr_start, end)

        return start.next


def build_list(lst: List[int]) -> Optional[ListNode]:
    if len(lst) == 0:
        return None

    head = ListNode(lst[0])
    curr = head
    for val in lst[1:]:
        curr.next = ListNode(val)
        curr = curr.next

    return head


def unbuild_list(head: Optional[ListNode]):
    lst = []

    while head is not None:
        lst.append(head.val)
        head = head.next

    return lst


soln = Solution()


def test_case_1():
    lst = build_list([1, 2, 3, 4, 5])
    k = 2
    assert unbuild_list(soln.reverseKGroup(lst, k)) == [2, 1, 4, 3, 5]


def test_case_2():
    lst = build_list([1, 2, 3, 4, 5])
    k = 3
    assert unbuild_list(soln.reverseKGroup(lst, k)) == [3, 2, 1, 4, 5]


def test_length_is_k():
    lst = build_list([1, 2])
    k = 2
    assert unbuild_list(soln.reverseKGroup(lst, k)) == [2, 1]


def test_length_multiple_of_k():
    lst = build_list([1, 2, 3, 4])
    k = 2
    assert unbuild_list(soln.reverseKGroup(lst, k)) == [2, 1, 4, 3]


def test_length_is_below_k():
    lst = build_list([1, 2])
    k = 5
    assert unbuild_list(soln.reverseKGroup(lst, k)) == [1, 2]