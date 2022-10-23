# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, preorder, inorder):
        root = preorder[0]
        idx = inorder.index(root)
        
        left_inorder = inorder[:idx]
        right_inorder = inorder[idx+1:]
        
        left_preorder = preorder[1:1+len(left_inorder)]
        right_preorder = preorder[1+len(left_inorder):]
        
        root_node = TreeNode(root)
        if left_preorder:
            root_node.left = self.helper(left_preorder, left_inorder)
        
        if right_preorder:
            root_node.right = self.helper(right_preorder, right_inorder)
        
        return root_node
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder: root -left - right; inorder: left - root - right
        # the first element of the preorder list is the root, find the corresponding left subtree and right subtree
        return self.helper(preorder, inorder)