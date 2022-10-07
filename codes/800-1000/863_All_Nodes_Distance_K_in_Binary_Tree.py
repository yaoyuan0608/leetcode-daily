# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # create a graph first, and do bfs from target
        graph = defaultdict(list)
        def dfs(node):
            if not node:
                return 
            if node.left:
                graph[node.left].append(node)
                graph[node].append(node.left)
                dfs(node.left)
            if node.right:
                graph[node.right].append(node)
                graph[node].append(node.right)
                dfs(node.right)
        dfs(root)
        q = deque([])
        q.append((target, None, 0))
        res = []
        while q:

            node, parent, dist = q.popleft()
            if dist == k:
                res.append(node.val)
            if dist > k:
                break
            for child in graph[node]:
                if child != parent:
                    q.append((child, node, dist+1))
        return res