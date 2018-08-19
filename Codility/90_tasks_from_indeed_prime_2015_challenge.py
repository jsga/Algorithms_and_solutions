"""
Longest password
"""

# 100%
# https://app.codility.com/demo/results/trainingGMCQU8-2G4/

def solution(S):

    # First of all split into words inside a list
    SP = S.split()

    # We loop each element of the list and determine whether it is a valid password and whats the length
    max_l = -1 # keep here the mas


    for s in SP:

        # indicate whether constraints are satisfied
        is_ok = True
        # Count number of letters and numbers
        count_l = 0
        count_n = 0

        for c in s: # for every character in the word

            # Save here whether letters or numbers
            isd = c.isdigit()
            isa = c.isalpha()

            # either one of the other
            if isd or isa:
                pass # OK, satisfies the constraint
            else:
                is_ok = False
                break

            # even number of letters
            if isa:
                count_l += 1
            # Odd number of numbers
            if isd:
                count_n += 1

        # Check constraints, break if not satisfied
        # Valid letters and numbers

        print('check validity')
        if is_ok == False:
            continue

        elif count_l % 2 != 0: # even number letters
            continue

        elif (count_n % 2 -1) != 0:
            continue
        else:
            max_l = max(max_l, len(s))
    # END
    return max_l


S = "test 5 a0A pass007 ?xy1"
solution(S)

S = "test11 52 a0A pass0071 ?xy1"
solution(S)

S = "t1??"
solution(S)

S = ""
solution(S)






"""
Maximum depth of lake
"""

# Dynamic programming
# Make two pre-computations: max_so_far, from left to right
# https://app.codility.com/demo/results/training32FFV6-3BN/

def maxSoFar(A):

    # Keep solution here
    ret = [0]*len(A)
    ret[0] = A[0] # First element is always the max so far
    # Loop
    for i in range(1,len(A)):
        ret[i] = max(ret[i-1], A[i])
    # END
    return ret


def solution(A):

    # Calculate max so far, from left and right
    max_l = maxSoFar(A)
    max_r = maxSoFar(A[::-1])

    # At each spot i, the depth is max minus the rock height
    sol = 0

    for i,a in enumerate(A):
        sol = max(sol, min(max_l[i], max_r[len(A) -1- i]) - a)

    # END
    return sol

A = [1,3,2,1,2,1,5,3,3,4,2]
maxSoFar(A)
solution(A) # 2

A = [1,3]
maxSoFar(A)
solution(A) # 0

A = [1]
maxSoFar(A)
solution(A) # 0

A = [1,4,1,4]
solution(A) # 0




"""
Slalom skiing
"""

# Boils down to finding 3 indexes: x, y z
# x is the starting point
# We maximize:
# the number of elements greater than A[z] and lower than A[y] (consecutive)
# num elements lower than A[y] and greater than A[z]
# num elements greater than A[z]

# O(nlong) could suggest:
# 1. Sorting first and then do some single loops
# 2. Binary search.


# Brute force.
# Brute force: scan all possible combinations of x,y z and return the max count O(N**3)
# Not even correct: when the last element is 2, 11 is selected, not 6 and 9
# https://app.codility.com/demo/results/trainingQBEFA3-WJY/
def solution(A):

    N = len(A)

    # Special case
    if N <= 3:
        return N

    sol = 0

    for i in range(0,N-2):
        for j in range(i+1,N-1):

            # Now calculate gates crossed
            # from start to first turn
            count1 = 0
            aux_A = A[i] # keep track descending slope
            for k in range(i,j):
                if A[k] > aux_A:
                    count1 += 1
                    aux_A = A[k]

            # Try all possible values of the second turn
            for z in range(j+1,N):

                # For each of the values of z, calculate gates in between j and z
                count2 = 0
                aux_A = A[j]  # keep track descending slope
                for k in range(j, z):
                    if A[k] < aux_A:
                        count2 += 1
                        aux_A = A[k]

                # Also calculate leftover turns
                count3 = 0
                aux_A = A[z]  # keep track descending slope
                for k in range(z,N):
                    if A[k] > aux_A:
                        count3 += 1
                        aux_A = A[k]

                # Keep track of max after i,j,z have been set
                sol = max(sol, count1+count2+count3+3)

    # END
    return sol

A = [15,13,5,7,4,10,12,8,2,11,6,9,3]
solution(A) # 8


A = [15,13,5,7,4,10,12,8,2,11,6,9,3]
idx = sorted(range(len(A)), key=lambda k: A[k])


