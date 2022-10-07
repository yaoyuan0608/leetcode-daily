class TreeNode:
    def __init__(self, val):
        # k,v: <child.val, childNode>
        self.children = defaultdict(TreeNode)
        self.val = val
class Solution:
    def getid(self, node):
        # generate the id for each node
        if not node:
            return 0
        string = ''
        for child in sorted(node.children):
            child_node = node.children[child]
            string += str(self.getid(child_node)) + '#' + str(child) + '#'
        # no need to include the value of current node
        self.node2key[node] = string
        self.key2count[string] += 1
        if self.key2count[string] == 1:
            self.key2id[string] = len(self.key2id) + 1
            
        return self.key2id[string]
    
    def dfs(self, node, path):
        # extract the hash string of current node, if >=2, skip this node
        string = self.node2key[node]
        if string != '' and self.key2count[string] >= 2:
            return
        # if not root, append to result
        if node.val != '/':
            path.append(node.val)
            self.res.append(path[:])
            
        for child in sorted(node.children):
            child_node = node.children[child]
            self.dfs(child_node, path)
        if node.val != '/':
            path.pop()
    
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        # similar to 652, we can use a hash string to represent all files under this folder
        # key2id: map the hash string to an id, key2count: number of duplicated hash string
        # node2key: map the node to key
        self.key2id = defaultdict(int)
        self.key2count = defaultdict(int)
        self.node2key = defaultdict(str)
        self.res = []
        
        # create a tree(trie) first
        root = TreeNode('/')
        for path in paths:
            node = root
            for s in path:
                if s not in node.children:
                    node.children[s] = TreeNode(s)
                node = node.children[s]
        
        self.getid(root)
        self.dfs(root, [])
        return self.res