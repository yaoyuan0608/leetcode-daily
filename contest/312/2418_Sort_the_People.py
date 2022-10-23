class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        if not names or not heights or len(names) != len(heights):
            return []
        comb = [[name, height] for name, height in zip(names, heights)]
        comb = sorted(comb, key=lambda x:x[1], reverse=True)
        return [x[0] for x in comb]