"""
A non-empty array A consisting of N integers is given.

A peak is an array element which is larger than its neighbors. More precisely, it is an index P such that 0 < P < N − 1,  A[P − 1] < A[P] and A[P] > A[P + 1].

For example, the following array A:

    A[0] = 1
    A[1] = 2
    A[2] = 3
    A[3] = 4
    A[4] = 3
    A[5] = 4
    A[6] = 1
    A[7] = 2
    A[8] = 3
    A[9] = 4
    A[10] = 6
    A[11] = 2
has exactly three peaks: 3, 5, 10.

We want to divide this array into blocks containing the same number of elements. More precisely, we want to choose a number K that will yield the following blocks:

A[0], A[1], ..., A[K − 1],
A[K], A[K + 1], ..., A[2K − 1],
...
A[N − K], A[N − K + 1], ..., A[N − 1].
What's more, every block should contain at least one peak. Notice that extreme elements of the blocks (for example A[K − 1] or A[K]) can also be peaks, but only if they have both neighbors (including one in an adjacent blocks).

The goal is to find the maximum number of blocks into which the array A can be divided.

Array A can be divided into blocks as follows:

one block (1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2). This block contains three peaks.
two blocks (1, 2, 3, 4, 3, 4) and (1, 2, 3, 4, 6, 2). Every block has a peak.
three blocks (1, 2, 3, 4), (3, 4, 1, 2), (3, 4, 6, 2). Every block has a peak. Notice in particular that the first block (1, 2, 3, 4) has a peak at A[3],
because A[2] < A[3] > A[4], even though A[4] is in the adjacent block.
However, array A cannot be divided into four blocks, (1, 2, 3), (4, 3, 4), (1, 2, 3) and (4, 6, 2), because the (1, 2, 3) blocks do not contain a peak.
Notice in particular that the (4, 3, 4) block contains two peaks: A[3] and A[5].

The maximum number of blocks that array A can be divided into is three.

Write a function:

def solution(A)

that, given a non-empty array A consisting of N integers, returns the maximum number of blocks into which A can be divided.

If A cannot be divided into some number of blocks, the function should return 0.

For example, given:

    A[0] = 1
    A[1] = 2
    A[2] = 3
    A[3] = 4
    A[4] = 3
    A[5] = 4
    A[6] = 1
    A[7] = 2
    A[8] = 3
    A[9] = 4
    A[10] = 6
    A[11] = 2
the function should return 3, as explained above.

Assume that:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [0..1,000,000,000].
Complexity:

expected worst-case time complexity is O(N*log(log(N)));
expected worst-case space complexity is O(N) (not counting the storage required for input arguments).
"""


def solution(A):

    # Find peaks and save indexes
    N = len(A)
    peak = []
    for i in range(1,N-1):
        if A[i] > A[i-1] and A[i] > A[i+1]:
            peak.append(i)
    print('peaks at:' + str(peak))

    if len(peak) == 0:
        return 0


    # The block must be same length, so N must be divisible by K
    # Iterate through primes
    i=1
    max_K = 0
    while i*i < N or i*i == N:

        if N % i == 0:
            # Two primes found. Check for their possible split
            print('iter = ' + str(i) + ' Primes found: ' + str([i, int(N/i)]) )

            for k in [i, int(N/i)]: # Repeat 2 times

                filled_block = 0
                for j in range(1,k+1): # Here we iterate through each block and count peaks
                    count_block = 0
                    for p in peak:
                        if p >= (j-1)*k and p <= j*k-1:
                            count_block += 1
                    # if at least a peak has been found in this block, mark as filled
                    if count_block >= 1:
                        filled_block += 1

                # If we found peaks in all blocks, update max counter
                if filled_block == N/k:
                    max_K = max(max_K, N/k)
                    print('For prime ' + str(k) + ' blocks OK. Max_k = ' + str(max_K) + ' filled_block = ' + str(filled_block))
                else:
                    print('For prime ' + str(k) + ' blocks not OK. Max_k = ' + str(max_K) + ' filled_block = ' +  str(filled_block))

        # Increase counter
        i += 1

    # END
    return int(max_K)




# https://app.codility.com/demo/results/training54DX8C-Y4J/

def solution(A):

    # Find peaks and save indexes
    N = len(A)
    peak = [0]*N
    for i in range(1,N-1):
        peak[i] = peak[i-1]
        if A[i] > A[i-1] and A[i] > A[i+1]:
            peak[i] += 1
    peak[N-1] = peak[N-2]
    print('peak count:' + str(peak))

    if N == 0 or peak[-1] == 0:
        return 0


    # The block must be same length, so N must be divisible by K
    # Iterate through primes
    i=1
    max_K = 0
    while i*i <= N:

        if N % i == 0:
            # Two primes found. Check for their possible split
            print('iter = ' + str(i) + ' Primes found: ' + str([i, int(N/i)]) )

            for k in [i, int(N/i)]: # For each prime found

                filled_block = 0
                for j in range(1,int(N/k)+1): # Here we iterate through each block and check the peak count
                    #print('i= ' + str(i) + ' k =' + str(k) + ' j=' + str(j))
                    if (peak[j*k-1] - peak[(j-1)*k]) >= 1:
                        filled_block += 1
                        #print('OK')
                    else:
                        break # stop as soon as we cant fill uip the block

                # If we found peaks in all blocks, update max counter
                if filled_block == N/k:
                    max_K = max(max_K, N/k)
                    print('For prime ' + str(k) + ' blocks OK. Max_k = ' + str(max_K) + ' filled_block = ' + str(filled_block) + ' N/k=' + str(N/k))
                else:
                    print('For prime ' + str(k) + ' blocks not OK. Max_k = ' + str(max_K) + ' filled_block = ' +  str(filled_block)+ ' N/k=' + str(N/k))

        # Increase counter
        i += 1

    # END
    return int(max_K)

A = [1,2,3,4,3,4,1,2,3,4,6,2]
solution(A) # 3


A = [1,2,3]
solution(A)

A = [1]
solution(A)

A = [0, 1, 0, 0, 1, 0, 0, 1, 0]
solution(A) # 3

A = [1,3,1,1,1,1,1,1,3,1,1,1]
solution(A) # 2

