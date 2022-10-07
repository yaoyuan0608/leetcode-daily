# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        # do bfs level by level, from right to left
        # 1. for one node, if its child has right node, which is visited, set node.left/node.right to None
        # 2. else, continue right to left
        
        q = deque([])
        q.append(root)
        seen = set(q)
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node.right:
                    if node.right.right and node.right.right in seen:
                        node.right = None
                        return root
                    q.append(node.right)
                    seen.add(node.right)
                if node.left:
                    if node.left.right and node.left.right in seen:
                        node.left = None
                        return root
                    q.append(node.left)
                    seen.add(node.left)
        return root