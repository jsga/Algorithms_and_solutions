"""
Let's call any (contiguous) subarray B (of A) a mountain if the following properties hold:

B.length >= 3
There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
(Note that B could be any subarray of A, including the entire array A.)

Given an array A of integers, return the length of the longest mountain.

Return 0 if there is no mountain.

Example 1:

Input: [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
Example 2:

Input: [2,2,2]
Output: 0
Explanation: There is no mountain.
Note:

0 <= A.length <= 10000
0 <= A[i] <= 10000
Follow up:

Can you solve it using only one pass?
Can you solve it in O(1) space?

"""


class Solution(object):
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        # Keep record of start and top-so-far of the valley
        start = 0
        top = -1
        # Keep also the max length
        max_mountain = 0

        for i, a in enumerate(A):

            # Print some stuff
            print(
                'i = ' + str(i) + ' a = ' + str(a) + ' start = ' + str(start) + ' top = ' + str(top) + ' max = ' + str(
                    max))

            # Set the start of the mountain
            if i == 0 or a < A[start]:
                start = i

                # up the mountain, top not set yet
            elif a > A[start] and top == -1:

            # Down the mountain, top set
            elif top != -1:

                if a < A[i - 1]:  # still going down
                    continue
                else:
                    # Bottom found.
                    max_mountain = max(max_mountain, i - start)
                    # Reset top and start
                    top = -1
                    start = i
            else:
                print('Dont know why im here')
