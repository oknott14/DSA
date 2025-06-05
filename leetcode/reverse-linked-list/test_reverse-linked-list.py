from typing import Optional, List

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None:
      return head
    
    new_head = head
    head = head.next
    new_head.next = None

    while head:
      temp = head.next
      head.next = new_head
      new_head = head
      head = temp

    return new_head
  
  def build_list(self, arr: List[int]) -> ListNode | None:
    if len(arr) == 0:
        return None
    
    return ListNode(arr.pop(0), self.build_list(arr))
  
  def list_to_arr(self, head: Optional[ListNode]) -> List[int]:      
    node_list = []

    while head is not None:
        node_list.append(head.val)
        head = head.next
    return node_list
            

        

soln = Solution()

def test_case_1():
  input = soln.build_list([])
  output = []
  assert str(soln.list_to_arr(soln.reverseList(input))) == str(output)

def test_case_2():
  input = soln.build_list([1,2])
  output = [2,1]
  assert str(soln.list_to_arr(soln.reverseList(input))) == str(output)

def test_case_3():
  input = soln.build_list([1,2,3,4,5])
  output = [5,4,3,2,1]
  assert str(soln.list_to_arr(soln.reverseList(input))) == str(output)