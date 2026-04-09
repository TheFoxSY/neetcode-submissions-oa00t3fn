class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        numbers = ""
        res = []
        for number in digits:
            numbers += str(number)
        before = int(numbers)
        after = before + 1
        
        for number in str(after):
            res.append(int(number))
        
        return res
        
