class MyCalendarThree:

    def __init__(self):
        self.times = []

    def book(self, start: int, end: int) -> int:
        self.times.append([start,1])
        self.times.append([end,-1])
        self.times = sorted(self.times)
        book = 0
        cur = 0
        for time in self.times:
            cur += time[1]
            book = max(book, cur)
        return book


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)