class SnapshotArray:

    def __init__(self, length: int):
        self.snap_count = 0
        self.database = [[[0, 0]] for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        self.database[index].append([self.snap_count, val])

    def snap(self) -> int:
        self.snap_count += 1
        return self.snap_count - 1

    def get(self, index: int, snap_id: int) -> int:
        snap_idx = bisect.bisect_right(self.database[index], [snap_id, 10**9])
        return self.database[index][snap_idx-1][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)