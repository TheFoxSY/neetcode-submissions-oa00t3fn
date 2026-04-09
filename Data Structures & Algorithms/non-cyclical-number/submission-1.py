class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        total = 0
        while total != 1:
            total = 0
            for letter in str(n):
                total += int(letter) ** 2
            
            if total not in seen:
                seen.add(total)
            else:
                return False       
           
            n = str(total)
        
        return True