class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def dfs(i , j):
            if i >= len(s):
                if i == j:
                    res.append(part[:])
                return   
            
            if self.isPalindrome(s, j , i):
                part.append(s[j : i + 1])
                dfs(i + 1, i + 1)
                part.pop()
            
            dfs(i + 1, j)
       
        dfs(0 ,0)
        return res
    
    
    def isPalindrome(self, s, l, r) -> bool:
        while l < r:
            if s[l] != s[r]:
                return False
            l , r = l + 1 , r - 1
        return True 

        