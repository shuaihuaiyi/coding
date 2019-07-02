# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
  def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    p1 = head
    p2 = head
    for i in range(n):
      if p2 is None:
        raise ValueError
      p2 = p2.next
    if p2 is None:
      return head.next
    while p2.next is not None:
      p1 = p1.next
      p2 = p2.next
    p1.next = p1.next.next
    return head
