class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # sum = 0
        # i, j, k should be distinct
        nums.sort()
        res = []
        for i in range(len(nums)-2):

            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            start = i + 1
            end = len(nums) - 1
            target = - nums[i]
            while start < end:

                if nums[start] + nums[end] > target:
                    end -= 1
                elif nums[start] + nums[end] < target:
                    start += 1
                else:
                    res.append([nums[i], nums[start], nums[end]])
                    start += 1
                    end -= 1
                    while start < end and nums[start] == nums[start - 1]:
                        start += 1
                    
        return res

