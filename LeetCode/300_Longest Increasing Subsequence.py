"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Note:
There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
"""


class Solution:
    def lengthOfLIS(self, nums):
        """
        O(N**2) solution based on dynamic programming
        Iterate backwards. Start by count = 1
        For each element, select:
            which element to the right are greater
            Amongst them: which one has the greatest count?
            add +1 and continue
        """

        if len(nums) == 0: return 0

        dp = [1] * len(nums)  # The min length is always 1

        for i in range(len(nums) - 1, -1, -1):

            # Iterate over elements to the right of i
            # The one that is greater AND has biggest dp value is the optimal
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i] and dp[j] >= dp[i]:
                    dp[i] = dp[j] + 1

        # Finally get the max of dp
        sol = 0
        for d in dp:
            sol = max(sol, d)

        # END
        return sol


S = Solution()
nums = [10, 9, 2, 5, 3, 7, 101, 18]
S.lengthOfLIS(nums)  # 4

nums = [2,6,4,5,8,101,18]
S.lengthOfLIS(nums) # 5 -> 2 4 5 8 101