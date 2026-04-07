# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        evenHead = head.next
        tbr = head
        while head.next and head.next.next:
            temp = head.next
            head.next = head.next.next
            nextHead = temp.next
            temp.next = temp.next.next
            head = nextHead
        head.next = evenHead
        return tbr