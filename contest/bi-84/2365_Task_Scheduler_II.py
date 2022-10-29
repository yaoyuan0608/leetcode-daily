class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        rest_d = defaultdict(lambda:float('-inf'))
        count = 0
        for index, task in enumerate(tasks):
            if count - rest_d[task] < space:
                count = rest_d[task]+space
            # while count - rest_d[task] < space:
            #     count += 1
            count += 1
            rest_d[task] = count
                
        return count