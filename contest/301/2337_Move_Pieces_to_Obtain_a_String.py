class Solution:
    def canChange(self, start: str, target: str) -> bool:
        # check if they contain the same number of s and l, and in same position
        # check if all l in start are in front of r in target
        # check if all r in start are behind all r in target
        start_d = defaultdict(list)
        target_d = defaultdict(list)
        
        for idx,s in enumerate(start):
            start_d[s].append(idx)
        for idx, e in enumerate(target):
            target_d[e].append(idx)
        
        if start.replace('_','') != target.replace('_',''):
            return False
        for sl, tl in zip(start_d['L'], target_d['L']):
            if sl < tl:
                return False
        for sr, tr in zip(start_d['R'], target_d['R']):
            if sr > tr:
                return False
        return True