class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # nums[l:r+1] has median k when #less == #greater or #less+1 == #greater
        d_map = defaultdict(int)
        d_map[0] = 1
        count = 0
        res = 0
        flag = False
        for i in range(len(nums)):
            if nums[i] < k:
                count -= 1
            elif nums[i] > k:
                count += 1
            else:
                flag = True
            # the current index has crossed k, start to find corresponding values
            if flag:
                res += d_map[count]
                res += d_map[count-1]
            else:
                d_map[count] += 1
                
            #print(d_map,count,flag)
        return res