class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        start = 0
        for i in range(len(derived)-1):
            start = start ^ derived[i]
        if start ^ derived[-1] == 0:
            return True
        
        start = 1
        for i in range(len(derived)-1):
            start = start ^ derived[i]
        if start ^ derived[-1] == 1:
            return True
        return False