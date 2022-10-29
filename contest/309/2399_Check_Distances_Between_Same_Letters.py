class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        string_d = defaultdict(int)
        for idx, string in enumerate(s):
            if string not in string_d:
                string_d[string] = idx
            else:
                string_d[string] = idx - string_d[string] - 1
        
        for key, value in string_d.items():
            mapping_index = ord(key) - ord('a')
            if distance[mapping_index] != value:
                return False
        return True