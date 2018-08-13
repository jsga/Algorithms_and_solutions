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
# In this case the check is whether we can divide A, such that the max sum is less than m. Return maximum number of block.
# Each block might be of different length

def check(A,maxB):

    nb = 1 # number of blocks. If maxB is very large nb is 1
    pos = A[0] # Start
    s = pos # keep track of sum

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
    # The largest sum is (worse case) sum(A)
    # The lowest (best scenario): M
    #M = max(A)
    if M == 0: return 0
    elif M > len(A): return M

    sumA = sum(A)
    m = int((sumA + M)/2) # Starting guess of the sum
    result = [] # keep track of solution

    # Lets find the number of blocks that we can divide A in, called nb
    # If nb is lower than K, increase m
    # if nb is higher, decrease m

    while m <= sumA and m >= M:

        # number of blocks that A can be divided in
        nb = check(A,m)

        if nb > K:
            m += 1
        elif nb < K:
            m -= 1
        else:
            # Exactly K blocks found. Decrease m (always a better solution)
            print('   END  '+'m = ' + str(m) + ' nb =' + str(nb))
            if m not in result:
                result.append(m)
            else:
                break
            m -= 1
        print('m = ' + str(m) + ' nb =' + str(nb))

    print('****')
    return min(result)



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

