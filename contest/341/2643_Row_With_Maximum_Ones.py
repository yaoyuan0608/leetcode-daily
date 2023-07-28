class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        maximum = 0
        idx = 0
        for i, m in enumerate(mat):
            count = sum(m)
            if count > maximum:
                maximum = count
                idx = i
        return [idx, maximum]