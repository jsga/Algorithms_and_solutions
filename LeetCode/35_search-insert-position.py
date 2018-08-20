"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:
Input: [1,3,5,6], 5
Output: 2

Example 2:
Input: [1,3,5,6], 2
Output: 1

Example 3:
Input: [1,3,5,6], 7
Output: 4

Example 4:
Input: [1,3,5,6], 0
Output: 0
"""


class Solution:
    def searchInsert(self, nums, target):
        """
        The array is sorted so we can use binary search and start from the middle.
        """

        i_max = len(nums)
        i_min = 0

        while i_min < i_max:

            # Check middle point
            i = i_min + (i_max - i_min) // 2

            if nums[i] == target:
                return i

            if nums[i] > target: # target must be below i
                i_max = i

            elif nums[i] < target: # target must be above
                i_min = i+1

        # Here we did not find the element. Both ends met each other.
        return i_min


S = Solution()
nums = [1,3,5,6]
target = 5
S.searchInsert(nums,target) # 2

target = 2
S.searchInsert(nums,target) # 1

target = 7
S.searchInsert(nums,target) # 4

target = 0
S.searchInsert(nums,target) # 0

target = 4
S.searchInsert(nums,target) # 2

nums = [-1,-3,5,6]
target = 0
S.searchInsert(nums,target) # 2

nums = [-1,-3,5,6]
target = 0
S.searchInsert(nums,target) #2

nums = [1,3,5]
target = 4
S.searchInsert(nums,target) # 2