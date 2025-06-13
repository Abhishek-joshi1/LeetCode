from typing import List
class Solution:
    def merge(self, arr: List[int]) -> List[int]:
        res = []
        
        for curr in arr:
            if not res or res[-1][1] < curr[0]:
                res.append(curr)
                continue 
            else:
                res[-1][1] = max(res[-1][1], curr[1])
        return res 

if __name__ == "__main__":
    mySol = Solution()
    print(mySol.merge([[1,3],[2,6],[8,10],[15,18]]))
    print(mySol.merge([[1,4],[4,5]]))