class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        decode_d = {' ':' '}
        start = 0
        for k in key:
            if k not in decode_d:
                decode_d[k] = chr(ord('a')+start)
                start += 1
            else:
                continue
        res = ''
        for m in message:
            res += decode_d[m]
        return res