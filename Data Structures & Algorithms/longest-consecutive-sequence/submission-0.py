class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        HashMap = set(nums)
        longest = 0

        for val in nums:
            
            #check if it's the start of the sequence
            if (val - 1) not in HashMap:
                length = 0
                while (val + length) in HashMap:
                    length +=1
                longest = max(longest,length)
        return longest
