# coding=utf-8
"""
You are given two non-empty arrays A and B consisting of N integers. These arrays represent N planks. More precisely, A[K] is the start and B[K] the end of the K−th plank.

Next, you are given a non-empty array C consisting of M integers. This array represents M nails. More precisely, C[I] is the position where you can hammer in the I−th nail.

We say that a plank (A[K], B[K]) is nailed if there exists a nail C[I] such that A[K] ≤ C[I] ≤ B[K].

The goal is to find the minimum number of nails that must be used until all the planks are nailed. In other words, you should find a value J such that all planks will be nailed after using only the first J nails. More precisely, for every plank (A[K], B[K]) such that 0 ≤ K < N, there should exist a nail C[I] such that I < J and A[K] ≤ C[I] ≤ B[K].

For example, given arrays A, B such that:

    A[0] = 1    B[0] = 4
    A[1] = 4    B[1] = 5
    A[2] = 5    B[2] = 9
    A[3] = 8    B[3] = 10
four planks are represented: [1, 4], [4, 5], [5, 9] and [8, 10].

Given array C such that:

    C[0] = 4
    C[1] = 6
    C[2] = 7
    C[3] = 10
    C[4] = 2
if we use the following nails:

0, then planks [1, 4] and [4, 5] will both be nailed.
0, 1, then planks [1, 4], [4, 5] and [5, 9] will be nailed.
0, 1, 2, then planks [1, 4], [4, 5] and [5, 9] will be nailed.
0, 1, 2, 3, then all the planks will be nailed.
Thus, four is the minimum number of nails that, used sequentially, allow all the planks to be nailed.

Write a function:

def solution(A, B, C)

that, given two non-empty arrays A and B consisting of N integers and a non-empty array C consisting of M integers, returns the minimum number of nails that, used sequentially, allow all the planks to be nailed.

If it is not possible to nail all the planks, the function should return −1.

For example, given arrays A, B, C such that:

    A[0] = 1    B[0] = 4
    A[1] = 4    B[1] = 5
    A[2] = 5    B[2] = 9
    A[3] = 8    B[3] = 10

    C[0] = 4
    C[1] = 6
    C[2] = 7
    C[3] = 10
    C[4] = 2
the function should return 4, as explained above.

Assume that:

N and M are integers within the range [1..30,000];
each element of arrays A, B, C is an integer within the range [1..2*M];
A[K] ≤ B[K].
Complexity:

expected worst-case time complexity is O((N+M)*log(M));
expected worst-case space complexity is O(M) (not counting the storage required for input arguments).
"""

# Brute solution
# For each plank: what are the nails that can be used?
# Keep a record of them and save the one with lowest index.
# Return the max index (unless -1)

# https://app.codility.com/demo/results/trainingWNKHFE-EX7/
# The solution is 100% correct but not performing well
def solution(A,B,C):

    # keep index for planks and their corresponding nail
    maxC = len(C)+1 # maximum+1 index
    nail_idx = [maxC]*len(A)

    # For each plank, A and B
    for i in range(0,len(A)):
        a = A[i]
        b = B[i]
        for j,c in enumerate(C):
            if c >= a and c <= b:  # nail found. Keep always the min index
                nail_idx[i] = min(nail_idx[i],j)
        # early stop if no nails found
        if nail_idx[i] == maxC:
            return -1

    # Find max index
    return max(nail_idx)+1

# Idea: do a binary search on the inner loop (TODO)



A = [1,4,5,8]
B = [4,5,9,10]
C = [4,6,7,10,2]
solution(A,B,C) # 4


A = [1,4,5,8]
B = [4,5,9,10]
C = [4,6,7,12]
solution(A,B,C) # -1

A = [1,4]
B = [4,5]
C = [4]
solution(A,B,C) # 1

A = [1,4]
B = [4,5]
C = [10,4]
solution(A,B,C) # 2