class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True

        s = s.lower()
        left = 0
        right = len(s) - 1

        while left < right:
            while left < len(s) and not s[left].isalnum():
                left += 1
            
            while right > -1 and not s[right].isalnum():
                right -= 1

            if right <= -1 or left >= len(s):
                return True

            if s[right] != s[left]:
                return False

            left += 1
            right -= 1
        
        return True
            