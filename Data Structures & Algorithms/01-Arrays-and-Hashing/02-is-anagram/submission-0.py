from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        cnt = Counter(s)

        for char in t:
            cnt[char] -= 1

            if cnt[char] < 0:
                return False
        return True
