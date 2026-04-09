class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        check1=collections.defaultdict(int)
        check2=collections.defaultdict(int)
        for i in s:
            check1[i]+=1
        for i in t:
            check2[i]+=1
        if check1==check2:
            return True
        else: return False