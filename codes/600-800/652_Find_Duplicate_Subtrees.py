# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, node):
        if not node:
            return '#'
        # string concatenate requires o(n) time complexity, so o(n2) in total
        string = str(node.val) + '#' + self.helper(node.left) + '#' + self.helper(node.right)
        self.node_map[string] += 1
        if self.node_map[string] == 2:
            self.res.append(node)
        return string
    
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        # post-order traversal, use a map to store all substree
        self.node_map = defaultdict(int)
        self.res = []
        self.helper(root)
        return self.res