'''
An array A consisting of N integers is given. The dominator of array A is the value that occurs in more than half of the elements of A.

For example, consider array A such that

 A[0] = 3    A[1] = 4    A[2] =  3
 A[3] = 2    A[4] = 3    A[5] = -1
 A[6] = 3    A[7] = 3
The dominator of A is 3 because it occurs in 5 out of 8 elements of A (namely in those with indices 0, 2, 4, 6 and 7) and 5 is more than a half of 8.

Write a function

def solution(A)

that, given an array A consisting of N integers, returns index of any element of array A in which the dominator of A occurs. The function should return −1 if array A does not have a dominator.

Assume that:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].
For example, given array A such that

 A[0] = 3    A[1] = 4    A[2] =  3
 A[3] = 2    A[4] = 3    A[5] = -1
 A[6] = 3    A[7] = 3
the function may return 0, 2, 4, 6 or 7, as explained above.

Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(1) (not counting the storage required for input arguments).
'''

# Too slow. find another way.
# https://app.codility.com/demo/results/trainingV5H94R-DSP/
def solution(A):

	N = len(A)
	idx = [] # initialize solution

	for i in range(0,N):
		idx_aux = [i] # store temporarily the indexes

		# loop over the remaining array
		for j in range(i+1, N):
			if A[i] == A[j]:
				idx_aux.append(j)

		# Replace if bigger counting has been found
		if len(idx_aux) > len(idx):
			idx = idx_aux

		if len(idx) > (N / 2):  # early stop if found
			return idx[-1]

	if len(idx) > (N / 2):
		return idx[-1]
	else:
		return -1



def solution(A):

	N = len(A)
	count = 0
	domin_element = []
	domin_idx = 0

	for i in range(0,N):

		if count == 0:
			# Add dominant
			domin_element = A[i]
			domin_idx = i
			count = 1
		else:
			if A[i] == domin_element:
				count += 1
			else:
				count -= 1
		print('iter: ' + str(i) + ' count:' + str(count) + '  domin_element:' + str(domin_element) + ' domin_idx:'  +str(domin_idx))

	# Count must be 2 for sure.
	# If it is 1 then we need some more checks...
	if count >= 2:
		return domin_idx
	elif len( [number for number in A if number == domin_element]) > N//2:
		return domin_idx
	else:
		return -1


A = [3,4,3,2,3,-1,3,3]
solution(A) # 0, 2, 4, 6 and 7

A = [1,1,1,1,1]
solution(A)

A = [1,2,3,4]
solution(A)

A = [1,2,1,2,3]
solution(A)

A = [1,2,1]
solution(A)


