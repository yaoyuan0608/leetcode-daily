# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findClosestLeaf(self, root: Optional[TreeNode], k: int) -> int:
        # convert it to a graph problem, and do bfs until find the leaf node
        graph = defaultdict(list)
        leaves = set()
        def dfs(node):
            if not node:
                return
            if not node.left and not node.right:
                leaves.add(node.val)
                return
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                dfs(node.left)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                dfs(node.right)
        
        dfs(root)
        
        q = deque([k])
        seen = set()
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node in seen:
                    continue
                if node in leaves:
                    return node
                seen.add(node)
                q.extend(graph[node])