'''
You are given integers K, M and a non-empty array A consisting of N integers. Every element of the array is not greater than M.

You should divide this array into K blocks of consecutive elements. The size of the block is any integer between 0 and N. Every element of the array should belong to some block.

The sum of the block from X to Y equals A[X] + A[X + 1] + ... + A[Y]. The sum of empty block equals 0.

The large sum is the maximal sum of any block.

For example, you are given integers K = 3, M = 5 and array A such that:

  A[0] = 2
  A[1] = 1
  A[2] = 5
  A[3] = 1
  A[4] = 2
  A[5] = 2
  A[6] = 2
The array can be divided, for example, into the following blocks:

[2, 1, 5, 1, 2, 2, 2], [], [] with a large sum of 15;
[2], [1, 5, 1, 2], [2, 2] with a large sum of 9;
[2, 1, 5], [], [1, 2, 2, 2] with a large sum of 8;
[2, 1], [5, 1], [2, 2, 2] with a large sum of 6.
The goal is to minimize the large sum. In the above example, 6 is the minimal large sum.

Write a function:

def solution(K, M, A)

that, given integers K, M and a non-empty array A consisting of N integers, returns the minimal large sum.

For example, given K = 3, M = 5 and array A such that:

  A[0] = 2
  A[1] = 1
  A[2] = 5
  A[3] = 1
  A[4] = 2
  A[5] = 2
  A[6] = 2
the function should return 6, as explained above.

Assume that:

N and K are integers within the range [1..100,000];
M is an integer within the range [0..10,000];
each element of array A is an integer within the range [0..M].
Complexity:

expected worst-case time complexity is O(N*log(N+M));
expected worst-case space complexity is O(1) (not counting the storage required for input arguments).
'''




# We first define the "check" condition (see Codility reading mnaterial)

def check(A,maxB):

    nb = 1 # number of blocks. If maxB is very large nb is 1
    pos = A[0] # Start

    for el in A[1:]:

        if pos + el > maxB:
            # We cannot reach this one so don't extend the block. Close it and re-start
            pos = el
            nb += 1
        else:
            # we can keep on extending the block
            pos += el

    return nb


# Now put together in a binary search:
def solution(K,M, A):

    # Based on binary search algorithm
    # The largest sum is sum(A), i.e. a single block
    # The lowest sum: M or max(A), where the max is in a single block

    max_sumB = sum(A)
    min_sumB = max(A)
    maxB = (max_sumB + min_sumB) // 2
    result = 0

    # Special cases
    if K == 1: return max_sumB
    if K >= len(A): return min_sumB

    # Find the max sum of blocks by binary search
    while min_sumB <= max_sumB:

        maxB = (max_sumB + min_sumB)//2
        nb = check(A,maxB) # min number of blocks with sum of maxB

        print('maxB = ' + str(maxB) + ' nb =' + str(nb) + ' min_sumB = ' + str(min_sumB) + ' max_sumB = ' + str(max_sumB))

        if nb > K:
            # More number of blocks than needed.
            # maxB should be smaller then
            min_sumB = maxB + 1

        elif nb <= K:
            max_sumB = maxB - 1
            result = maxB

    return result



A = [2,1,5,1,2,2,2]
maxB = 9
check(A,maxB) # 2
maxB = 1
check(A,maxB) # 6

# CarefuL. Same result for 6 and 7...
check(A,6)
check(A,7)

K = 3
A = [2,1,5,1,2,2,2]
M = 5#max(A)
solution(K,M,A) # 6

A = [1,1,1,1,1,1,1,1,1,1]
M = 1
K = 3
solution(K,M,A)

A = [1]
M = 1
K = 1
solution(K,M,A)

A = [0,0,0,0]
M = 0
K = 2
solution(K,M,A)

