class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill = sorted(skill)
        total = skill[0] + skill[-1]
        res = 0
        l,r = 0, len(skill)-1
        
        while l < r:
            if skill[l] + skill[r] != total:
                return -1
            res += skill[l] * skill[r]
            l += 1
            r -= 1
        return res