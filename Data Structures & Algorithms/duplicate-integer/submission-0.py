from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        seen = Counter(nums)

        for x in list(seen.values()):
            if x > 1:
                return True
        return False