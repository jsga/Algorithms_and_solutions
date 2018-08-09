"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def list2num(self,l):

        ret = ""
        for i in reversed(l):
            ret += str(i)
        return int(ret)

    def num2list(self, n):

        n_s = str(n)
        ret = ''
        for i in reversed(n_s):
            ret += str(i)
        return int(ret)

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        n1 = self.list2num(l1)
        n2 = self.list2num(l2)

        sol = self.num2list(n1+n2)
        return sol


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        if l1 == None:
            return l2
        if l2 == None:
            return l1

        # Initialize solution
        ans = []  # listNode()
        s = 0
        resto_prev = 0

        while True:

            # do the sum and find if resto applies
            if (l1 and not l2) or (l2 and not l1):
                # print(l1)
                # print(l2)

                if not l1:  # execute if l1 IS none
                    s = l2.val
                    l2 = l2.next
                    # print('l1 not None')
                elif not l2:
                    s = l1.val
                    l1 = l1.next
                    # print('l2 not none')
            elif l1 and l2:
                # print('Both not None')
                # print(l1.val)
                # print(l2.val)
                s = l1.val + l2.val
                l1 = l1.next
                l2 = l2.next
            else:
                #  Both are none so we are almost done
                # if resto is 1 add one to the solution
                if resto_prev == 1:
                    ans.append(1)
                break

            # Keep resto
            if s + resto_prev >= 10:
                resto = 1
                s -= 10
            else:
                resto = 0

            # Update answer
            ans.append(s + resto_prev)
            resto_prev = resto
            # print('sum = ' + str(s))
            # print('----')

        return ans

l1 = [2,4,3]
l2 = [5,6,4]
S = Solution()
S.addTwoNumbers(l1,l2) # 708


l = [2,4,3]
S.list2num(l1)


if  2 and  2:
    print('sss')
else:
    print('else')