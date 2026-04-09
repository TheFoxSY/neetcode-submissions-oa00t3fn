class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {} # char -> last index

        for index, letter in enumerate(s):
            lastIndex[letter] = index
        
        size, endIndex = 0, 0
        res = []
        for index, letter in enumerate(s):
            size += 1
            endIndex = max(endIndex, lastIndex[letter])
            if index == endIndex:
                res.append(size)
                size = 0
        
        return res
                
            

        