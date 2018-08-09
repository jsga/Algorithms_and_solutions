"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0, len(nums)-1):
            for j in range(i+1, len((nums))):
                if nums[i] + nums[j] == target:
                    return [i,j]

        return False


# Solution above too slow (of course). Lets give another try



# The key here is that given a number and a target, there is only one possible number that completes the sum
# that means we do not need to check all remaining numbers. Only check that the ONE number exists.

# We can either create a dictionary (efficient with large numbers)
# or a array of ones and zeros (efficient with small numbers)

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Find existing elements
        d = {}
        for i in range(0, len(nums)):
            d[nums[i]] = i

        # Loop through nums again and check if complementary exists
        for i in range(0,len(nums)):
            if target - nums[i] in d:
                # Do not allow for the same element
                if d[target - nums[i]] != i:
                    return [d[target - nums[i]], i]

        return False

S = Solution()
nums = [0,2,3,7,1,8]
target = 15
sol = S.twoSum(nums,target) # 5 3
sol

nums = [-3,4,3,90]
target = 0
S.twoSum(nums,target) # 0,2

nums = [3,2,4]
target = 6
S.twoSum(nums,target) # 1,2

nums = [3,3]
target = 6
S.twoSum(nums,target) # 0 1


