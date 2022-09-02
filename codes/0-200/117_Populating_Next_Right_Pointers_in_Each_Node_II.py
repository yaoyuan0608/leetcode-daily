"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # curr: current node, head: head of next level, tail: tail of next level
        # iterate level by level, if curr, move to next level, 
        # check the left and right childs of curr, update head and tail accordingly
        curr = root
        head = tail = None
        while curr:
            if curr.left:
                if not head:
                    head = curr.left
                if not tail:
                    tail = curr.left
                else:
                    tail.next = curr.left
                    tail = tail.next
            if curr.right:
                if not head:
                    head = curr.right
                if not tail:
                    tail = curr.right
                else:
                    tail.next = curr.right
                    tail = tail.next
            curr = curr.next
            if not curr:
                curr = head
                head = tail = None
        return root