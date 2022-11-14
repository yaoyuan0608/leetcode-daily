class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot = sorted(robot)
        factory = sorted(factory)
        memo = {}
        # ith robot on jth factory with k used before
        def dp(i, j, k):
            # robot reach end
            if i == len(robot):
                memo[(i,j,k)] = 0
                return 0
            # no more factory
            if j == len(factory):
                memo[(i,j,k)] = float('inf')
                return float('inf')
            # current ith robot move to next factory (j+1)
            res1 = dp(i, j+1, 0)
            # current ith robot used current jth factory and move the next robot
            if k < factory[j][1]:
                res2 = dp(i+1, j, k+1) + abs(robot[i] - factory[j][0])
            else:
                res2 = float('inf')
            res = min(res1, res2)
            memo[(i,j,k)] = res
            return res
        
        return dp(0,0,0)
        