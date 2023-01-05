class Solution:
    def findMin(self, nums: List[int]) -> int:
        # the problem can be translated as, looking for the index,
        # whose value is smaller than all others on its right side
        left = 0
        right = len(nums)-1
        # this is the only two problem that needs [left, right] and while left < right
        while left < right:
            # for all elements on the right side of mid, are bigger or equal than mid
            mid = left + (right-left)//2
            if nums[mid] <= nums[right]:
                right = mid
            else:
                left = mid + 1
        return nums[left]