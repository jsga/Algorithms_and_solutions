'''
An integer M and a non-empty array A consisting of N non-negative integers are given. All integers in array A are less than or equal to M.

A pair of integers (P, Q), such that 0 ≤ P ≤ Q < N, is called a slice of array A. The slice consists of the elements A[P], A[P + 1], ..., A[Q]. A distinct slice is a slice consisting of only unique numbers. That is, no individual number occurs more than once in the slice.

For example, consider integer M = 6 and array A such that:

    A[0] = 3
    A[1] = 4
    A[2] = 5
    A[3] = 5
    A[4] = 2
There are exactly nine distinct slices: (0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2), (3, 3), (3, 4) and (4, 4).

The goal is to calculate the number of distinct slices.

Write a function:

def solution(M, A)

that, given an integer M and a non-empty array A consisting of N integers, returns the number of distinct slices.

If the number of distinct slices is greater than 1,000,000,000, the function should return 1,000,000,000.

For example, given integer M = 6 and array A such that:

    A[0] = 3
    A[1] = 4
    A[2] = 5
    A[3] = 5
    A[4] = 2
the function should return 9, as explained above.

Assume that:

N is an integer within the range [1..100,000];
M is an integer within the range [0..100,000];
each element of array A is an integer within the range [0..M].
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(M) (not counting the storage required for input arguments).
'''


# A single element is always a slice. The lower bound for the slution is len(A)=N
# Pure caterpilar method. Keep on adding elements to hash table until a repeated one. When so, re-start process.


def solution(M,A):

    if len(A)==1: return 1

    count = 0
    d =[] # list where we keep the seen elements

    # Initialize counter and list
    count += 1
    d.append(A[0])

    for i,a in enumerate(A[1:]):

        # element is not seen in the slice
        if a not in d:
            d.append(a)
            count += 1 + (len(d) -1) # always count current element + new slices

        else: # element is seen already.
            # Remove elements previous to a in d
            idx_rem = d.index(a)
            d = d[idx_rem+1:]
            d.append(a) # add the last element
            count += 1 + (len(d) -1) # count current element + already existing

    # END
    return count


# Another try: avoid checking two times for a in d
# Performance not totally fulfilled... https://app.codility.com/demo/results/trainingDQNKSZ-P4C/
def solution(M, A):
    if len(A) == 1: return 1

    count = 0
    d = []  # list where we keep the seen elements

    # Initialize counter and list
    count += 1
    d.append(A[0])

    for i, a in enumerate(A[1:]):

        try:
            # element is seen already.
            # Remove elements previous to a in d
            idx_rem = d.index(a)
            d = d[idx_rem + 1:]
            d.append(a)  # add the last element
            count += 1 + (len(d) - 1)  # count current element + already existing

        except ValueError: # element a does not exists in d
            d.append(a)
            count += 1 + (len(d) - 1)  # always count current element + new slices

    # END
    return count





A = [3,4,5,5,2]
solution(6,A) # 9

A = [3,4,5,5,5,2]
solution(6,A) # 10

A = [1]
solution(1,A) # 1

A = [1,0]
solution(1,A) # 3

A = [1,2,1]
solution(10,A) # 5