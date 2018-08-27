"""
Write a function:

def solution(S)

that, given a string S, returns the index (counting from 0) of a character such that the part of the string to the left of that character is a reversal of the part of the string to its right. The function should return −1 if no such index exists.

Note: reversing an empty string (i.e. a string whose length is zero) gives an empty string.

For example, given a string:

"racecar"

the function should return 3, because the substring to the left of the character "e" at index 3 is "rac", and the one to the right is "car".

Given a string:

"x"

the function should return 0, because both substrings are empty.

Assume that:

the length of S is within the range [0..2,000,000].
Complexity:

expected worst-case time complexity is O(length(S));
expected worst-case space complexity is O(1) (not counting the storage required for input arguments).
"""

# https://app.codility.com/demo/results/trainingSMSSC9-C3V/
def solution(S):

    # Only possible when S has an odd number of elements.
    if len(S) % 2 == 0:
        return -1

    else:
        # middle point
        mid = len(S) // 2

        # Iterate towards the edges and check if characters are the same
        # Stop if different characters found
        i = mid - 1
        j = mid+1
        while i >= 0 and j < len(S):

            if S[i] != S[j]:
                return -1
            else:
                i -= 1
                j += 1
        # END
        return mid

S = 'racecar'
solution(S) # 3

S = 'aabaa'
solution(S) # 2

S = []
solution(S)

S = 'c'
solution(S)

S = 'cc'
solution(S)