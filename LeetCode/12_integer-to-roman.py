"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: 3
Output: "III"

Example 2:

Input: 4
Output: "IV"

Example 3:

Input: 9
Output: "IX"

Example 4:

Input: 58
Output: "LVIII"
Explanation: C = 100, L = 50, XXX = 30 and III = 3.

Example 5:

Input: 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""

# This problem really sucks.
# You can do many if-else inside a while, or more concise loopoing throgh a tuple

class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        d = (('M', 1000), ('CM', 900), ('D', 500), ('CD', 400), ('C', 100), ('XC', 90), ('L', 50), ('XL', 40), ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1))
        result = ""
        for roman, value in d:
            while num >= value:
                num -= value
                result += roman

        return result


S = Solution()
S.intToRoman(4) # IV
S.intToRoman(9) # IX
S.intToRoman(14) # XIV
S.intToRoman(19) # XIX
S.intToRoman(23) # XXIII
S.intToRoman(40) # XL
S.intToRoman(44) # XLIV
S.intToRoman(64) # LXIV
S.intToRoman(90) # XC
S.intToRoman(99) # XCIX
S.intToRoman(1901) # MCMI
S.intToRoman(1994) # MCMXCIV
