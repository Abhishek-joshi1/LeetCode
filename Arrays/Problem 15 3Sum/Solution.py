from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)
        
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue 
            left = i + 1
            right = n - 1
            while left < right:
                target = nums[i] + nums[left] + nums[right]
                if target == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while right > left and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif target < 0:
                    left += 1
                elif target > 0:
                    right -= 1
                
        return res 
    
if __name__ == "__main__":
    mySol = Solution()
    print(mySol.threeSum([-1,0,1,2,-1,-4]))
    print(mySol.threeSum([0,1,1]))
    print(mySol.threeSum([0,0,0]))     