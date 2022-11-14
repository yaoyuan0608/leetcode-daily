class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:

        res = 0
        left = 0
        right = k-1
        total = 0
        seen = defaultdict(lambda: deque())
        for i in range(left, right+1):
            seen[nums[i]].append(i)
            total += nums[i]
            
        
        while right < len(nums):
            #print(seen)
            if len(seen) != right-left+1:
                res = res
            else:
                res = max(total, res)
                        
            total -= nums[left]
            seen[nums[left]].popleft()
            if not seen[nums[left]]:
                del seen[nums[left]]
            
            left += 1
            right += 1
            if right < len(nums):
                seen[nums[right]].append(right)
                total += nums[right]
                
        return res