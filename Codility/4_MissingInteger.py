# coding=utf-8
"""
This is a demo task.

Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Assume that:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(N) (not counting the storage required for input arguments).
"""


# Solution using a dictionary
# https://app.codility.com/demo/results/trainingU66GFP-HTW/

def solution(A):

    D = {} # keep here all the values that appear

    # Loop N times
    for a in A:
        D[a] = 1

    # Another loop. Find the smallest number missing
    m = 1
    for d in D:
        if m in D:
            m += 1
        else:
            return m
    # END. m in this case will be the largest element +1
    return m


# Using sets.
# Drawback: if A[0] is huge we are creating unnecessarily a huge set.
# Passes the tests with 100%
# https://app.codility.com/demo/results/trainingGECBJE-96A/
def solution(A):

    # Pace all existing values inside a set
    D = set(A)

    # Ideal set
    N = len(A)+2 # Each one number above N
    D2 = set(range(1,N))

    # Just calculate difference
    diff = D2.difference(D)

    # END
    return min(diff)

# Another possible approach: we only need to check N+1 numbers! We could do it with a list instead of a dictionary or a set (even though this way was easier)


A = [1,3,6,4,1,2]
solution(A) # 5

A = [1,2,3]
solution(A) # 4

A = [-1,-2,-3]
solution(A) # 1

A = [1]
solution(A) #2

A = [10]
solution(A) #1