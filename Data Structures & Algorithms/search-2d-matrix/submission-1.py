class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        helper = [(i, min(arr)) for i,arr in enumerate(matrix)]
        arrIndex = -1
        for i,minVal in helper:
            if minVal <= target:
                arrIndex = i
            else:
                break
        
        if arrIndex == - 1:
            return False
        
        start = 0
        end = len(matrix[arrIndex]) - 1
        while start <= end:
            mid = (start + end)//2

            if target < matrix[arrIndex][mid]:
                end = mid - 1
            elif target == matrix[arrIndex][mid]:
                return True
            else:
                start = mid + 1
        
        return False