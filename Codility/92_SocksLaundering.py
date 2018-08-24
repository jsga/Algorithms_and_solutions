"""
Bob is about to go on a trip. But first he needs to take care of his supply of socks. Each sock has its own color. Bob wants to take as many pairs of clean socks as possible (both socks in the pair should be of the same color).

Socks are divided into two drawers: clean and dirty socks. Bob has time for only one laundry and his washing machine can clean at most K socks. He wants to pick socks for laundering in such a way that after washing he will have a maximal number of clean, same-colored pairs of socks. It is possible that some socks cannot be paired with any other sock, because Bob may have lost some socks over the years.

Bob has exactly N clean and M dirty socks, which are described in arrays C and D, respectively. The colors of the socks are represented as integers (equal numbers representing identical colors).

For example, given four clean socks and five dirty socks:

If Bob's washing machine can clean at most K = 2 socks, then he can take a maximum of three pairs of clean socks. He can wash one red sock and one green sock, numbered 1 and 2 respectively. Then he will have two pairs of red socks and one pair of green socks.

Write a function:

def solution(K, C, D)

that, given an integer K (the number of socks that the washing machine can clean), two arrays C and D (containing the color representations of N clean and M dirty socks respectively), returns the maximum number of pairs of socks that Bob can take on the trip.

For example, given K = 2, C = [1, 2, 1, 1] and D = [1, 4, 3, 2, 4], the function should return 3, as explained above.

Assume that:

K is an integer within the range [0..50];
each element of arrays C, D is an integer within the range [1..50];
C and D are not empty and each of them contains at most 50 elements.
In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.
"""



# Brute force: select all possible combinations in D, in groups of K, such that the number of clean socks is maximal.
# Performance is not accounted for we should go for the easiest way of solving this.
# We need K nested loops, or, use itertools which is allowed
# https://app.codility.com/demo/results/training22JHPE-F24/

import itertools

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
    counts2 = {k: int(v / 2) for k, v in counts.items() if v >=2}

    # END
    return counts2


def solution(K, C, D):

    # Possible ways of cleaning D socks into K groups
    # warning: we can clean less than K socks too!
    comb = []
    for i in range(1,K+1):
        comb += list(itertools.combinations(D, i))

    # For each of those possibilities, find the number of pairs.
    # Keep the maximum
    pairs = hash_table(C)  # if we do not clean any socks
    sol = sum(pairs.values())

    for i in range(0,len(comb)):

        socks = C + list(comb[i]) # list of socks
        pairs = hash_table(socks) # count them
        sol = max(sol, sum( pairs.values()) )

    return sol



K = 2
C = [1,2,1,1]
D = [1,4,3,2,4]
solution(K,C,D) # 3

K = 1
C = [1,2,1,1]
D = [1,4,3,2,4]
solution(K,C,D) # 2

K = 4
C = [1,2,1,1]
D = [1]
solution(K,C,D) # 2

K = 0
C = [1,1,2,2]
D = [1,2,3]
solution(K,C,D) # 2