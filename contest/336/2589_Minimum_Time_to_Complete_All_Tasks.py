class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        candidate = []
        count = 0
        active = defaultdict(list)

        for i, (start,end,duration) in enumerate(tasks):    
            candidate += [(start,0,duration,i), (end,1,duration,i)]
        
        candidate = sorted(candidate)
        #print(sorted(stack))
        for time, d, duration,i in candidate:
            # if it is starting point
            if 1-d:
                active[i] = [time, duration]
            # if it is ending point, close task i
            else:              
                un_used = active[i][1]
                count += un_used
                # update all the other task in queue
                for j in active:
                    min_t = min(active[j][1], time-active[j][0]+1, un_used)
                    active[j][1] -= min_t
                    active[j][0] += min_t
                del active[i]
        return count 
