# idea: use stack for storing element in time order, use heap for storing element in value order
# use a set for storing values need to be removed
class MaxStack:
    # use a heap to lazy pop out the max value
    def __init__(self):
        self.hq = []
        self.stack = []
        self.total = 0
        self.remove = set()

    def push(self, x: int) -> None:
        # when two values are same, put the later one in heap
        heapq.heappush(self.hq, (-x, -self.total))
        self.stack.append((x, self.total))
        self.total += 1
        
    def pop(self) -> int:
        while self.stack and self.stack[-1][1] in self.remove:
            self.stack.pop()
        num, idx = self.stack.pop()
        self.remove.add(idx)
        return num

    def top(self) -> int:
        while self.stack and self.stack[-1][1] in self.remove:
            self.stack.pop()
        return self.stack[-1][0]

    def peekMax(self) -> int:
        while self.hq and -self.hq[0][1] in self.remove:
            heapq.heappop(self.hq)
        return -self.hq[0][0]

    def popMax(self) -> int:
        while self.hq and -self.hq[0][1] in self.remove:
            heapq.heappop(self.hq)
        num, idx = heapq.heappop(self.hq)
        self.remove.add(-idx)
        return -num
    
# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()