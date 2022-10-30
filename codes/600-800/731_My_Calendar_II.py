class MyCalendarTwo:

    def __init__(self):
        self.times = []

    def book(self, start: int, end: int) -> bool:
        self.times.append([start, 1])
        self.times.append([end, -1])
        self.times = sorted(self.times)
        book = 0
        for time in self.times:
            book += time[1]
            if book == 3:
                self.times.remove([start,1])
                self.times.remove([end,-1])
                return False
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)