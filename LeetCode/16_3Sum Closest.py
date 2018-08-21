"""

Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""


# We can start by thinking how we would find the closest 2 sum and then extend it to three (see bottom script)

class Solution:

    def threeSumClosest(self, nums, target):
        """
        Find the closest 3 sum to target. O(n**2)
        Based on caterpillar method to find the closes 2-sum for every item.
        """

        # Sort the array
        nums.sort()

        # Keep solution here
        sol_sum, sol3 =  sum(nums[:3]),sum(nums[:3]) # start with the worse solution possible
        sol_totarget = abs(sol3 - target)

        # loop every item and find 2 closest sum of the remaining array
        for i in range(0,len(nums)-2):

            # Edges of caterpillar
            j = i+1
            k = len(nums) - 1

            while j < k:

                # Solution so far
                sol3 = nums[i] + nums[j] + nums[k]

                # Update target
                sol_totarget_aux = abs(target - sol3)

                # Check if target found
                if sol_totarget_aux == 0:
                    return sol3
                # Better target found
                elif sol_totarget_aux < sol_totarget:
                    sol_sum = sol3
                    sol_totarget = sol_totarget_aux
                    print('i = ' + str(i) + ' j = ' + str(j) + ' k = ' + str(k))

                # Increase/decrease edges of caterpillar
                if  target  > sol3:
                    j += 1
                elif target < sol3:
                    k -= 1

        # END
        return sol_sum


S = Solution()
nums = [-5,-4,-2,0,3,4,8,10]
target = 7
S.threeSumClosest(nums,target) # 7


nums = [-1,2,1,-4]
target = 1
S.threeSumClosest(nums,target) # 2

nums = [-1,1,2]
target = 1
S.threeSumClosest(nums,target) # 3

nums = [-1,1,2]
target = 4
S.threeSumClosest(nums,target) # 2

nums = [1,1,1,0]
target = -100
S.threeSumClosest(nums,target) # 2




def twoSumclosest(self,nums,target):
    """
    nums is a sorted array. Find the 2 closes items to target and return their sum
    TODO: clean and make the code look nicer.
    """

    # Edges of caterpillar
    x = 0
    y = len(nums)-1

    # Solution so far
    sol_sum = nums[x] + nums[y]
    sol_totarget = max(abs(target), abs( sol_sum))


    while x < y:

        # Condition on the left and right
        left = target - nums[x]
        right = target - nums[y]

        # Update target
        sol_sum_aux = nums[x] + nums[y]
        sol_totarget_aux = abs(target - sol_sum_aux)
        if sol_totarget_aux < sol_totarget:  # Better target found
            sol_sum = sol_sum_aux
            sol_totarget = sol_totarget_aux

        if left >= nums[y]: # increase left index
            x += 1

        elif right <= nums[x]:
            y -= 1



    # END. Return the sum of both elements
    return sol_sum
