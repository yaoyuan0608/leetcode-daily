# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # root->right, right->left, left->root
        curr = root
        tmp = None
        prev = None
        nex = None
        while curr:
            nex = curr.left
            curr.left = tmp
            tmp = curr.right
            curr.right = prev
            
            prev = curr
            curr = nex
        return prev
# a nice reference: https://leetcode.com/problems/binary-tree-upside-down/discuss/49406/Java-recursive-(O(logn)-space)-and-iterative-solutions-(O(1)-space)-with-explanation-and-figure