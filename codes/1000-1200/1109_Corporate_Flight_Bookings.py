class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        lst = []
        # same as 1094.Car Pooling, use start and end as the signal to increase or decrease the value
        for f, l, s in bookings:
            bisect.insort(lst, (f-1, s))
            bisect.insort(lst, (l, -s))
        res = [0] * n
        prefix = 0
        pre_i = 0
        # from last index to current index, add values to all index between
        for i, val in lst:
            for j in range(pre_i, i):
                res[j] += prefix
            pre_i = i
            prefix += val
        return res