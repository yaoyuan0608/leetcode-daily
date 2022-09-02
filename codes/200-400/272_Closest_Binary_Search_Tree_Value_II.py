# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, node):
        if not node:
            return
        self.helper(node.left)
        if len(self.res) < self.k:
            self.res.append(node.val)
            self.helper(node.right)
        else:
            if abs(node.val - self.target) < abs(self.res[0] - self.target):
                self.res.popleft()
                self.res.append(node.val)
                self.helper(node.right)
        
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        # inorder trasversalm, maintain a stack with length of k
        # if abs(node.val - target) < abs(stack[0] - target), traversal on right
        self.res = deque([])
        self.target = target
        self.k = k
        self.helper(root)
        return self.res