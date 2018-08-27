class Solution(object):

    def maximumProduct(self, nums):
        """
        O(nlogn)
        sorting the array makes it faster
        """
        nums = sorted(nums)
        # --+, +++
        # Two negatives and positive, or all positive.
        return max(nums[0] * nums[1] * nums[-1], nums[-3] * nums[-2] * nums[-1])




S = Solution()
nums = [1,2,3,4,2,1]
S.maximumProduct(nums) # 24

nums = [1,2,3,4,-5,-5,0,0,0]
S.maximumProduct(nums) # 100

nums = [-1,-2,-3]
S.maximumProduct(nums)

nums = [-2,-2,2]
S.maximumProduct(nums)
