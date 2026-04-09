class Solution:
    def isHappy(self, n: int) -> bool:
        inputNumber = str(n)
        seen = set()
        total = 0
        while total != 1:
            total = 0
            for letter in inputNumber:
                total += int(letter) * int(letter)
            
            if total not in seen:
                seen.add(total)
            else:
                return False       
           
            inputNumber = str(total)
        
        return True