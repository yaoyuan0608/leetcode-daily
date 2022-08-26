class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # maintain a decreasing monotonic stack
        # pop out the idx, whose next warmer temp is the current pivot one
        stack = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            temp = temperatures[i]
            while stack and temperatures[stack[-1]] < temp:
                idx = stack.pop()
                res[idx] = i - idx
            stack.append(i)
        return res