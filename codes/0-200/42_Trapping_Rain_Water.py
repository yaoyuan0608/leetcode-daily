class Solution:
    def trap(self, height: List[int]) -> int:
        # water can be contained between two walls, it is called wall if current height is higher than preivous
        # maintain a non-decreasing monotonic stack, when a higher wall comes, pop out an index, it will be used as the height
        # the last wall in the stack will be used as the width
        # at the beginning of each while loop, 
        stack = []
        count = 0
        for i in range(len(height)):
            h = height[i]
            while stack and height[stack[-1]] <= h:
                last_idx = stack.pop()
                last_h = height[last_idx]
                if stack:
                    width_idx = stack[-1]
                    width = i - width_idx - 1
                    count += width * (min(h, height[width_idx]) - last_h)
            stack.append(i)
        return count