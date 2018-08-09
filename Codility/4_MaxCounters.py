'''
You are given N counters, initially set to 0, and you have two possible operations on them:

increase(X) − counter X is increased by 1,
max counter − all counters are set to the maximum value of any counter.
A non-empty array A of M integers is given. This array represents consecutive operations:

if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
if A[K] = N + 1 then operation K is max counter.
For example, given integer N = 5 and array A such that:

	A[0] = 3
	A[1] = 4
	A[2] = 4
	A[3] = 6
	A[4] = 1
	A[5] = 4
	A[6] = 4
the values of the counters after each consecutive operation will be:

	(0, 0, 1, 0, 0)
	(0, 0, 1, 1, 0)
	(0, 0, 1, 2, 0)
	(2, 2, 2, 2, 2)
	(3, 2, 2, 2, 2)
	(3, 2, 2, 3, 2)
	(3, 2, 2, 4, 2)
The goal is to calculate the value of every counter after all operations.

Write a function:

def solution(N, A)

that, given an integer N and a non-empty array A consisting of M integers, returns a sequence of integers representing the values of the counters.

The sequence should be returned as:

a structure Results (in C), or
a vector of integers (in C++), or
a record Results (in Pascal), or
an array of integers (in any other programming language).
For example, given:

	A[0] = 3
	A[1] = 4
	A[2] = 4
	A[3] = 6
	A[4] = 1
	A[5] = 4
	A[6] = 4
the function should return [3, 2, 2, 4, 2], as explained above.

Assume that:

N and M are integers within the range [1..100,000];
each element of array A is an integer within the range [1..N + 1].
Complexity:

expected worst-case time complexity is O(N+M);
expected worst-case space complexity is O(N) (not counting the storage required for input arguments).

'''

# Not O(N)
def solution(N, A):

	# initialize counter solution
	sol = [0]*N
	# Max count so far
	count_max = 0

	for i in range(0,len(A)):
		if A[i] > N:
			# set counters to the max
			sol[:] = [count_max]*N
		else:
			# Modify sol[A[i]-1]
			# If what we modify is equal to the max then add 1 to the max too
			if (sol[A[i]-1]==count_max) | (count_max == 0):
				count_max += 1
			# Increase 1 the count
			sol[A[i]-1] += 1

		print('Iter: ' + str(i) + '  sol: ' + str(sol)  + '  count_max = ' + str(count_max))

	return sol




A = [3,4,4,6,1,4,4]
N = 5
solution(N,A) #  [3, 2, 2, 4, 2]

A = [3,4,4,6,1,4,4,6]
N = 5
solution(N,A) #

A = [2, 1, 1, 2, 1]
N = 1
solution(N,A)

A = [1,2,3,4,5,6,7]
N = 8
solution(N,A)

A = [8, 6, 6, 6, 6, 1,6,1]
N = 7
solution(N,A)

A = [8,8,8,1,1,2,2,3,3,1,2,3,5]
N = 7
solution(N,A)