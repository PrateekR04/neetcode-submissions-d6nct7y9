class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # One pile at a time 
        
        
        
        
        l = 1
        r = max(piles)
        result = r
        
        while l<=r:
            k = (l + r)//2
            hours = 0
            for p in piles:
                hours += math.ceil(p/k)
            if hours <= h:
                result = min(result, k)
                r = k - 1
            else:
                l = k + 1


        return result