"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.

"""

# Dynamic programming approach & greedy

# Pre-process 1 time array calculating the lowest index such that jumping once we can reach the current cell.
# In other words, if we have [2,1,0], the 0 can be reached from 1 and 2 -> we select 2 as its index is lower

# Start by the end.
# Take the "earliest" jump (use the pre-processed array). This is kind of a greedy approach.
# Take 1 jump backwards
# Repeat steps above. If not possible anymore, return false
# Stop if index = 0, return true


class Solution:

    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # prev array: amongst all the cells from which we can reach i with a single jump, which is one with lowest index (i.e., earliest)?
        N = len(nums)
        prev = [N + 1] * N  # -1 means we cannot reach this cell
        prev[0] = 0  # the first cell is always reached by definition
        max_idx = 0 # keep the max index visited so that we don't check elements twice. This is mostly for optimization purposes.

        for i in range(0, len(nums)):

            # Iterate as many times as nums
            k = max_idx - i +1 # 1 Start with the latest index seen
            while k <= nums[i] and k + i < N and i+k >= max_idx:
                if prev[i + k] == (N + 1):  # we need to visit once the prev array since we go left to right
                    prev[i + k] = i
                    max_idx = i+k # update latest index visited
                k += 1

        print(prev)

        # Start by the end. Call the current best index b
        b = prev[-1]
        while b > 0 and b != (N + 1):
            if b == prev[b]: break # Stop if we did not move
            b = prev[b]


        # Return True only if we have reached the start of the array
        if b == 0:
            return True
        else:
            return False




S = Solution()
nums = [2,3,4,1,2,0,1,3]
S.canJump(nums) # True

nums = [2,5,0,0]
S.canJump(nums) # True

nums = [2,3,1,1,4]
S.canJump(nums) # True

nums = [3,2,1,0,2,0,1]
S.canJump(nums) # False

nums = [0]
S.canJump(nums) # True