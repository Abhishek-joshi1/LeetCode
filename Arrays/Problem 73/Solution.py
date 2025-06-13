from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        
        row_zero, col_zero = False, False 
        
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    if r == 0: row_zero = True 
                    if c == 0: col_zero = True 
                    matrix[r][0] = 0 
                    matrix[0][c] = 0
        
        for r in range(1, rows):
            for c in range(1, cols): 
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        
        if row_zero:
            for i in range(cols):
                matrix[0][i] = 0
        
        if col_zero:
            for j in range(rows):
                matrix[j][0] = 0 
        
        return matrix

if __name__ == "__main__":
    mySol = Solution()
    print(mySol.setZeroes([[1,1,1],[1,0,1],[1,1,1]]))
    print(mySol.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))
    
    # ans 1 : [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
    # ans 2 : [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]