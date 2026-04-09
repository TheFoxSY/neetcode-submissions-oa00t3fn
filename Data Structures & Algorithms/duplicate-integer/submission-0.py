class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        contains= set()
        for i in nums:
            if i in contains:
                return True
            contains.add(i)
        return False
        