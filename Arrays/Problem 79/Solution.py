from typing import List 

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visit = set()

        def dfs(r, c, i):
            if i == len(word):
                return True 
            if r < 0 or c < 0 or r >= rows or c >= cols or word[i] != board[r][c] or (r,c) in visit:
                return False

            visit.add((r,c))
            res = (dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1)) 
            visit.remove((r,c))

            return res     

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True 
        return False 
    
if __name__ == "__main__":
    mySol = Solution()
    print(mySol.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))