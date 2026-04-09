# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def merge(left_head: ListNode, right_head: ListNode) -> ListNode:
            dummy = ListNode(0)
            tail = dummy
            while left_head and right_head:
                if left_head.val < right_head.val:
                    tail.next = left_head
                    tail = tail.next
                    left_head = left_head.next
                else:
                    tail.next = right_head
                    tail = tail.next
                    right_head = right_head.next
            if left_head:
                tail.next = left_head
            else:
                tail.next = right_head
            return dummy.next
    
        #something
        
        if not head or not head.next:
            return head

        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        left_head = head
        right_head = slow.next
        slow.next = None

        left_head = self.sortList(left_head)
        right_head = self.sortList(right_head)

        mergedHead = merge(left_head, right_head)
        return mergedHead
        