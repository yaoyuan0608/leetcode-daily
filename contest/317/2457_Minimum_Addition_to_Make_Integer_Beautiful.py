class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        def countnum(x):
            x = str(x)
            count = 0
            for i in range(len(x)):
                count += int(x[i])
            return count
        
        count = countnum(n)
        move = 0
        n = str(n)
        idx = len(n) - 1
        power = 0

        if count <= target:
            return move

        while count > target and idx >= 0:
            k = int(n[idx]) + (idx != len(n)-1)
            move += (10 - k) * pow(10, power)
            count = countnum(move+int(n))
            if count <= target:
                return move
            idx -= 1
            power += 1
            
        return move