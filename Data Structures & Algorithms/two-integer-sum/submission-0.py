class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashMap = {}

        for index,val in enumerate(nums):

            curr = target - val

            if curr in hashMap:
                return [hashMap[curr],index]
            else:
                hashMap[val] = index
        
        return []