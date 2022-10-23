# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, inorder_list, postorder_list):
        root_val = postorder_list[-1]
        idx = inorder_list.index(root_val)
        left_inorder, right_inorder = inorder_list[:idx], inorder_list[idx+1:]
        left_postorder, right_postorder = postorder_list[:len(left_inorder)], postorder_list[len(left_inorder): len(left_inorder)+len(right_inorder)]
        root = TreeNode(root_val)
        if left_inorder:
            root.left = self.helper(left_inorder, left_postorder)
        if right_inorder:
            root.right = self.helper(right_inorder, right_postorder)
        return root
    
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # inorder: left - root - right, postorder: left - right - root
        # the last value in postorder is the node, do it recursively
        return self.helper(inorder, postorder)