'''
An array A consisting of N integers is given. It contains daily prices of a stock share for a period of N consecutive days. If a single share was bought on day P and sold on day Q, where 0 ≤ P ≤ Q < N, then the profit of such transaction is equal to A[Q] − A[P], provided that A[Q] ≥ A[P]. Otherwise, the transaction brings loss of A[P] − A[Q].

For example, consider the following array A consisting of six elements such that:

  A[0] = 23171
  A[1] = 21011
  A[2] = 21123
  A[3] = 21366
  A[4] = 21013
  A[5] = 21367
If a share was bought on day 0 and sold on day 2, a loss of 2048 would occur because A[2] − A[0] = 21123 − 23171 = −2048. If a share was bought on day 4 and sold on day 5, a profit of 354 would occur because A[5] − A[4] = 21367 − 21013 = 354. Maximum possible profit was 356. It would occur if a share was bought on day 1 and sold on day 5.

Write a function,

def solution(A)

that, given an array A consisting of N integers containing daily prices of a stock share for a period of N consecutive days, returns the maximum possible profit from one transaction during this period. The function should return 0 if it was impossible to gain any profit.

For example, given array A consisting of six elements such that:

  A[0] = 23171
  A[1] = 21011
  A[2] = 21123
  A[3] = 21366
  A[4] = 21013
  A[5] = 21367
the function should return 356, as explained above.

Assume that:

N is an integer within the range [0..400,000];
each element of array A is an integer within the range [0..200,000].
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(1) (not counting the storage required for input arguments).
'''


#https://app.codility.com/demo/results/trainingS6QQH7-U9A/

def solution(A):

	profit_so_far = last_transactions = 0


	for i in range(1,len(A)):

		# Find last transaction
		last_prof = A[i] - A[i-1]

		# Update last best
		last_transactions = max(last_prof + last_transactions,last_prof)

		# Best profit of past combined transactions
		profit_so_far = max(profit_so_far,last_prof,last_transactions)

		# Some info
		print(str(i) + ' A[i]=' + str(A[i]) +
		      ' last_prof = ' + str(last_prof) +
		      ' last_transactions = ' + str(last_transactions) +
		      ' profit_so_far = ' + str(profit_so_far))

	# If profit is negative return 0
	return max(0, profit_so_far)


A = [3,1,4,5,2,7]
solution(A) # 6

A = [3,2,6,1,4,5,2]
solution(A) # 4

A = [3,2,1,6,4,5,2]
solution(A) # 5

A = [23171, 21011, 21123, 21366, 21013, 21367]
solution(A) # 365

A = []
solution(A) # 0

A = [11,2,9,1,3]
solution(A) # 7 # this solution doe snot involve either the max or the min

A = [0, 200000]
solution(A) # 200000

A = [1,2,3,4,5,4,3,2,1]
solution(A)

A = [5,4,3,2,1,0,1,2,3,4,5]
solution(A)



# FUCk this is much easier
def solution(A):
	profit = 0
	min_price = 200000
	for i in range(1, len(A)):
		min_price = min(A[i-1], min_price)
		profit = max(profit, A[i] - min_price)
	return profit