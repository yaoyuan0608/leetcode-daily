"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
#         # store the path from p to root, q to root, and find the last common node
#         path_p = []
#         while p:
#             path_p.append(p)
#             p = p.parent
#         path_q = []
#         while q:
#             path_q.append(q)
#             q = q.parent
        
#         path_p = path_p[::-1]
#         path_q = path_q[::-1]
#         idx = 0

#         while idx < min(len(path_p), len(path_q)):
#             if path_p[idx].val != path_q[idx].val:
#                 return path_p[idx-1]
#             idx += 1
#         return path_p[idx-1]
        # use two pointer
        p1 = p
        p2 = q
        while p1 != p2:
            # if p1 reach the end, move p1 to q
            if p1.parent:
                p1 = p1.parent
            else:
                p1 = q
            
            if p2.parent:
                p2 = p2.parent
            else:
                p2 = p
        return p1