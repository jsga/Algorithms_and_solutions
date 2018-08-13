'''
An array A consisting of N integers is given. A triplet (P, Q, R) is triangular if it is possible to build a triangle with sides of lengths A[P], A[Q] and A[R]. In other words, triplet (P, Q, R) is triangular if 0 ≤ P < Q < R < N and:

A[P] + A[Q] > A[R],
A[Q] + A[R] > A[P],
A[R] + A[P] > A[Q].
For example, consider array A such that:

  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 12
There are four triangular triplets that can be constructed from elements of this array, namely (0, 2, 4), (0, 2, 5), (0, 4, 5), and (2, 4, 5).

Write a function:

def solution(A)

that, given an array A consisting of N integers, returns the number of triangular triplets in this array.

For example, given array A such that:

  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 12
the function should return 4, as explained above.

Assume that:

N is an integer within the range [0..1,000];
each element of array A is an integer within the range [1..1,000,000,000].
Complexity:

expected worst-case time complexity is O(N2);
expected worst-case space complexity is O(N) (not counting the storage required for input arguments).

'''


# Brute force (with early start). Too easy not to try.
# Notice that the order of indexes is not really relevant (well, except for P=Q and so on, which is not allowed)
# So we start by sorting A: O(nlogn)
# Early stop: if one element to the right is not fulfilling the triangle condition then the ones further away won't wither
# We can implement this in index K and in K
# Still this is O(N**3)
def solution(A):

    # Special case
    if len(A) < 3:
        return 0

    # Sort
    A.sort(reverse=True)
    count = 0

    # Start counting from the max until a no-triangle is found.
    for i in range(0, len(A) - 2):
        for j in range(i+1,len(A)-1):

            # Check for early stop
            if A[i] - A[j] > A[j]:
                break
            else:
                 # Look towards the rest of the possible triangles
                for k in range(j+1,len(A)):

                    if A[i] + A[j] > A[k] and A[j] + A[k] > A[i] and A[k] + A[i] > A[j] :
                        count += 1
                        print('i: ' + str(i) + ' j:' + str(j) + ' k: ' + str(k))
                    else:
                        break # early stop

    return count


# Follow the exercise in the documentation. This almost the same.
# The Caterpillar here is [y,z]. We move one at a time (either y or z)
# Once z if fixed all the solutions in between are satisfied
# https://app.codility.com/demo/results/training2H47SM-V9K/

# Warning! Aorting the array in the opposite direction changes the conditions (see the documentation). In that case as z moves along conditions are not
# necessarily satisfied.

def solution(A):

    # Special case
    if len(A) < 3:
        return 0

    # Sort
    A.sort()

    # Start loop
    n = len(A)
    result = 0
    for x in range(0,n-2):
        # For each element:
        z = x + 2 # end of caterpillar
        for y in range(x + 1, n-1):
            # Move z (end of caterpillar)
            while z < n and A[x] + A[y] > A[z]:# and A[y] + A[z] > A[x] and  A[z] + A[x] > A[y]:
                z += 1
            #print('x = ' + str(x) + ' y = ' + str(y) +  ' z = '+str(z) + '  add count: ' + str(z - y - 1))
            result += z - y - 1

    return result


A = [10,2,5,1,8,12]
solution(A) # 4
solution2(A) # 4


A = [3, 3, 5, 6]
solution(A) # 3
solution2(A)

A = [10,8,5]
solution(A) # 1

A = [10,2,2]
solution(A) # 0
