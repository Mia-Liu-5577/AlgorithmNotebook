class Solution:
    def isAlphanumeric(self, c):
        return (c >= 'A' and c <= 'Z') or \
                (c >= 'a' and c <= 'z') or \
                (c >= '0' and c <= '9')

    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        left = 0
        right = len(s) - 1
        # Always pay attention to boundary
        while left < right:
            while left < len(s) and not self.isAlphanumeric(s[left]):
                left += 1
            while right >= 0 and not self.isAlphanumeric(s[right]):
                right -= 1
            
            if left < len(s) and right >= 0 and s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
        
