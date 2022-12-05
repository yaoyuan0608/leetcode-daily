# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # reverse the node first
        # from (new) start to end, delete all nodes smaller than current maximum
        # reverse back
        def reverse(head):
            cur = head
            pre, nex = None, None
            while cur:
                nex = cur.next
                cur.next = pre
                pre = cur
                cur = nex
            head = pre
            return head
        def remove(head):
            cur = head
            maximum = head.val
            while cur and cur.next:
                if cur.next.val < maximum:
                    cur.next = cur.next.next
                else:
                    maximum = cur.next.val
                    cur = cur.next
            return head
        
        head = reverse(head)
        head = remove(head)
        head = reverse(head)
        return head