class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        m, n = len(board), len(board[0])
        
        def check_dup_row(arr, m):
            for r in range(m):
                seen = set()
                for num in arr[r]:
                    if num == ".":
                        continue
                    if num in seen:
                        return False
                    seen.add(num)
            return True        

        def check_dup_col(arr, m, n):
            for col in range(n):
                seen = set()
                for row in range(m):
                    val = arr[row][col]
                    if val == ".":
                        continue
                    if val in seen:
                        return False
                    seen.add(val)
            return True
        
        def check_dup_box(arr,m,n):
            for box_row in range(0,m,3):
                for box_col in range(0,n,3):
                    seen = set()
                    for i in range(3):
                        for j in range(3):
                            val = arr[box_row+i][box_col+j]
                            if val == ".":
                                continue
                            elif val in seen:
                                return False
                            else:
                                seen.add(val)
            return True

        if not check_dup_row(board, m):
            return False
        
        if not check_dup_col(board, m, n):
            return False
        if not check_dup_box(board,m,n):
            return False
        
        
        return True