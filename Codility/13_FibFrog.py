"""
The Fibonacci sequence is defined using the following recursive formula:

    F(0) = 0
    F(1) = 1
    F(M) = F(M - 1) + F(M - 2) if M >= 2
A small frog wants to get to the other side of a river. The frog is initially located at one bank of the river (position −1) and wants to get to the other bank (position N). The frog can jump over any distance F(K), where F(K) is the K-th Fibonacci number. Luckily, there are many leaves on the river, and the frog can jump between the leaves, but only in the direction of the bank at position N.

The leaves on the river are represented in an array A consisting of N integers. Consecutive elements of array A represent consecutive positions from 0 to N − 1 on the river. Array A contains only 0s and/or 1s:

0 represents a position without a leaf;
1 represents a position containing a leaf.
The goal is to count the minimum number of jumps in which the frog can get to the other side of the river (from position −1 to position N). The frog can jump between positions −1 and N (the banks of the river) and every position containing a leaf.

For example, consider array A such that:

    A[0] = 0
    A[1] = 0
    A[2] = 0
    A[3] = 1
    A[4] = 1
    A[5] = 0
    A[6] = 1
    A[7] = 0
    A[8] = 0
    A[9] = 0
    A[10] = 0
The frog can make three jumps of length F(5) = 5, F(3) = 2 and F(5) = 5.

Write a function:

def solution(A)

that, given an array A consisting of N integers, returns the minimum number of jumps by which the frog can get to the other side of the river. If the frog cannot reach the other side of the river, the function should return −1.

For example, given:

    A[0] = 0
    A[1] = 0
    A[2] = 0
    A[3] = 1
    A[4] = 1
    A[5] = 0
    A[6] = 1
    A[7] = 0
    A[8] = 0
    A[9] = 0
    A[10] = 0
the function should return 3, as explained above.

Assume that:

N is an integer within the range [0..100,000];
each element of array A is an integer that can have one of the following values: 0, 1.
Complexity:

expected worst-case time complexity is O(N*log(N));
expected worst-case space complexity is O(N) (not counting the storage required for input arguments).
"""


# https://app.codility.com/demo/results/trainingMWXSJZ-FZM/
# 91%

def solution(A):

	# Create Fibonacci numbers up to len(A). Create a set. log(n)
	F = []
	F.append(1)
	F.append(2)
	s = 3
	while s <= len(A)+1:
		F.append(s)
		s = F[-1] + F[-2]

	# Start with the loop
	st = [-1] # Stack of possible positions
	count = 0 # count jumps

	while st:

		st_new = [] # new possible jumps of the frog
		for pos in st:

			# From each possible position: where can we go? Keep those numbers in the stack
			i = len(F)-1 # index of the Fib number. Start by the biggest
			while i >=0:
				if pos + F[i] <= len(A):
					if pos + F[i] == len(A):
						print('END')
						return count + 1

					elif A[pos + F[i]] == 1:
						st_new.append(pos + F[i])
				i -= 1
			print('from pos ' + str(pos) + ' the frog jumps to ' + str(st_new)) # indexes where the frog can be

		# Replace stacks
		st = st_new[:] # TODO: remove this replacement and use a single one

		# Add 1 jump
		count += 1

		print('st = ' + str(st) + ' count = ' + str(count))

		# If the stack is empty then we cannot reach te end
		if len(st) == 0:
			return -1

	# END
	return count


A = [1,0,0,1,1,0,1,0,0,0,0]
solution(A) # 3

A = [0,0,0,0,1]
solution(A) # 2. We do a last jump

A = [0,0,0,0]
solution(A) # 1 a single jump

A = [1, 1, 0, 0, 0]
solution(A) # 2

A = [1,1]
solution(A) # 1

A = [0,0,0,0,0] # 6 jumps -> not proper stopping criteria
solution(A)

A = [0,0,0,0] # 1
solution(A)

