'''
Write a function

def solution(A)

that, given an array A consisting of N integers, returns the number of distinct values in array A.

Assume that:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
For example, given array A consisting of six elements such that:

 A[0] = 2    A[1] = 1    A[2] = 1
 A[3] = 2    A[4] = 3    A[5] = 1
the function should return 3, because there are 3 distinct values appearing in array A, namely 1, 2 and 3.

Complexity:

expected worst-case time complexity is O(N*log(N));
expected worst-case space complexity is O(N) (not counting the storage required for input arguments).
'''

# O(N**2)
def solution2(A):

	found = []
	for i in range(len(A)):
		if A[0] not in found:
			found.append(A[0])
		A.pop(0)
		print('Iter: ' + str(i) + ' A: ' + str(A) +  ' Found:' + str(found))

	return len(found)


# O(NlogN)
def solution(A):

	if len(A)==0:
		return 0
	A.sort()
	count = 1

	for i in range(1,len(A)):
		if A[i] == A[i-1]:
			continue
		else:
			count += 1

	return count


A = [1,1,2,2,3,3,1,1]
solution(A)

A = [1,1,1,1,1,1]
solution(A)

A = [1,2,3,4,5]
solution(A)

A = [1]
solution(A)

