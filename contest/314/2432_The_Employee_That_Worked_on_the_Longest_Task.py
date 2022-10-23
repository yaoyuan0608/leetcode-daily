class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        start = 0
        time = defaultdict(int)
        for iid, end in logs:
            length = end - start
            if length not in time:
                time[length] = iid
            else:
                time[length] = min(iid, time[length])
            start = end
        #print(time)
        maximum = max(time.keys())
        return time[maximum]