class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        # starting from right to left, maintain an increasing monotonic stack
        # if the current idx has the largest height so far, it has ocean view
        stack = []
        res = []
        for i in range(len(heights)-1, -1, -1):
            height = heights[i]
            while stack and heights[stack[-1]] < height:
                stack.pop()
            if not stack:
                res.append(i)
            stack.append(i)
        return res[::-1]