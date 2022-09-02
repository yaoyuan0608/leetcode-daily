# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        # need left boundary, leaf boundary and right boundary
        left = [root]
        leaf = []
        right = [root]
        
        # first to see whether the root has left boundary
        node = root.left
        while node:
            left.append(node)
            if node.left:
                node = node.left
            else:
                node = node.right
        if len(left) != 1:
            left.pop()
        # right boundary is similar to left boundary
        node = root.right
        while node:
            right.append(node)
            if node.right:
                node = node.right
            else:
                node = node.left
        if len(right) != 1:
            right.pop()
        q = deque([])
        q.append(root)
        while q:
            for _ in range(len(q)):
                node = q.pop()
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
                if not node.left and not node.right and node != root:
                    leaf.append(node)

        res = []
        for node in left + leaf + right[::-1][:-1]:
            res.append(node.val)
        return res