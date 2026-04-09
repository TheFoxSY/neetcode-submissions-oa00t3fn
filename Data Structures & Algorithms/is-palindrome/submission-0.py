class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_new = s.lower()
        res = ""
        for letter in s_new:
            if letter.isalnum():
                res += letter
        
        if res[::-1] == res:
            return True
        else:
            return False
        