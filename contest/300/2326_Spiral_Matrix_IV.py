# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        res = [[-1] * n for _ in range(m)]
        x, y = 0, 0
        direct = 0
        while head:
            res[x][y] = head.val
            head = head.next
            if direct%4 == 0:
                y += 1
                if y >= n or res[x][y] != -1:
                    y -= 1
                    x += 1
                    direct += 1
            elif direct%4 == 1:
                x += 1
                if x >= m or res[x][y] != -1:
                    x -= 1
                    y -= 1
                    direct += 1
            elif direct%4 == 2:
                y -= 1
                if y < 0 or res[x][y] != -1:
                    y += 1
                    x -= 1
                    direct += 1
            elif direct%4 == 3:
                x -= 1
                if x < 0 or res[x][y] != -1:
                    x += 1
                    y += 1
                    direct += 1
        return res