class Solution:
    def fillCups(self, amount: List[int]) -> int:
        count = 0
        while sum(amount) != max(amount):
            min_idx = amount.index(min(amount))
            for i in range(3):
                if i != min_idx:
                    amount[i] -= 1
            count += 1
        
        return count + sum(amount)