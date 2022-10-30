class NumberContainers:

    def __init__(self):
        self.number_d = defaultdict(list)
        self.index_d = defaultdict(list)
    def change(self, index: int, number: int) -> None:
        tmp_list = self.number_d[number]
        heapq.heappush(tmp_list, index)
        self.number_d[number] = tmp_list
        self.index_d[index] = number

    def find(self, number: int) -> int:
        tmp_list = self.number_d[number]
        while tmp_list and self.index_d[tmp_list[0]] != number:
            heapq.heappop(tmp_list)
        if not tmp_list:
            self.number_d[number] = tmp_list
            return -1
        else:
            self.number_d[number] = tmp_list
            return tmp_list[0]

# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)