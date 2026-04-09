class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_new = s.lower()
        l, r = 0, len(s_new) - 1 
        
        while l < r:
            while (l < r and not self.isAlpha(s[l])):
                l += 1
            while (r > l and not self.isAlpha(s[r])):
                r -= 1
            if s_new[l] != s_new[r]:
                return False
            l, r = l + 1, r - 1
        return True
            
    def isAlpha(self, c):
        return (ord('a') <= ord(c) <= ord('z') or
                ord('A') <= ord(c) <= ord('Z') or
                ord('0') <= ord(c) <= ord('9'))
        