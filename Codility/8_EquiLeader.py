'''
A non-empty array A consisting of N integers is given.

The leader of this array is the value that occurs in more than half of the elements of A.

An equi leader is an index S such that 0 ≤ S < N − 1 and two sequences A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N − 1] have leaders of the same value.

For example, given array A such that:

    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2
we can find two equi leaders:

0, because sequences: (4) and (3, 4, 4, 4, 2) have the same leader, whose value is 4.
2, because sequences: (4, 3, 4) and (4, 4, 2) have the same leader, whose value is 4.
The goal is to count the number of equi leaders.

Write a function:

def solution(A)

that, given a non-empty array A consisting of N integers, returns the number of equi leaders.

For example, given:

    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2
the function should return 2, as explained above.

Assume that:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000,000..1,000,000,000].
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(N) (not counting the storage required for input arguments).
'''



# O(N**2). Re-using function from previous exercise.
def solution(A):

	# Define helpder funtion to return leader
	def leader(S):
		A_len = len(S)
		candidate = -1
		candidate_count = 0
		candidate_index = -1

		for index in range(0, A_len):
			if candidate_count == 0:
				candidate = S[index]
				candidate_index = index
				candidate_count += 1
			else:
				if S[index] == candidate:
					candidate_count += 1
				else:
					candidate_count -= 1

		if len([number for number in S if number == candidate]) <= (A_len // 2):
			return -1
		else:
			return candidate


	count = 0
	# Leaders of first and second part
	for i in range(0,len(A)):

		# Part 1 and 2
		l1 = leader(A[:(i+1)])
		l2 = leader(A[i+1:])
		# Same leader: keep count
		if l1 == l2 and l1 != -1 and l2 != -1:
			count += 1
			print('Equileader at ' + str(i))
		else:
			print('i=' + str(i) + ' l1 = '+ str(l1) + ' l2=' + str(l2))
	return count



# Faster but not enough! FUCK
def solution(A):

	# Define helpder funtion to return leader
	def leader_n(S):

		candidate = -1
		candidate_count = 0
		sol = [] # keep a list of leader up to the index

		for index in range(0, len(S)):
			if candidate_count == 0:
				candidate = S[index]
				candidate_count += 1
			else:
				if S[index] == candidate:
					candidate_count += 1
				else:
					candidate_count -= 1

			if len([n for n in S[:(index+1)] if n == candidate]) > (len(S[:(index+1)]) / 2):
				sol.append(candidate)
			else:
				sol.append(-1)
		return sol

	# Forward leader
	for_l = leader_n(A)
	back_l = leader_n(A[::-1])

	# find elements that are the same
	count = 0
	for i in range(0,len(for_l)-1):
		#print('forw: ' + str(for_l[i]) +' back: '+ str(back_l[len(for_l) - i - 2]))

		if for_l[i] == back_l[len(for_l) - i - 2] and for_l[i] != -1 and back_l[len(for_l) - i - 2] != -1:
			count += 1

	return count


A = [4,3,4,4,4,2]
solution(A) # 2

A = [4, 4, 2, 5, 3, 4, 4, 4]
solution(A) # 3

A = [1,2,3,4,5]
solution(A)