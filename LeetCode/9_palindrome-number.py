"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Follow up:

Coud you solve it without converting the integer to a string?
"""


class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        # initial checks
        if x < 0:
            return False

        # convert to string
        s = str(x)
        # loop reverse
        rs = ""
        for i in reversed(s):
            rs += i
        # Back to numeric
        xr = int(rs)

        print(rs)
        print(xr)

        # Check if x and reversed are the same
        if x == xr:
            return True
        else:
            return False

S = Solution()
S.isPalindrome(10)

S.isPalindrome(101)
S.isPalindrome(121)


# Now do not convert to string
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        # initial checks
        if x < 0:
            return False

        # convert to list
        s = [i for i in x]

        # Check if same as reversed


x = 100
for i in range(0,len(x)):
    print(x[i])