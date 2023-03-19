class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:
        # all candidates without square root factor
        primes = {1, 2, 3, 5, 6, 7, 10, 11, 13, 14, 15, 17, 19, 21, 22, 23, 26, 29, 30}
        mod = 1000000007
        counter = Counter(num for num in nums if num in primes)
        # note is the counter containing all possible subset
        note = Counter({1: 1})
        for key in counter:
            if key != 1:
                new_note = Counter()
                for key1 in note:
                    new_note[key1] += note[key1]
                    if gcd(key, key1) == 1:
                        new_note[key1 * key] += note[key1] * counter[key]
                    new_note[key1] %= mod
                print(note)
                note = new_note
        # we can add any 1 in the subset
        return (sum(note.values()) * pow(2, counter[1], mod) - 1) % mod