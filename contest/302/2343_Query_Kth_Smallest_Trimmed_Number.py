class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        res = []
        for query in queries:
            k,trim = query
            new_num = [int(num[::-1][:trim][::-1]) for num in nums]
            sorted_new_num = sorted([(num, idx) for idx, num in enumerate(new_num)])
            res.append(sorted_new_num[k-1][1])
        return res