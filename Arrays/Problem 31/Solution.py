from typing import List 

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # step 1 to find a element who value is lesser than the right adjacent element 
        pivot = -1 
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                pivot = i
                break
        if pivot == -1: return nums.sort()
        
        #step 2: find a element who value is just bigger than the pivot element for that do reverse traversing 
        j = len(nums) - 1
        while j > i:
            if nums[j] > nums[i]:
                new_pivot = j
                break
            j -= 1
            
        # Swap of elements 
        nums[pivot], nums[new_pivot] = nums[new_pivot], nums[pivot] 

        # after swap from element after the pivot element do sorting 
        nums[pivot + 1:] = reversed(nums[pivot + 1:])

        return nums
    
if __name__ == "__main__":
    mySol = Solution()
    print(mySol.nextPermutation([1,2,3]))