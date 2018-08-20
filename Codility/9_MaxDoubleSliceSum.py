'''
A non-empty array A consisting of N integers is given.

A triplet (X, Y, Z), such that 0 ≤ X < Y < Z < N, is called a double slice.

The sum of double slice (X, Y, Z) is the total of A[X + 1] + A[X + 2] + ... + A[Y − 1] + A[Y + 1] + A[Y + 2] + ... + A[Z − 1].

For example, array A such that:

    A[0] = 3
    A[1] = 2
    A[2] = 6
    A[3] = -1
    A[4] = 4
    A[5] = 5
    A[6] = -1
    A[7] = 2
contains the following example double slices:

double slice (0, 3, 6), sum is 2 + 6 + 4 + 5 = 17,
double slice (0, 3, 7), sum is 2 + 6 + 4 + 5 − 1 = 16,
double slice (3, 4, 5), sum is 0.
The goal is to find the maximal sum of any double slice.

Write a function:

def solution(A)

that, given a non-empty array A consisting of N integers, returns the maximal sum of any double slice.

For example, given:

    A[0] = 3
    A[1] = 2
    A[2] = 6
    A[3] = -1
    A[4] = 4
    A[5] = 5
    A[6] = -1
    A[7] = 2
the function should return 17, because no double slice of array A has a sum of greater than 17.

Assume that:

N is an integer within the range [3..100,000];
each element of array A is an integer within the range [−10,000..10,000].
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(N) (not counting the storage required for input arguments).
'''

# O(N**3)
def solution(A):
	max = 0
	N = len(A)
	for i in range(0,N-2):
		for j in range(i+1,N-1):
			for k in range(j+1,N):
				# Do sum and update if higher found
				aux_sum = sum(A[i+1:j] + A[j+1:k])
				if aux_sum > max:
					max = aux_sum
					print('i=' + str(i) + ' j=' + str(j) + ' k=' + str(k))
	return max


# Max slice problem (!!!!) See reading material
# Mostly correct. Some issues with the indexes...
# https://app.codility.com/demo/results/trainingRM7R5U-KVP/
def solution(A):

	# Max slice forward
	max_ending = 0
	max_slice_f = [0]
	for i in range(1,len(A)-2):
		max_ending = max(0, max_ending + A[i])
		max_slice_f.append(max(max_slice_f[i-1], max_ending))

	print(max_slice_f)

	# Max slice backward
	max_ending = 0
	max_slice_b = [0]
	for i in range( len(A)-2,1,-1):
		max_ending = max(0, max_ending + A[i])
		max_slice_b.append(max(max_slice_b[-1], max_ending))

	print(max_slice_b)

	# traverse both arrays and find highest sum
	max_all = 0
	N = len(max_slice_b)
	for i in range(0, N):
		max_all = max(max_all,max_slice_f[i] + max_slice_b[N- i-1])
		print('i=' + str(i) + ' f=' + str(max_slice_f[i]) + ' b=' + str(max_slice_b[N- i-1]))


	#max_slice.pop(0)
	return max_all


A = [3,2,6,-1,4,-5,-2]
solution(A) # 12 (0,3,5) 2+6+4 = 12
solution(A[::-1])


A = [3,2,6,-1,4,5,-1,2]
solution(A)

A = [1,2,3,3,3,10,12]
solution(A) # (0,1,7) 3+3+3+10 = 19



A = [1,1,1]
solution(A)

A = [-1,-1,-10,1,-10,1]
solution(A)

A = [5, 17, 0, 3]
solution(A) # 17