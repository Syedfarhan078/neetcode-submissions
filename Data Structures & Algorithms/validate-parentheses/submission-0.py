class Solution:
    def isValid(self, s: str) -> bool:
        previous_length = -1

        while len(s) != previous_length:
            previous_length = len(s)

            s = s.replace("()", "")
            s = s.replace("{}", "")
            s = s.replace("[]", "")

        return len(s) == 0


