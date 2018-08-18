'''
A DNA sequence can be represented as a string consisting of the letters A, C, G and T, which correspond to the types of successive nucleotides in the sequence. Each nucleotide has an impact factor, which is an integer. Nucleotides of types A, C, G and T have impact factors of 1, 2, 3 and 4, respectively. You are going to answer several queries of the form: What is the minimal impact factor of nucleotides contained in a particular part of the given DNA sequence?

The DNA sequence is given as a non-empty string S = S[0]S[1]...S[N-1] consisting of N characters. There are M queries, which are given in non-empty arrays P and Q, each consisting of M integers. The K-th query (0 ≤ K < M) requires you to find the minimal impact factor of nucleotides contained in the DNA sequence between positions P[K] and Q[K] (inclusive).

For example, consider string S = CAGCCTA and arrays P, Q such that:

    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6
The answers to these M = 3 queries are as follows:

The part of the DNA between positions 2 and 4 contains nucleotides G and C (twice), whose impact factors are 3 and 2 respectively, so the answer is 2.
The part between positions 5 and 5 contains a single nucleotide T, whose impact factor is 4, so the answer is 4.
The part between positions 0 and 6 (the whole string) contains all nucleotides, in particular nucleotide A whose impact factor is 1, so the answer is 1.
Write a function:

def solution(S, P, Q)

that, given a non-empty string S consisting of N characters and two non-empty arrays P and Q consisting of M integers, returns an array consisting of M integers specifying the consecutive answers to all queries.

The sequence should be returned as:

a Results structure (in C), or
a vector of integers (in C++), or
a Results record (in Pascal), or
an array of integers (in any other programming language).
For example, given the string S = CAGCCTA and arrays P, Q such that:

    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6
the function should return the values [2, 4, 1], as explained above.

Assume that:

N is an integer within the range [1..100,000];
M is an integer within the range [1..50,000];
each element of arrays P, Q is an integer within the range [0..N − 1];
P[K] ≤ Q[K], where 0 ≤ K < M;
string S consists only of upper-case English letters A, C, G, T.
Complexity:

expected worst-case time complexity is O(N+M);
expected worst-case space complexity is O(N) (not counting the storage required for input arguments).

'''


# The arrays P and Q give the slice of S. Instead of the sum here we are interested in the max of that slice
# The complexity hints that simple loops over S and (P,Q) are allowed

# Idea: What about looping over P and Q, calculating slice_len,
# then for each slice_len, loop over S once and return a solution for each one?
# The solution builds up on top of each other: for slice_len -1 is used to compute slice_len
# Still this is not N + M !

# Another approach:
# Given a couple of ranges P and Q: How many A's are there? We just need one loop over S to calculate this:
# 	do a cum-sum and take the difference in the indexes
# Extend the above for 4 types of letters -> The solution is O(N) for the pre-computing and O(M) due to the number of ranges -> O(M+N)


# https://app.codility.com/demo/results/training47WFJU-THS/
def solution(S,P,Q):

	# Pre-allocate the 4 arrays
	N = len(S) + 1
	SA ,SC , SG , ST = [0] * N, [0] * N, [0] * N, [0] * N

	if S[0] == "A":
		SA[1] =  1
	elif S[0] == "C":
		SC[1] =  1
	elif S[0] == "G":
		SG[1] =  1
	elif S[0] == "T":
		ST[1] =  1

	for i in range(2,len(S)+1):
		if S[i-1] == "A": SA[i] = SA[i-1] + 1
		else: SA[i] = SA[i-1]

		if S[i-1] == "C": SC[i] = SC[i-1] + 1
		else: SC[i] = SC[i-1]

		if S[i-1] == "G": SG[i] = SG[i-1] + 1
		else: SG[i] = SG[i-1]

		if S[i-1] == "T": ST[i] = ST[i-1] + 1
		else: ST[i] = ST[i-1]

	# Loop over M and keep difference in indexes
	sol = [-1]*len(P)

	for i in range(0,len(P)):
		p = P[i]
		q = Q[i]+1

		# Start by A then C,G T:
		if SA[q] - SA[p] > 0:
			sol[i] = 1

		elif SC[q] - SC[p] > 0:
			sol[i] = 2

		elif SG[q] - SG[p] > 0:
			sol[i] = 3

		elif ST[q] - ST[p] > 0:
			sol[i] = 4
	# END
	return sol



S,P,Q = 'CAGCCTA', [2, 5, 0], [4, 5, 6]
solution(S,P,Q) # [2, 4, 1]

S,P,Q ='TC', [0, 0, 1], [0, 1, 1]
solution(S,P,Q) # 4,2,2

S,P,Q ='T', [0, 0, 0], [0, 0,0]
solution(S,P,Q) # 4,4,4

S,P,Q = 'AC', [0, 0, 1], [0, 1, 1]
solution(S,P,Q) # 1 1 2

S,P,Q = 'AAT', [0, 0, 1], [0, 1, 2]
solution(S,P,Q) # 1 1 1



# Straightforward not-performing-well solution

# O(M*N)
def solution(S, P, Q):

	# Translate char to int first
	char_to_int = {'A':1, 'C':2, 'G':3 ,'T':4}
	Si = [char_to_int[s] for s in S]

	M = len(P) # length query
	sol = []
	for k in range(M):
		print('\titer k = ' + str(k))
		# Cut string
		if P[k] == Q[k]:
			sol.append(Si[P[k]]) # Single number
			continue
		else:
			str_cut = Si[P[k]:(Q[k]+1)]
			# Find lowest impact.
			sol.append(min(str_cut))
		print(str(sol))
	return sol

# Not the most efficient -> the "min" makes it M*N