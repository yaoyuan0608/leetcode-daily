# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def dfs(node, string):
            if not node:
                string += 'None '
                return string
            
            string += str(node.val) + ' '
            string = dfs(node.left, string)
            string = dfs(node.right, string)
            return string

        return dfs(root, '')
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def dedfs(q):
            if q[0] == 'None':
                q.popleft()
                return None
            else:
                root = TreeNode(q[0])
                q.popleft()
                root.left = dedfs(q)
                root.right = dedfs(q)
                return root
        
        str_list = data.split(' ')
        q = deque(str_list)
        root = dedfs(q)
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))