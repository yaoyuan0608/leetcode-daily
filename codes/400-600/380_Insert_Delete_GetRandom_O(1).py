### idea: use a list to store all values, use a dict to store the pair of (value, idx in list) for quick lookup
class RandomizedSet:
    def __init__(self):
        self.idx = 0
        self.dict = {}
        self.list = []
    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        else:
            self.dict[val] = self.idx
            self.list.append(val)
            self.idx += 1
            return True
    def remove(self, val: int) -> bool:
        if val in self.dict:
            old_idx = self.dict[val]
            self.dict[self.list[-1]] = old_idx
            self.list[old_idx], self.list[-1] = self.list[-1], self.list[old_idx]
            self.list.pop()
            del self.dict[val]
            self.idx -= 1
            return True
        else:
            return False
    def getRandom(self) -> int:
        return random.choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()