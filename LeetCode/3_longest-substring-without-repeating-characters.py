"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


def lengthOfLongestSubstring( s):
    """
    :type s: str
    :rtype: int
    """

    if len(s) == 0:
        return 0
    elif len(s) == 1:
        return 1

    # Keep count and substring to far
    count = 0
    a = s[0]

    for i in range(1, len(s)):

        print('i = ' + str(i) + ' count = ' + str(count) + ' a = ' + str(a) + ' s[i] = ' + str(s[i]))

        # Update the substring.
        # find if s[i] is in a
        if s[i] in a:
            # crop a removing previous strings than s
            aux = ""
            for el in reversed(a):
                if el == s[i]:
                    break
                else:
                    aux += el
            print('  --- i = ' + str(i) + 'cropping a = ' + str(a) + ' at s(i) = ' + str(s[i]) +' -> aux = ' + str(aux))
            a = aux[::-1]

        # Append to previous
        a += s[i]

        # count is the max length
        count = max(count, len(a))

    # END
    print(' ** END ** count = ' + str(count))
    return count



s = 'pwwkew'
lengthOfLongestSubstring(s)

s = 'pwwkewaww'
lengthOfLongestSubstring(s)

s = ''
lengthOfLongestSubstring(s)

s = 'aa'
s = 'bpfbhmipx'
lengthOfLongestSubstring(s)
lengthOfLongestSubstring2(s)


def lengthOfLongestSubstring2(s):
    start = maxLength = 0
    usedChar = {}

    for i in range(len(s)):
        if s[i] in usedChar and start <= usedChar[s[i]]:
            start = usedChar[s[i]] + 1
        else:
            maxLength = max(maxLength, i - start + 1)

        usedChar[s[i]] = i

    return maxLength