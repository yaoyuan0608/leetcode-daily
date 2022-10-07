# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumFlips(self, root: Optional[TreeNode], result: bool) -> int:
        # tree dp dfs(node, target): minimum operation to make node as target
        self.memo = {}
        @cache
        def dp(node, target):
            if not node:
                return
            if not node.right and not node.left:
                return int(node.val != target)
            if node in self.memo and target in self.memo[node]:
                return self.memo[node][target]
            
            res = float('inf')
            # OR operation
            if node.val == 2:
                if target == 1:
                    res = min(res, dp(node.left, 1))
                    res = min(res, dp(node.right, 1))
                elif target == 0:
                    res = min(res, dp(node.left,0) + dp(node.right,0))
            # AND operation
            elif node.val == 3:
                if target == 1:
                    res = min(res, dp(node.left,1) + dp(node.right,1))
                elif target == 0:
                    res = min(res, dp(node.left,0))
                    res = min(res, dp(node.right,0))
            # XOR operation
            elif node.val == 4:
                if target == 1:
                    res = min(res, dp(node.left,1) + dp(node.right,0))
                    res = min(res, dp(node.left,0) + dp(node.right,1))
                elif target == 0:
                    res = min(res, dp(node.left,0) + dp(node.right,0))
                    res = min(res, dp(node.left,1) + dp(node.right,1))
            # NOT operation
            elif node.val == 5:
                if node.left:
                    if target == 1:
                        res = min(res, dp(node.left, 0))
                    elif target == 0:
                        res = min(res, dp(node.left, 1))
                elif node.right:
                    if target == 1:
                        res = min(res, dp(node.right, 0))
                    elif target == 0:
                        res = min(res, dp(node.right, 1))
            self.memo[node] = {}
            self.memo[node][target] = res
            return res
        return dp(root, result)