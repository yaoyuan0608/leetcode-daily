# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
    
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        def helper(node, depth):
            if not node:
                return -1
            depth_tree[node.val] = depth
            cur = max(helper(node.left, depth+1), helper(node.right, depth+1)) + 1
            height_tree[node.val] = cur
            return cur
        
        depth_tree = defaultdict(int)
        height_tree = defaultdict(int)
        
        helper(root, 0)
        # group the nodes that has the same depth, and save their heights
        level = {}
        for node, depth in depth_tree.items():
            if depth not in level:
                level[depth] = []
            heapq.heappush(level[depth], (-height_tree[node], node))
        
        res = []
        for q in queries:
            depth = depth_tree[q]
            # maximum depth node
            if len(level[depth]) == 1:
                res.append(depth - 1)
            elif level[depth][0][1] == q:
                # find the node with second maximum height
                tmp = heapq.heappop(level[depth])
                res.append(-level[depth][0][0] + depth)
                heapq.heappush(level[depth], tmp)
            else:
                res.append(-level[depth][0][0] + depth)
        return res