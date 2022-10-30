class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        color_d = defaultdict(int)
        number_d = defaultdict(int)
        for r,s in zip(ranks, suits):
            color_d[s] += 1
            number_d[r] += 1
        
        for key, value in color_d.items():
            if value >= 5:
                return 'Flush'
        for key, value in number_d.items():
            if value >= 3:
                return 'Three of a Kind'
        for key, value in number_d.items():
            if value >= 2:
                return 'Pair'
        return 'High Card'