# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # bfs, use a deque to store the node and its index 
        # for right and left child, their indexes: 2*index+1, 2*index+2
        res = 0
        q = deque([])
        if not root:
            return res
        q.append((root,0))
        while q:
            tmp_left = float('inf')
            tmp_right = float('-inf')
            for _ in range(len(q)):
                node, idx = q.popleft()
                tmp_left = min(tmp_left, idx)
                tmp_right = max(tmp_right, idx)    
                res = max(res, tmp_right - tmp_left + 1)
                if node.left:
                    q.append((node.left, 2*idx+1))
                if node.right:
                    q.append((node.right, 2*idx+2))
        return res