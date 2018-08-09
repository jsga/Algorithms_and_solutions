'''
A string S consisting of N characters is considered to be properly nested if any of the following conditions is true:

S is empty;
S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
S has the form "VW" where V and W are properly nested strings.
For example, the string "{[()()]}" is properly nested but "([)()]" is not.

Write a function:

class Solution { public int solution(String S); }

that, given a string S consisting of N characters, returns 1 if S is properly nested and 0 otherwise.

For example, given S = "{[()()]}", the function should return 1 and given S = "([)()]", the function should return 0, as explained above.

Assume that:

N is an integer within the range [0..200,000];
string S consists only of the following characters: "(", "{", "[", "]", "}" and/or ")".
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(N) (not counting the storage required for input arguments).

'''


def solution(S):

	# empty case
	if len(S)==0:
		return 1

	# Last opened bracket
	lo = []

	for i in range(0,len(S)):

		# opening brackets
		if S[i] == '(':
			lo.append('(')
		elif S[i] == '{':
			lo.append('{')
		elif S[i] == '[':
			lo.append('[')

		if len(lo)==0:
			# no opening brackets left
			return 0

		# closing brackets
		if S[i] == ')':
			if lo[-1] == "(":
				lo.pop(-1) # remove last element
			else:
				return 0

		elif S[i] == '}':
			if lo[-1] == "{":
				lo.pop(-1) # remove last element
			else:
				return 0

		elif S[i] == ']':
			if lo[-1] == "[":
				lo.pop(-1) # remove last element
			else:
				return 0

	# if lo is not empty not all brackets were closed
	if len(lo) == 0:
		return 1
	else:
		return 0





S = '([)()]'
solution(S)

S = '{[()()]}'
solution(S) # 1

S = '{[()(]}'
solution(S) # 0

S = ''
solution(S) # 1

S = '()[]{}'
solution(S) # 1

S = '())'
solution(S) # 1

