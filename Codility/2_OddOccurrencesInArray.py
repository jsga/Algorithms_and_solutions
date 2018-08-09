'''
A non-empty array A consisting of N integers is given. The array contains an odd number of elements, and each element of the array can be paired with another element that has the same value, except for one element that is left unpaired.

For example, in array A such that:

  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9
the elements at indexes 0 and 2 have value 9,
the elements at indexes 1 and 3 have value 3,
the elements at indexes 4 and 6 have value 9,
the element at index 5 has value 7 and is unpaired.
Write a function:

def solution(A)

that, given an array A consisting of N integers fulfilling the above conditions, returns the value of the unpaired element.

For example, given array A such that:

  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9
the function should return 7, as explained in the example above.

Assume that:

N is an odd integer within the range [1..1,000,000];
each element of array A is an integer within the range [1..1,000,000,000];
all but one of the values in A occur an even number of times.
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(1) (not counting the storage required for input arguments).
'''



# N**2 or NlogN
def solution(A):

	found = []

	for i in range(len(A)):

		if A[i] in found:
			found.pop(found.index(A[i]))
		else:
			found.append(A[i])
	return found


solution([9,3,7,3,9])

solution([9,3,7,3,9,4,4,6])

solution([9,3,7,3,9,4,4,7,6])


# Understandind the bitwise operators in Python
# Same
5^4^7^6^5
(5^4^7^6)^5
(5^4)^7^6^5

#
9^3^7^3^9
9^3^7^3^9^4
7^4
# Bitwise: XOR
"{0:b}".format(7) # 111
"{0:b}".format(9) # 100
# XOR should be 011, which is 3

"{0:b}".format(-9) # 100

10 << 2 # 1010 shifted 2 places left: 101000 32 + 8 = 40

10 & 1 # even
11 & 1 # odd