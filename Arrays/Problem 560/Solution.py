from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = 0
        pre_sum = 0
        myMap = defaultdict(int)
        myMap[0] = 1

        for n in nums:
            pre_sum += n
            remove = pre_sum - k
            cnt += myMap[remove]
            myMap[pre_sum] += 1
        
        return cnt

if __name__ == "__main__":
    mySol = Solution()
    print(mySol.subarraySum(nums = [1,1,1], k = 2))
    print(mySol.subarraySum(nums = [1,2,3], k = 3))