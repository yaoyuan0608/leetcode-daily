class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        # compare the nums with target by odd and even numbers
        # the key point here is that an odd number cannot convert to an even number

        nums_odd = sorted([x for x in nums if x%2 == 1])
        nums_even = sorted([x for x in nums if x%2 == 0])
        target_odd = sorted([x for x in target if x%2 == 1])
        target_even = sorted([x for x in target if x%2 == 0])
        # easy to prove that sum(diff) == 0, so we only need to consider those diff > 0
        count = 0
        for i in range(len(nums_odd)):
            diff = nums_odd[i] - target_odd[i]
            if diff > 0:
                count += diff//2
        
        for i in range(len(nums_even)):
            diff = nums_even[i] - target_even[i]
            if diff > 0:
                count += diff//2
        return count