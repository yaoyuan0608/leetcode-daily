# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        def dfs(node, string):
            if not node:
                string += '# '
                return string
            string += str(node.val) + ' '
            string = dfs(node.left, string)
            string = dfs(node.right, string)
            return string
        return dfs(root, '')

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        def dedfs(q):
            if not q:
                return 
            if q[0] == '#':
                q.popleft()
                return None
            else:
                root = TreeNode(q.popleft())
                root.left = dedfs(q)
                root.right = dedfs(q)
                return root
        str_list = data.split(' ')
        q = deque(str_list)
        return dedfs(q)
    
# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
# use the idea of preorder sort, each element on top of a queue is the root