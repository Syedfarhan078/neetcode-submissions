class Solution:
    def isPalindrome(self, s: str) -> bool:
        check_string = "".join([char for char in s.lower() if char.isalnum()])
        left = 0
        right = len(check_string) - 1

        while left < right:
            if check_string[left] != check_string[right]:
                return False
            
            left += 1
            right -=1
        
        return True