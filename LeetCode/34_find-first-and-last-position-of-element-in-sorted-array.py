"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""


class Solution:
    def searchRange(self, nums, target):
        """
        Note that the array is sorted. This is a classical example of binary search.
        The complexity also indicates the same
        Start from the middle and update the low and high indexes accordingly
        """

        out = [-1,-1]
        low = 0
        high = len(nums)-1

        # Special case: length 1
        if low == high:
                if target == nums[0]:
                    return [0,0]

        while low <= high:

            i = low + (high - low) // 2 # mid point

            # decrease high end
            if nums[i] > target:
                high = i-1

            # Increase lower end
            elif target > nums[i]:
                low = i+1

            if nums[i] == target:
                # Target found. Loop above and below to find max and min.

                # Lower end
                out[0] = i
                j = 1
                while i-j >= 0:
                    if nums[i-j] == target:
                        out[0] = i-j
                        j += 1
                    else:
                        break

                # higher end
                out[1] = i
                j = 1
                while  i+j < len(nums):
                    if nums[i + j] == target:
                        out[1] = i + j
                        j += 1
                    else:
                        break

                # found. Break
                break
        # END
        return out


S = Solution()
nums = [5,7,7,8,8,10]
target = 8
S.searchRange(nums,target) # 3 4

nums = [5,7,7,8,8,10]
target = 4
S.searchRange(nums,target) #-1 -1

nums = [5,7,7,7,7,8,8,10]
target = 7
S.searchRange(nums,target) # 1 4

nums = []
target = 7
S.searchRange(nums,target) # -1 -1

nums = [1]
target = 1
S.searchRange(nums,target) # 0,0

nums = [1]
target = 3
S.searchRange(nums,target) # -1 -1

nums = [1,1,1,1]
target = 1
S.searchRange(nums,target) # 0,3

nums = [1,2]
target = 2
S.searchRange(nums,target) # 1,1