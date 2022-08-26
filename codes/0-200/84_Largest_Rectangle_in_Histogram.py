class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # maintain an increasing monotonic stack, when a smaller height comes, pop idx from stack
        # all the other height popped out is higher than the pivot one
        stack = []
        res = 0
        heights += [-1]
        for i in range(len(heights)):
            height = heights[i]
            while stack and heights[stack[-1]] > height:
                idx = stack.pop()
                tmp_height = heights[idx]
                # if there is still an element in stack, it always higher than pivot one
                if stack:
                    tmp_width = i - stack[-1] - 1
                # if stack is empty, all values on left side are bigger than pivot
                else:
                    tmp_width = i
                res = max(res, tmp_height * tmp_width)
            stack.append(i)
        return res