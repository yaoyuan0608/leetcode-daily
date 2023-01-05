class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # regarding the middle point, there is always one side is sorted. 
        # if middle is bigger than mostleft, it means left side is sorted, compare the target with middle value, 
        # if the target is located in [left,mid], change right to mid-1
        
        left = 0
        right = len(nums) - 1
        # left and right can all be reached, so the ranges are inclusive
        while left <= right:
            mid = left + (right - left) // 2
            # we find target value
            if target == nums[mid]:
                return mid
            # if left side is sorted
            # <= is necessary here, because the calculation of mid is rounding down, and it is possible that mid == leftx
            if nums[left] <= nums[mid]:
                # if the target is located in [left, mid)
                if nums[mid] > target and nums[left] <= target:
                    right = mid - 1
                else:
                    left = mid + 1
            # if right side is sorted
            else:
                # if the target is located in (mid, right]
                if nums[mid] < target and nums[right] >= target:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1