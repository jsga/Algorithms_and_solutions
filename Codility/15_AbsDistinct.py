'''
A non-empty array A consisting of N numbers is given. The array is sorted in non-decreasing order. The absolute distinct count of this array is the number of distinct absolute values among the elements of the array.

For example, consider array A such that:

  A[0] = -5
  A[1] = -3
  A[2] = -1
  A[3] =  0
  A[4] =  3
  A[5] =  6
The absolute distinct count of this array is 5, because there are 5 distinct absolute values among the elements of this array, namely 0, 1, 3, 5 and 6.

Write a function:

def solution(A)

that, given a non-empty array A consisting of N numbers, returns absolute distinct count of array A.

For example, given array A such that:

  A[0] = -5
  A[1] = -3
  A[2] = -1
  A[3] =  0
  A[4] =  3
  A[5] =  6
the function should return 5, as explained above.

Assume that:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−2,147,483,648..2,147,483,647];
array A is sorted in non-decreasing order.
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(N) (not counting the storage required for input arguments).
'''


# Keep in mind NON-DECREASING means elements in A might be repeated

# Caterpilar method:
def solution(A):

    # Special case
    if len(A)==1: return 1

    # Keep track of absolute value (1 loop only)
    Ab = [abs(a) for a in A]

    # Index from top and bottom
    up = len(A)-1
    low = 0

    # keep a count
    count = 0

    while up >= low:

        if Ab[up] > Ab[low]:
            count += 1
            # Decrease index until a different element is found
            up -= 1
            while Ab[up] == Ab[up+1] and up >= low:
                up -= 1


        elif Ab[up] < Ab[low]:
            count += 1
            # Increase index until a different element is found
            low += 1
            while Ab[low] == Ab[low-1] and up >= low:
                low += 1

        else:
            count += 1
            # Decrease until new element
            up -= 1
            while Ab[up] == Ab[up+1] and up >= low:
                up -= 1
            # Increase until new element
            low += 1
            while Ab[low] == Ab[low-1] and up >= low:
                low += 1


    return count

# Missing a special case
# https://app.codility.com/demo/results/trainingU6SEFC-TUF/


# This is much better (however not using the theory of caterpilar method!)
def solution(A):

    # Use a set for unique elements
    count = set()
    # Elements are only added if non existing
    for a in A:
        count.add(abs(a))

    return len(count)


A = [-5,-3,-1,0,3,6]
solution(A) #5

A = [1]
solution(A) # 1

A = [1,1,1,1,1]
solution(A) # 1

A = [-1,-1,-1,1,1,1]
solution(A) # 1

A = [-2,-1,0,1,2]
solution(A) # 3

A = [-2,1]
solution(A) # 3