"""
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""


class Solution:
    def topKFrequent(self, nums, k):
        """
        Create a hash table and add elements as they appear
        Get their values
        Sort them by value and get the k elements by key
        """
        d = {}
        # Keep frequency in a dictionary
        for n in nums:
            try:
                d[n] += 1
            except KeyError:
                d[n] = 1

        # Sort by the values (number of occurrences). Return the key (element repeated)
        D = sorted(d.items(), key=lambda x: x[1])  # Sort by key (element number 1)

        # Save k last elements in a list
        sol = []
        for i in range(len(D)-1, len(D) -1-k, -1):
            sol.append(D[i][0])

        # END
        return sol


S = Solution()
nums = [1,1,1,2,2,3,3,3,3]
k = 2
S.topKFrequent(nums,k)