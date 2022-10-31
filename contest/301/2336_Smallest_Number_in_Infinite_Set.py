class SmallestInfiniteSet:

    def __init__(self):
        self.curr = 1
        self.q = []
    def popSmallest(self) -> int:
        if not self.q:
            res = self.curr
            self.curr += 1
            return res
        else:
            res = heapq.heappop(self.q)
            return res
    def addBack(self, num: int) -> None:
        if num >= self.curr:
            return
        else:
            if num not in self.q:
                heapq.heappush(self.q, num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)