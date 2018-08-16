"""
A non-empty array A consisting of N integers is given.

A permutation is a sequence containing each element from 1 to N once, and only once.

For example, array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
is a permutation, but array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
is not a permutation, because value 2 is missing.

The goal is to check whether array A is a permutation.

Write a function:

def solution(A)

that, given an array A, returns 1 if array A is a permutation and 0 if it is not.

For example, given array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
the function should return 1.

Given array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
the function should return 0.

Assume that:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [1..1,000,000,000].
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(N) (not counting the storage required for input arguments).

"""

# summing A does not necessarily work:  1 1 1 7, sum = 10, same as 1 2 3 4
# Hash table: not an option since the range of A >> N

# https://app.codility.com/demo/results/trainingR85X4X-ZHH/
def solution(A):

    # Calculate sum from 1 to N
    N = len(A)
    S = (N+1)*(N//2) + (N%2)*(N+1)/2
    Sa = sum(A)

    # Set (hash table)
    s = set(A)

    # Condition: The sum must be equal to S and each element must be unique
    if len(s) == len(A) and S == Sa:
        return 1
    else:
        return 0


A = [4,1,3,2]
solution(A) # 1

A = [4,1,3]
solution(A)

A = [1]
solution(A) # 1

A = [2]
solution(A) # 0


A = [1,2,3,4,5,6,7,8,9,11]
solution(A) # 0

A = [1,1,1,7]
solution(A) # 0