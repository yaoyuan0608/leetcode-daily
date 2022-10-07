# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_value(self, node):
        if not node:
            return
        self.val_count[node.val] += 1
        self.get_value(node.left)
        self.get_value(node.right)
    
    def helper(self, node, maximum, minimum):
        if not node:
            return True
        if node.val > maximum or node.val < minimum:
            return False
        # if the node is not leaf
        if node.left or node.right:
            return self.helper(node.left, node.val-1, minimum) and self.helper(node.right, maximum, node.val+1)
        elif node.val in self.root_dict and node.val not in self.visited:
            new_node = self.root_dict[node.val][0]
            self.visited.add(new_node)
            node.left = new_node.left
            node.right = new_node.right
            return self.helper(node.left, node.val-1, minimum) and self.helper(node.right, maximum, node.val+1)
        return True
    
    def canMerge(self, trees: List[TreeNode]) -> Optional[TreeNode]:
        # no two leaf nodes are the same -> the final root value is unique at all original trees
        # as all nodes are unique, so when ecounter a leaf as one of the root, we need to merge it to our tree
        # every time we merge a subtree, need to verify the value of its nodes, do preorder traversal
        
        # key: root val, value: idx
        self.root_dict = defaultdict(list)
        # occurance of each node value
        self.val_count = defaultdict(int)
        for idx, tree in enumerate(trees):
            self.root_dict[tree.val].append(tree)
            self.get_value(tree)

        count = 0
        root = None
        for key in self.root_dict:
            if self.val_count[key] == 1:
                root = self.root_dict[key][0]
                count += 1
        if count > 1 or not root:
            return None
        self.visited = set()
        self.visited.add(root.val)
        flag = self.helper(root, float('inf'), float('-inf'))
        if flag and len(self.visited) == len(trees):
            return root
        else:
            return None