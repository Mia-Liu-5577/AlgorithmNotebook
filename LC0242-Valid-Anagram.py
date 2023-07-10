import collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        char_count = collections.defaultdict(int) # a: 1, b: 2, ..
        abs_sum = 0
        for i in range(len(s)):
            char_count[s[i]] += 1
            abs_sum += (1 if char_count[s[i]] > 0 else -1)

            char_count[t[i]] -= 1
            abs_sum += (1 if char_count[t[i]] < 0 else -1)
        return abs_sum == 0
