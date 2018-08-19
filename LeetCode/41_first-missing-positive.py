"""
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:
Input: [1,2,0]
Output: 3

Example 2:
Input: [3,4,-1,1]
Output: 2

Example 3:
Input: [7,8,9,11,12]
Output: 1

Note:
Your algorithm should run in O(n) time and uses constant extra space.
"""



class Solution:

    def firstMissingPositive(self, nums):
        """
        Storage is very limited so we do 3 tricks:
        - Remove elements that are <= 0
        - Remove elements above N+1
        - The remaining we re-arrange in a new array that is used as a hash table
        The solution is the first element of such table that has not been filled
        """
        # Number of solutions
        N = len(nums)+1

        # Remove elements not in the solution
        for i in range(0,len(nums)):
            if nums[i] < 0 or nums[i] >= N:
                nums[i] = 0

        # Use the index as the hash to record the frequency of each number
        # Add N to the values that have appeared
        # if N = 10 numbers, we want nums[i]=2 to be hashed at the second position, so 2 % N = 2
        # lets say nums is [2,2]. In the first iteration we have [2,12]. In the second, 12 % 10 = 2 again we find the correct index so [2,22]

        # Watch out: add 1 to the possible answers, since N is a possible solution too, 9 % 10 = 9
        
        nums.append(0)
        for i in range(len(nums)):
            nums[nums[i] % N] += N

        # Given the modified array, we want to select the first element that has a value lower than N
        # That means it never appeared
        for i in range(1, len(nums)):
            if nums[i] < N: # Equivalent to nums[i] // N == 0
                return i

        # Last option: the greatest possible number
        return N

    def firstMissingPositive_slow(self, nums):
        """
        The solution is in {1,2,3,...N+1}. Straightforward approach: loop over the solution set until one is not found.
        It passes the test even though it is O(N**2)
        """
        N = len(nums)

        if N == 0: return 1

        for s in range(1, N + 2):  # Start by the smallest and return as soon as one not found
            if s not in nums:
                return s


S = Solution()
nums = [1,2,0]
S.firstMissingPositive(nums) # 3

nums = [1,2,-1,3,5,6,10,11]
S.firstMissingPositive(nums) # 4

nums = [7,8,9,11,12]
S.firstMissingPositive(nums) # 1

nums = [1,2,3]
S.firstMissingPositive(nums) # 4

nums = []
S.firstMissingPositive(nums) # 1

nums = [1]
S.firstMissingPositive(nums)  # 2

nums = [2]
S.firstMissingPositive(nums)  # 1