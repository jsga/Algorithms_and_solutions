'''
Write a function:

def solution(A, B, K)

that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:

{ i : A ≤ i ≤ B, i mod K = 0 }

For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.

Assume that:

A and B are integers within the range [0..2,000,000,000];
K is an integer within the range [1..2,000,000,000];
A ≤ B.
Complexity:

expected worst-case time complexity is O(1);
expected worst-case space complexity is O(1).
'''


def solution(A, B, K):
	# This is a purely math problem since O(1) is required
	if A % K == 0:
		sol = 1 + int((B - A ) / K)
	else:
		sol = int( (B - (A - (A % K) )) / K) # it's similar to doing a "ceil" function

	return sol

A, B, K = 6, 11,2
solution(A,B,K) # 3

A, B, K = 5, 12,2
solution(A,B,K) # 4

A, B, K = 6, 12,6
solution(A,B,K) # 2

A, B, K = 0, 0,11
solution(A,B,K) # 1

A, B, K = 1, 1,11
solution(A,B,K) # 0

A, B, K = 10, 10,5
solution(A,B,K) # 1

A, B, K = 6, 6, 1
solution(A,B,K) # 1




