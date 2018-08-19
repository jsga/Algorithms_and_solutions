"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
"""


class Solution:
    def longestValidParentheses(self, s):
        """
        Approach based on stack
        Append if (
        If ) and the previous element was a (, pop both
            In that case add a +2 to the counter (last element in the stack) of the longest parenthesis
        If ) but and the stack is empty just keep it empty
        """

        stack = [0]
        longest = 0

        for c in s:
            if c == "(":
                stack.append(0)
            else:
                if len(stack) > 1:
                    val = stack.pop()
                    stack[-1] += val + 2
                    longest = max(longest, stack[-1])
                else:
                    stack = [0]

        return longest


S = Solution()
s = ')()())'
S.longestValidParentheses(s) # 4


s = ')(())()))'
S.longestValidParentheses(s) # 6

s = ')(())()(('
S.longestValidParentheses(s) # 6

s = '()(('
S.longestValidParentheses(s) # 2

s = '(((()'
S.longestValidParentheses(s) # 2

s = '()(()'
S.longestValidParentheses(s) # 2

s = '())))'
S.longestValidParentheses(s) # 2

s = '()(((('
S.longestValidParentheses(s) # 2

s = ')))(('
S.longestValidParentheses(s) # 0

s = '(()()'
S.longestValidParentheses(s) # 4

