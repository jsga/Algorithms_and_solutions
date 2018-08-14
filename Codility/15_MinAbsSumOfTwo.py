# coding=utf-8
"""
Let A be a non-empty array consisting of N integers.

The abs sum of two for a pair of indices (P, Q) is the absolute value |A[P] + A[Q]|, for 0 ≤ P ≤ Q < N.

For example, the following array A:

  A[0] =  1
  A[1] =  4
  A[2] = -3
has pairs of indices (0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2).
The abs sum of two for the pair (0, 0) is A[0] + A[0] = |1 + 1| = 2.
The abs sum of two for the pair (0, 1) is A[0] + A[1] = |1 + 4| = 5.
The abs sum of two for the pair (0, 2) is A[0] + A[2] = |1 + (−3)| = 2.
The abs sum of two for the pair (1, 1) is A[1] + A[1] = |4 + 4| = 8.
The abs sum of two for the pair (1, 2) is A[1] + A[2] = |4 + (−3)| = 1.
The abs sum of two for the pair (2, 2) is A[2] + A[2] = |(−3) + (−3)| = 6.
Write a function:

def solution(A)

that, given a non-empty array A consisting of N integers, returns the minimal abs sum of two for any pair of indices in this array.

For example, given the following array A:

  A[0] =  1
  A[1] =  4
  A[2] = -3
the function should return 1, as explained above.

Given array A:

  A[0] = -8
  A[1] =  4
  A[2] =  5
  A[3] =-10
  A[4] =  3
the function should return |(−8) + 5| = 3.

Assume that:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000,000..1,000,000,000].
Complexity:

expected worst-case time complexity is O(N*log(N));
expected worst-case space complexity is O(N) (not counting the storage required for input arguments).

"""


# Start by sorting A.
# If all elements are positive (+ 0) the solution is the absolute value of the min with itself.
# If all elements are negative the solution is the maximum with itself
# If Both positive and negative: Find the "closest" pair of numbers (in abs value terms)

# This is like a srinking caterpillar

# https://app.codility.com/demo/results/training79TFY3-YGX/
def solution(A):

    # Sort in ascending order
    A.sort()
    print(A)

    # Keep indexes from the bottom and top
    low = 0
    up = len(A)-1

    # Solution
    sol = 2*1000000000

    # Start loop
    while low <= up:

        # Both ends positive or 0
        if A[low] > 0 and A[up] > 0:
            return min(sol,A[low]*2)

        # Both ends negative
        elif A[low] < 0 and A[up] < 0:
            return min(sol,-A[up]*2)

        # Both zero
        elif A[low] == 0 or A[up] == 0:
            return 0

        # low is negative and up positive
        else:
            # Save absolute values to save computation

            sol = min(sol,abs(A[low] + A[up]))

            if abs(A[low]) > abs(A[up]):
                low += 1
            else:
                up -= 1
        print('low = ' + str(low) + ' up = ' + str(up) + ' sol = ' + str(sol))

    # END

    return sol


A = [-8,4,5,-10,3]
solution(A) # 3

A = [1,4,-3]
solution(A) # 1

A = [1,2,3,4,5]
solution(A) # 2

A = [-1,-2,-3,-4]
solution(A) # 2

A = [0,-1,-2,-3,-4]
solution(A) # 0

A = [2]
solution(A)