# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, cur):
        root = TreeNode(self.nodes[cur][0])
        count = 1
        left_size = 0
        right_size = 0
        # if the next node has a deeper depth, do recursion on left tree
        # the return type is the left node and size of left tree
        if cur+1 < len(self.nodes) and self.nodes[cur+1][1] == self.nodes[cur][1] + 1:
            left_node, left_size = self.dfs(cur+1)
            root.left = left_node
        if cur+left_size+1 < len(self.nodes) and self.nodes[cur+left_size+1][1] == self.nodes[cur][1] + 1:
            right_node, right_size = self.dfs(cur+left_size+1)
            root.right = right_node
            
        count += left_size + right_size
        return root, count
        
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        # create the nodes list with their depths
        nodes = []
        i = 0
        while i < (len(traversal)):
            start = i
            while start < len(traversal) and traversal[start] == '-':
                start += 1
            depth = start - i
            i = start
            while start < len(traversal) and traversal[start].isdigit():
                start += 1
            
            value = int(traversal[i:start])
            nodes.append((value, max(depth,0)))
            i = start
            
        self.nodes = nodes
        return self.dfs(0)[0]
        