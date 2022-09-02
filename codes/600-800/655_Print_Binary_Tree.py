# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_depth(self, node):
        if not node:
            return 0
        left = self.get_depth(node.left)
        right = self.get_depth(node.right)
        return max(left, right) + 1
    
    def print_tree(self, node, r, c):
        if not node:
            return
        self.matrix[r][c] = str(node.val)
        self.print_tree(node.left, r+1, c-pow(2,self.depth-r-2))
        self.print_tree(node.right, r+1, c+pow(2,self.depth-r-2))
        
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        # get the height and matrix first
        self.depth = self.get_depth(root)
        n = pow(2, self.depth)-1
        self.matrix = [[""] * n for _ in range(self.depth)]
        self.print_tree(root, 0, (n-1)//2)
        return self.matrix