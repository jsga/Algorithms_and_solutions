'''
We draw N discs on a plane. The discs are numbered from 0 to N − 1. An array A of N non-negative integers, specifying the radiuses of the discs, is given. The J-th disc is drawn with its center at (J, 0) and radius A[J].

We say that the J-th disc and K-th disc intersect if J ≠ K and the J-th and K-th discs have at least one common point (assuming that the discs contain their borders).

The figure below shows discs drawn for N = 6 and A as follows:

  A[0] = 1
  A[1] = 5
  A[2] = 2
  A[3] = 1
  A[4] = 4
  A[5] = 0


There are eleven (unordered) pairs of discs that intersect, namely:

discs 1 and 4 intersect, and both intersect with all the other discs;
disc 2 also intersects with discs 0 and 3.
Write a function:

def solution(A)

that, given an array A describing N discs as explained above, returns the number of (unordered) pairs of intersecting discs. The function should return −1 if the number of intersecting pairs exceeds 10,000,000.

Given array A shown above, the function should return 11, as explained above.

Assume that:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [0..2,147,483,647].
Complexity:

expected worst-case time complexity is O(N*log(N));
expected worst-case space complexity is O(N) (not counting the storage required for input arguments).
'''



def solution(A):


	# Pre-process and find start and end of discs.
	N = len(A)
	if N == 0:
		return 0

	start = [0]*N
	end = [0]*N

	for i in range(0,N):
		# Crop if disc goes blow 0 or above N
		start[i] = max(0, i - A[i])
		end[i] = min(N, i + A[i] )

	# Sort by start
	start, end = zip(*sorted(zip(start, end)))
	end = list(end)
	start = list(start)

	# Count how many discs ended before the new one starts (new_start <= old_ends)
	count = 0
	aux_end = [] # add or discard

	for i in range(0,N):
		# Find values of end of discs that are higher than the start.
		# If not, remove from the list, they will never intersect again.
		j=0
		while j <= len(aux_end)-1:
			#print('i=' + str(i) + ' j=' + str(j) + ' count=' + str(count) + ' start[i]=' + str(start[i]) +  ' aux_end=' + str(aux_end))
			if aux_end[j] >= start[i]:
				count += 1
				j += 1
			else:
				aux_end.pop(j)
		# Add end of i
		aux_end.append(end[i])

		if count > 10000000:
			return -1

	# END
	return count


# count += len([x for x in end[0:i] if x >= start[i]])


A = [3,1,1,1,0]
solution(A) # 7


A = [1,5,2,1,4,0]
solution(A) # 11

A = []
solution(A)









'''
def solution(A):

	A2 = sorted(enumerate(A), key=lambda x: x[1],reverse=True)
	N = len(A2)
	count = 0
	elint_save = []

	for i in range(0,N):

		# elements that intersect. Careful not to get out of range
		if (A2[i][0] - A2[i][1]) < 0: # Below 0
			if (A2[i][0] + A2[i][1]) > N:
				elint = list(range(0,N))
			else:
				elint = list(range(0, A2[i][0] + A2[i][1]))
		else: # above 0
			if (A2[i][0] + A2[i][1]) > N:
				elint = list(range(A2[i][0] - A2[i][1],N))
			else:
				elint = list(range(A2[i][0] - A2[i][1], A2[i][0] + A2[i][1]))

		elint_save += elint

		# check how many elements have been shown previusly to the left
		prev = [ A2_el[0] for A2_el in A2[0:i]]
		prev.append(A2[i][0])
		prev_found = [k not in prev for k in elint]

		# Add counter
		count += sum(prev_found)

		# count by summing
		print('iter: ' + str(i) + ' count: ' + str(count) + ' elint: ' + str(elint) + ' ' + str(prev_found))

		# Check max counter
		if count > 10000000:
			return -1

	return count


A = [1,5,2,1,4,0]
solution(A)

A = [1,1,1]
solution(A) # should be 3 its 2. FUCK





def solution(A):

	A2 = sorted(enumerate(A), key=lambda x: x[1], reverse=True)
	N = len(A2)
	count = 0

	for i in range(0, N):

		# closing of the disc
		end_i = A2[i][0] + A2[i][1]
		if (A2[i][0] + A2[i][1]) > (N-1):
			end_i = (N-1)

		# for the remaining  of the disks above, count if they intersect
		low_i = 0
		for j in range(A2[i][0], end_i):
			low_i += int(A2[j][0] - A2[j][1] <= end_i)

		count += low_i

		# count by summing
		print('iter: ' + str(i) + ' count: ' + str(count) + ' low_i: ' + str(low_i) )

		# Check max counter
		if count > 10000000:
			return -1

	return count
'''






