# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # recursive go through all nodes in tree. if node.val == key, we find the node to remove
        # find the next value to replace current node, then do the same operation on its right subtree
        if not root:
            return 
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val == key:
            # if not right sucessor
            if not root.right:
                return root.left
            else:
                tmp = root.right
                while tmp.left:
                    tmp = tmp.left
                root.val = tmp.val
                root.right = self.deleteNode(root.right, tmp.val)
        return root