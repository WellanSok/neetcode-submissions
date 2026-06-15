class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        midRow = len(matrix) 
        midCol = len(matrix[0])
        r , c = 0,midCol-1
        while r < midRow and c>=0:
            if matrix[r][c] > target:
                c -=1
            elif matrix[r][c] < target:
                r +=1
            else:
                return True
        return False