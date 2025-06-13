class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_sum = 0
        max_sum = -float('inf')

        for i in range(len(nums)):
            curr_sum += nums[i]
            max_sum = max(curr_sum, max_sum)
            if curr_sum < 0:
                curr_sum = 0
        return max_sum

if __name__ == "__main__":
    mySol = Solution()
    print(mySol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
    print(mySol.maxSubArray([1]))
    print(mySol.maxSubArray([5,4,-1,7,8]))