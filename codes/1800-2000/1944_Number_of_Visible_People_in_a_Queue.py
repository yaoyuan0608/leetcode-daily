class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        # maintain a decreasing monotonic stack, when a higher person comes, all people in its left cannot see anyone anymore
        
        stack = []
        res = [0] * len(heights)
        for i in range(len(heights)):
            while stack and heights[stack[-1]] < heights[i]:
                idx = stack.pop()
                res[idx] += 1
            # each time before appending, let the last person see current person
            if stack:
                res[stack[-1]] += 1
            stack.append(i)
        return res