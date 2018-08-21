# coding=utf-8
'''
For a given array A of N integers and a sequence S of N integers from the set {−1, 1}, we define val(A, S) as follows:

val(A, S) = |sum{ A[i]*S[i] for i = 0..N−1 }|

(Assume that the sum of zero elements equals zero.)

For a given array A, we are looking for such a sequence S that minimizes val(A,S).

Write a function:

def solution(A)

that, given an array A of N integers, computes the minimum value of val(A,S) from all possible values of val(A,S) for all possible sequences S of N integers from the set {−1, 1}.

For example, given array:

  A[0] =  1
  A[1] =  5
  A[2] =  2
  A[3] = -2
your function should return 0, since for S = [−1, 1, −1, 1], val(A, S) = 0, which is the minimum possible value.

Assume that:

N is an integer within the range [0..20,000];
each element of array A is an integer within the range [−100..100].
Complexity:

expected worst-case time complexity is O(N*max(abs(A))2);
expected worst-case space complexity is O(N+sum(abs(A))) (not counting the storage required for input arguments).
'''


# THe solution is not dynamic in the sense that the solution up to i is not necessarily the same if we add 1 element to the array
# For example consider [3,3]-> solution = 0
# And [3,3,6] sol=0 which is different than [0,6] -> sol = 6
# Different strategy

# Notice the range of A is small. This gives us a hint. An array of size sum(abs(A)) must be created
# Keep in this array the possible solutions as new numbers come up
# When all the possible combinations are obtained: How do we know we have found the answer?

# This solution is based on the fact that S=sum(abs(A)) can be divided in two sets. (one for + another for -).

def solution(A):

        N = len(A)
        M = 0
        for i in range(N):
            A[i] = abs(A[i])
            M = max(A[i], M)

        S = sum(A)
        dp = [0] * (S + 1)
        dp[0] = 1

        for j in range(N):

            for i in range(S, -1, -1):

                if (dp[i] == 1) and (i + A[j] <= S):

                    dp[i + A[j]] = 1

        result = S
        print(dp)

        for i in range(S // 2 + 1):
            if dp[i] == 1:
                result = min(result, S - 2 * i)

        # END
        return result


A = [1,5,2,-2]
solution(A) # 0

A = [1,5,2,-2,10,10]
solution(A) # 0

A = [3, 3, 3, 4, 5]
solution(A)

A = []
solution(A) # 0

A = [2]
solution(A) # 2

A = [1,2]
solution(A) # 1