# coding=utf-8
"""
A small frog wants to get to the other side of a river. The frog is initially located on one bank of the river (position 0) and wants to get to the opposite bank (position X+1). Leaves fall from a tree onto the surface of the river.

You are given an array A consisting of N integers representing the falling leaves. A[K] represents the position where one leaf falls at time K, measured in seconds.

The goal is to find the earliest time when the frog can jump to the other side of the river. The frog can cross only when leaves appear at every position across the river from 1 to X
(that is, we want to find the earliest moment when all the positions from 1 to X are covered by leaves). You may assume that the speed of the current in the river is negligibly small, i.e. the leaves do not change their positions once they fall in the river.

For example, you are given integer X = 5 and array A such that:

  A[0] = 1
  A[1] = 3
  A[2] = 1
  A[3] = 4
  A[4] = 2
  A[5] = 3
  A[6] = 5
  A[7] = 4
In second 6, a leaf falls into position 5. This is the earliest time when leaves appear in every position across the river.

Write a function:

def solution(X, A)

that, given a non-empty array A consisting of N integers and integer X, returns the earliest time when the frog can jump to the other side of the river.

If the frog is never able to jump to the other side of the river, the function should return −1.

For example, given X = 5 and array A such that:

  A[0] = 1
  A[1] = 3
  A[2] = 1
  A[3] = 4
  A[4] = 2
  A[5] = 3
  A[6] = 5
  A[7] = 4
the function should return 6, as explained above.

Assume that:

N and X are integers within the range [1..100,000];
each element of array A is an integer within the range [1..X].
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(X) (not counting the storage required for input arguments).
"""


# Hash table. Store found indexes in an array
# https://app.codility.com/demo/results/trainingQXXFMF-BEF/
def solution(X,A):

    leaf = [0]*X
    tot = 0

    for i,a in enumerate(A):

        # Check if new leaf on new position
        if leaf[a-1]==0:
            leaf[a-1] = 1
            tot += 1
        # Check if total has been reached
        if tot == X:
            return i # in the last iteration so no need to add a +1
    # never reached the end
    return -1

A = [1,3,1,4,2,3,5,4]
X = 5
solution(X,A) # 6

A = [1,3,1,4,2,3,1,4]
X = 5
solution(X,A) # -1

A  = [1]
X = 1
solution(X,A) # 0
