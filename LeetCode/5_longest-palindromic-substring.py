"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:

Input: "cbbd"
Output: "bb"

"""


# Dynamic programming approach:
# Find a small palindrome that have size either 1 or 2
# We can extend it if characters at both sides are the same. Extend it as far as long as possible
# Keep track of the maximum length and the palindrome itself.


class Solution:

    def longestPalindrome(self, s):

        if len(s) == 0: return ""

        # Keep track of solution
        pal = s[0] # 1 letter is the smallest palindrome one can find

        # 1-sized palindrome.
        for i in range(0,len(s)):
            # Extend element i as much as possible
            # Extend the palindrome k positions
            k = 1
            while i-k >= 0 and i+k < len(s):
                if s[i-k] == s[i+k]: # Possible extension found
                    if 2 * k + 1 > len(pal):
                        pal = s[i - k:i + k + 1]
                    # try to extend palindrome length
                    k += 1
                else:
                    break

        print('After 1-palindrome found: ' + str(pal) + ' i = ' + str(i) + ' k = ' + str(k))

        # 2-sized palindrome. i now represents the beginning of the 2-pal
        for i in range(0, len(s)-1):

            # Need to find two same letters first
            if s[i] == s[i+1]:
                if len(pal) < 2: # The solution might be simply the 2-pal
                    pal = s[i:i+2]

                # Now try to extend it
                k = 1
                while i - k >= 0 and i + k + 1 < len(s):
                    if s[i - k] == s[i + k + 1]:
                        # Replace solution
                        if 2 * k + 2 > len(pal):
                            pal = s[i - k:i + k + 2]

                        k += 1
                    else:
                        break

        # END
        return pal


# Missing the case when the 1 or 2 palindromes are the answer

S = Solution()
s = "ababababa"
S.longestPalindrome(s) # ababababa
#
s = 'babad'
S.longestPalindrome(s) # bab

s = "cbbd"
S.longestPalindrome(s) # bb

s = "bbbb"
S.longestPalindrome(s) # bb

s = "aba"
S.longestPalindrome(s) # aba

s = "abcda"
S.longestPalindrome(s) # a




# Idea 1: Kind of brute force
# Create a function that checks if a string is a palindrome.
# Create another function that checks whether there exists a palindrome of size n
# We cannot do binary search unfortunately.

class Solution:
    def isPal(self, s):
        """
        Return 1 if s is a palindrome and 0 otherwise
        """
        # Pointers from both sides
        low = 0
        up = len(s)-1
        while low < up:
            if s[low] == s[up]:
                low += 1
                up -= 1
            else:
                return 0
        return 1

    def check(self, s, k):
        """
        Returns "" if there is no palindrome of size k, and the first palindrome of size k if there is one
        """

        for i in range(k,len(s)+1): # careful with the index
            select = s[(i-k):i]
            if self.isPal(select) == 1:
                return select
        return ""



    def longestPalindrome(self, s):
        """
        Return the longets palindrome. Binary search
        """
        # Special cases
        if len(s)==0:
            return ''
        elif len(s) == 1:
            return s

        # Max length of palindrome: 10000
        max_pal = min(len(s)+1,1000)
        min_pal = 0
        k = max_pal
        sol = ''
        print('START k = ' + str(k) + ' min = ' + str(min_pal) + ' max = ' + str(max_pal))

        while k > min_pal:

            # Check if palindrome exists
            sol_aux = self.check(s,k)
            print('\t sol_aux = ' + str(sol_aux))
            # If the length is strictly lower than what we found before, stop
            if len(sol_aux) < len(sol):
                return sol
            # Otherwise update
            sol = sol_aux
            k -= 1

            print('k = ' + str(k) + ' min = ' + str(min_pal) + ' max = ' + str(max_pal) + ' sol_aux = ' + str(sol_aux))

        # END
        return sol

S = Solution()
s = "bb"
S.isPal(s)
S.check(s,2) # bb
S.longestPalindrome(s) # bb

S = Solution()
s = "aba"
S.check(s,2)
S.longestPalindrome(s) # aba