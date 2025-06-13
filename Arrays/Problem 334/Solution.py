from typing import List
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) <= 2:
            return False 
        first = float("inf")
        Second = float("inf")
        Third = float("inf")
        
        for i in range(len(nums)):
            if nums[i] < first:
                first = nums[i]
                continue
            elif nums[i] < Second:
                Second = nums[i]
                continue
            else:
                return True
        return False
    
if __name__ == "__main__":
    mySol = Solution()
    print(mySol.increasingTriplet([1,2,3,4,5]))
    print(mySol.increasingTriplet([5,4,3,2,1]))
    print(mySol.increasingTriplet([2,1,5,0,4,6]))