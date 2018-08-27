"""
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:
Input: [1,3,4,2,2]
Output: 2

Example 2:
Input: [3,1,3,4,2]
Output: 3

Note:
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
"""

class Solution:
    def findDuplicate_modify(self, nums):
        """
        Binary search, counting elements.
        Recall that numbers span from 1 to n+1
        If we select the 5th position and count the values less than 5, we should count 5. If not there is a repeated element
        """
        low = 1
        high = len(nums) - 1

        while low < high:
            # mid point
            mid = low + (high - low) // 2
            count = 0

            # Count number equal or less than nums
            for i in nums:
                if i <= mid:
                    count += 1

            # The solution is in [mid+1,high]
            if count <= mid:
                low = mid + 1
            # If the count is higher it means one of the elements is repeated (below mid), so we can shrink the high bound
            else:
                high = mid

        return low

    def findDuplicate_modify(self, nums):
        """
        Here we modify nums
        Use nums as a hash table
        Add len(nums) and then find out which value is above 2*len(nums)
        This is O(N) and without extra space.
        """
        # Modify nums
        N = len(nums)
        for n in nums:
            nums[n % N] += N

        # Find value that has been modified 2 times
        for i, n in enumerate(nums):
            if n >= 2 * N:
                return i
        # No need to arrive here given the assumptions...
        return False
