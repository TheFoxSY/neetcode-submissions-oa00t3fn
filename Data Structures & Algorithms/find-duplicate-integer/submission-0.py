class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count = set()
        for i in nums:
            if i in count:
                return i
            count.add(i)
        