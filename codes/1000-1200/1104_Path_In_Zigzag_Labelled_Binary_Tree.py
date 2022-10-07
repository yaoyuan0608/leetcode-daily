class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        # use the index of each node, we can calculate its left and right node index
        # at the level of i, indexes are in the range of [2^(i-1), 2^i-1]
        # normally, the parent of the current node is x//2, but the level is reversed, so the idx of the parent should be reversed
        # parent - 2^(i-1) = 2^i-1 - reverse_parent -> parent = 2^i-1+2^(i-1)-parent
        # 1. get the level of the node, 2. perform above formula until end
        level = 0
        while label >= 2**level:
            level += 1
        level -= 1
        res = []
        while label and level:
            res.append(label)
            label = 2**level - 1 + 2**(level-1) - label//2
            level -= 1
        res.append(1)
        return res[::-1]