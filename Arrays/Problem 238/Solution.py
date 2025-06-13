class Solution:
    def productExceptSelf(self, nums):
        if not nums:
            return -1
        res = [0] * len(nums)
        l = 1
        for i in range(len(nums)):
            res[i] = l
            l *= nums[i]
        
        r = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= r
            r *= nums[i]
        nums = res
        return nums 

if __name__ == "__main__":
    mySol = Solution()
    print(mySol.productExceptSelf([1,2,3,4]))
    print(mySol.productExceptSelf([-1,1,0,-3,3]))