'''
A non-empty array A consisting of N integers is given. A pair of integers (P, Q), such that 0 ≤ P ≤ Q < N, is called a slice of array A. The sum of a slice (P, Q) is the total of A[P] + A[P+1] + ... + A[Q].

Write a function:

def solution(A)

that, given an array A consisting of N integers, returns the maximum sum of any slice of A.

For example, given array A such that:

A[0] = 3  A[1] = 2  A[2] = -6
A[3] = 4  A[4] = 0
the function should return 5 because:

(3, 4) is a slice of A that has sum 4,
(2, 2) is a slice of A that has sum −6,
(0, 1) is a slice of A that has sum 5,
no other slice of A has sum greater than (0, 1).
Assume that:

N is an integer within the range [1..1,000,000];
each element of array A is an integer within the range [−1,000,000..1,000,000];
the result will be an integer within the range [−2,147,483,648..2,147,483,647].
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(N) (not counting the storage required for input arguments).
'''

def solution(A):

	if len(A)==1:
		return A[0]

	prev_sum = cand_max = total_max = A[0]

	for i in range(1,len(A)):

		prev_sum = A[i] + A[i-1]
		cand_max = max(cand_max + A[i], prev_sum)
		total_max = max(total_max, cand_max,A[i] )

	return total_max


A = [0,3,2,-6,4,0]
solution(A) # 5

A = [1,3,4,-3,-5,10,1]
solution(A) # 11

A = [1]
solution(A)

A = [1,2]
solution(A)

A = [1,-2]
solution(A)


A = [-1,2]
solution(A)

A = [1,1,1]
solution(A)




