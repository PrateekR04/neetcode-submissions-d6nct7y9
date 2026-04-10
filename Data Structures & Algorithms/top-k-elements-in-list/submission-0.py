from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Map = Counter(nums)
        res = []
        for key, val in sorted(Map.items(), key=lambda x: x[1], reverse=True):
            res.append(key)
            if len(res) == k:
                break
    
        return res

