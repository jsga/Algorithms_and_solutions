'''
https://app.codility.com/programmers/lessons/5-prefix_sums/passing_cars/

Task description
A non-empty array A consisting of N integers is given. The consecutive elements of array A represent consecutive cars on a road.

Array A contains only 0s and/or 1s:

0 represents a car traveling east,
1 represents a car traveling west.
The goal is to count passing cars. We say that a pair of cars (P, Q), where 0 ≤ P < Q < N, is passing when P is traveling to the east and Q is traveling to the west.

For example, consider array A such that:

  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1
We have five pairs of passing cars: (0, 1), (0, 3), (0, 4), (2, 3), (2, 4).

Write a function:

def solution(A)

that, given a non-empty array A of N integers, returns the number of pairs of passing cars.

The function should return −1 if the number of pairs of passing cars exceeds 1,000,000,000.

For example, given:

  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1
the function should return 5, as explained above.

Assume that:

N is an integer within the range [1..100,000];
each element of array A is an integer that can have one of the following values: 0, 1.
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(1) (not counting the storage required for input arguments).
'''

# Approach 1: 100% correct, 0% performance: n**2 complexity
def solution_n2(A):
    # write your code in Python 3.6
    count = 0
    N = len(A)
    for i in range(N):
        #print('iter ' + str(i) + '  A = ' + str(A))

        # check max count
        if count > 1000000000:
            return -1
        # now count pairs left
        if A[0] == 1:
            A.pop(0)
            continue
        else:
            count += sum(A)
            A.pop(0)
    return(count)

# Approach 2: 100% score
def solution(A):
    # write your code in Python 3.6
    count = 0
    N = len(A)
    n_prev0 = 0 # number of previous zeroes

    for i in range(N):

        # check max count
        if count > 1000000000:
            return -1

        # now count pairs left
        if A[i] == 1 :
            count += n_prev0
            continue
        else:
            n_prev0 += 1
    return(count)



# My own tests
A = [0,1,0,1,1]
solution(A)

A = [0,1]
solution(A)

A = [1,0]
solution(A)

A = [0,1,0,1,0,0,0,0,0,1]
solution(A)
solution_n2(A)

A = [0]
solution(A)

A = [1]
solution(A)