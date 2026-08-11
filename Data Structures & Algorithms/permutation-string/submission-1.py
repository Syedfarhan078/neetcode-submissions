class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)

        if n > m:
            return False
        
        sorted_s1 = "".join(sorted(s1))

        for i in range(0, m - n + 1):
            substr = s2[i: i+n]

            check_substr = "".join(sorted(substr))

            if sorted_s1 == check_substr:
                return True
        
        return False

