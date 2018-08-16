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

# Easy solution and correct. Not performing well for big test case.
# https://app.codility.com/demo/results/training9U3R4W-8T7/
def solution(N,A):

    # Initialize max counter and solution array
    maxc = 0
    sol = [0]*N

    # Loop through A and record
    for i,a in enumerate(A):

        if a <= N:
            # add a single counter and update max
            sol[a-1] += 1 # Careful with the index
            maxc = max(maxc, sol[a-1])
        else:
            # Reset all counters to the max
            sol = [maxc]*N
        #print(sol)

    # END
    return sol

# The key idea is to keep a minimum counter, so that we know if we add 1 or instead minimum+1
# Do not update all values when the max counter is set.

# https://app.codility.com/demo/results/trainingEWDCE9-XBX/
def solution(N, A):

    sol = [0] * N
    maximum = 0
    minimum = 0

    # step through the array of instructions
    for a in A:
        if a <= N:
            # A minimum value was set
            sol[a-1] = max(minimum,sol[a-1])

            # Add 1
            sol[a-1] += 1

            # update the maximum
            maximum = max(sol[a-1],maximum)
        else:
            # an update-all instruction resets the minimum
            minimum = maximum

        print(str(sol) + ' min = ' + str(minimum) + ' max = ' + str(maximum))

    # set any counters below the minimum to the minimum
    sol = [max(s,minimum) for s in sol]

    # END
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