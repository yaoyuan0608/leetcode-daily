class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        # maximum substring problem with constrain: sliding windows
        # calculate the maximum T and F
        def find_max(string):
            left, right = 0, 0
            count = 0
            res = 0
            for right in range(len(answerKey)):
                cur = answerKey[right]
                count += cur == string
                while count > k and left <= right:
                    old = answerKey[left]
                    count -= old == string
                    left += 1
                res = max(res, right-left+1)
            return res
        return max(find_max('T'), find_max('F'))