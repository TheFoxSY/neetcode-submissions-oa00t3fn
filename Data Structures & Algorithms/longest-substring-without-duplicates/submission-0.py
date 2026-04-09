class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l ,r = 0, 1
        tempMax = 1
        maximum = 0
        seen = set()

        while l < len(s):
            if r >= len(s) or s[l] == s[r] or s[r] in seen:
                maximum = max(tempMax, maximum)
                tempMax = 1
                l += 1
                r = l + 1
                seen = set()
            else:
                seen.add(s[r])
                tempMax += 1
                r += 1
        
        return maximum
