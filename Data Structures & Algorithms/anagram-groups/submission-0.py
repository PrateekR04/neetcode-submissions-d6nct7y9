from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Result = []
        group = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s)) 
            group[key].append(s)
        
        for val in group.values():
            Result.append(val)
        return Result

