class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        # iterate from beginning to end, when meet a number, add two more space
        # when meet #, delete a space. if the number of space is negative, return false
        preorder_list = preorder.split(',')
        space = 1
        for pre in preorder_list:
            space -= 1
            if space < 0:
                return False
            if pre != '#':
                space += 2
        return space == 0