"""
Halfling Woolly Proudhoof is an eminent sheep herder. He wants to build a pen (enclosure) for his new flock of sheep. The pen will be rectangular and built from exactly four pieces of fence (so, the pieces of fence forming the opposite sides of the pen must be of equal length). Woolly can choose these pieces out of N pieces of fence that are stored in his barn. To hold the entire flock, the area of the pen must be greater than or equal to a given threshold X.

Woolly is interested in the number of different ways in which he can build a pen. Pens are considered different if the sets of lengths of their sides are different. For example, a pen of size 1×4 is different from a pen of size 2×2 (although both have an area of 4), but pens of sizes 1×2 and 2×1 are considered the same.

Write a function:

def solution(A, X)

that, given an array A of N integers (containing the lengths of the available pieces of fence) and an integer X, returns the number of different ways of building a rectangular pen satisfying the above conditions. The function should return −1 if the result exceeds 1,000,000,000.

For example, given X = 5 and the following array A:

  A[0] = 1
  A[1] = 2
  A[2] = 5
  A[3] = 1
  A[4] = 1
  A[5] = 2
  A[6] = 3
  A[7] = 5
  A[8] = 1


the function should return 2. The figure above shows available pieces of fence (on the left) and possible to build pens (on the right). The pens are of sizes 1x5 and 2x5. Pens of sizes 1×1 and 1×2 can be built, but are too small in area. It is not possible to build pens of sizes 2×3 or 3×5, as there is only one piece of fence of length 3.

Assume that:

N is an integer within the range [0..100,000];
X is an integer within the range [1..1,000,000,000];
each element of array A is an integer within the range [1..1,000,000,000].
Complexity:

expected worst-case time complexity is O(N*log(N));
expected worst-case space complexity is O(N) (not counting the storage required for input arguments).
"""


def hash_table(A):
    """
    Create a dictionary counting elements in A where count >=2
    """

    # Dictionary as hash table
    counts = dict()
    for i in A:
        counts[i] = counts.get(i, 0) + 1

    # Remove counted elements with less than 1 frequency
    # Also round them to the lower multiple of 2
    counts2 = {k: (2* int(v / 2)) for k, v in counts.items() if v >=2}

    # END
    return counts2

def sqrt_ceil(X):
    """
    Return the square root rounded to the ceiling
    """
    # An element with each other: elements of d greater than int(sqrt(X))
    sq = (X ** 0.5)
    # Ceil of sq
    if sq != int(sq):
        sq = int(sq) + 1

    return sq

def solution(A,X):

    # Special case
    if len(A) <= 1:
        return 0

    # Create a hash table that keeps occurrences of A more than once:
    d = hash_table(A)

    # Two types of rectangles: Squared and non-squared.
    # Count the squared first.
    sq = sqrt_ceil(X)
    d1 = {k: v for k, v in d.items() if k >= sq and v >= 4}
    count = len(d1)

    # Non-squared.
    # Find the first section in d such that the perimeter is >= X. Use binary search.
    dl = list(d.keys())
    dl.sort()

    if dl[-1] >= X:
        # Otherwise there is nothign to count

        for i,a in enumerate(dl):

            if i == len(dl)-1:
                break # last element does not combine with any other

            # Binary search to find the first occurrence
            low = i+1 # Look only elements to the right
            high = len(dl)-1
            while low <= high:
                mid = (high + low)//2

                if a * dl[mid] >= X:
                    high = mid
                else:
                    low = mid+1

                if low == high:
                    mid = low
                    break

            # j is the index we want. count from j to N-1
            count += len(dl) - mid # do not count the seuqred pen (might not be possible anyways)

    # END
    if count > 1000000000:
        return -1
    else:
        return count


A = [1,2,5,1,1,2,3,5,1]
X = 5
solution(A,X) # 2

A = [1,1,2,2,3,3,4,4,5,5,5,5,6,6] # 5 is the only squerd here
A = [6,6,5,5,5,5,4,4,3,3,2,2,1,1]
X = 4
solution(A,X) # 14,15,16 23,24,25,26 34,35,36 45,46 56 55 -> 14

A = [1,1,1,1]
X = 1
solution(A,X) # 1

A = []
X = 1
solution(A,X) # 0

A = [2, 2, 2,2]
X = 1
solution(A,X) # 1

A = [2, 2, 2,2,3,3,3,3,4,4,4,4] # [2,3,4]
X = 1
solution(A,X) # 22,33,44, 23,24,34 = 6

A = [12, 12, 12,12,13,13,13,13,14,14,14,14]
X = 1
solution(A,X) # 22,33,44, 23,24,34 = 6

A = [1,1,1,1,1,1,1,1,1]
X = 2
solution(A,X) # 0

A = [2, 3, 2, 3, 2, 3, 2, 3,4,4] # 33
X = 9
solution(A,X) # 1

A = [4,4,4,4,3,3,3,2,2]
X = 3
solution(A,X) # 4