# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, node, p, q):
        if not node:
            return
        if node.val == p or node.val == q:
            return node
        left = self.helper(node.left, p, q)
        right = self.helper(node.right, p, q)
        
        if left and right:
            return node
        elif left or right:
            return left or right
            
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        # the path from start to dest will pass the LCA of these two nodes
        # store the path of root -> start, root -> dest, remove the prefix before LCA
        # notice that if the paths are the same, they are common prefix
        
        # find the LCA of two nodes, then do bfs
        lca = self.helper(root, startValue, destValue)
        
        path_s, path_d = '', ''
        stack = [(lca, '')]
        while stack:
            node, string = stack.pop()
            if node.val == startValue:
                path_s = string
            if node.val == destValue:
                path_d = string
            if node.left:
                stack.append((node.left, string + 'L'))
            if node.right:
                stack.append((node.right, string + 'R'))
        
        return 'U' * len(path_s) + path_d