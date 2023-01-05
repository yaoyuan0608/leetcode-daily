class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # same idea as in problem 33
        l = 0
        r = len(nums) - 1
        while l <= r:        
            # # a small trick to avoid duplicates
            # while l < r and nums[l] == nums[l+1]:
            #     l += 1
            # while l < r and nums[r] == nums[r-1]:
            #     r -= 1
            mid = l + (r-l) // 2
            if nums[mid] == target:
                return True
            # if mid is strictly bigger than l, [l, mid) is strickly sorted
            if nums[mid] > nums[l]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # [l,mid) is strickly not sorted
            elif nums[mid] < nums[l]:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            # all other cases like nums[l] == nums[mid]
            else:
                l += 1
        return False