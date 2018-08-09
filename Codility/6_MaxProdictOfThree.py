'''
A non-empty array A consisting of N integers is given. The product of triplet (P, Q, R) equates to A[P] * A[Q] * A[R] (0 ≤ P < Q < R < N).

For example, array A such that:

  A[0] = -3
  A[1] = 1
  A[2] = 2
  A[3] = -2
  A[4] = 5
  A[5] = 6
contains the following example triplets:

(0, 1, 2), product is −3 * 1 * 2 = −6
(1, 2, 4), product is 1 * 2 * 5 = 10
(2, 4, 5), product is 2 * 5 * 6 = 60
Your goal is to find the maximal product of any triplet.

Write a function:

def solution(A)

that, given a non-empty array A, returns the value of the maximal product of any triplet.

For example, given array A such that:

  A[0] = -3
  A[1] = 1
  A[2] = 2
  A[3] = -2
  A[4] = 5
  A[5] = 6
the function should return 60, as the product of triplet (2, 4, 5) is maximal.

Assume that:

N is an integer within the range [3..100,000];
each element of array A is an integer within the range [−1,000..1,000].
Complexity:

expected worst-case time complexity is O(N*log(N));
expected worst-case space complexity is O(1) (not counting the storage required for input arguments).
'''

def solution(A):
	# Sort with index
	# Enumerate adds an index
	# Lambda applies a function before sorting
	# So we add an index like (0,3),(1,-1) and sort based on (3) and (4)
	A2 = sorted(enumerate(A), key=lambda x: x[1])
	# +++ product
	p1 = A2[-1][1] * A2[-2][1] * A2[-3][1]
	# --+ prodct
	p2 = A2[0][1] * A2[1][1] * A2[-1][1]

	if p1 > p2:
		return p1
	else:
		return p2



A = [-3,1,2,-1,5,6] # [2,4,5]
solution(A)

A = [-3,1,2,-1,5,-12] # [0,4,5]
solution(A)
