class Solution:
    def countDigits(self, num: int) -> int:
        num_string = str(num)
        count = 0
        for i in range(len(num_string)):
            cur = int(num_string[i])
            if num % cur == 0:
                count += 1
        return count