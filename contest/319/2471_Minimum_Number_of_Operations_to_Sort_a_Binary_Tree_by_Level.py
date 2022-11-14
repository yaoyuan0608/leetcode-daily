# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverse(self, arr):
        pos = []
        for idx, val in enumerate(arr):
            pos.append((idx,val))
        pos = sorted(pos, key=lambda x : x[1])
        visited = {k : False for k in range(len(arr))}

        count = 0
        for i in range(len(pos)):
            if visited[i] or pos[i][0] == i:
                continue
            cycle_size = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = pos[j][0]
                cycle_size += 1

            if cycle_size > 0:
                count += (cycle_size - 1)
        return count
    
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        q = deque([])
        res = 0
        if not root:
            return res
        q.append(root)
        while q:
            tmp = []
            for _ in range(len(q)):
                node = q.popleft()
                tmp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            #print(tmp)
            val = self.reverse(tmp)
            res += val
            #print(val)
        return res