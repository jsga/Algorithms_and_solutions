'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

'''

# Recursive solution for fun. Works fine but needs N recursive calls (not very efficient). There must be another way.

class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n==2:
            return 2

        A = [1]*n
        return self._climStairs(A) + 1 # we always start by filling with ones

    def _climStairs(self, A, i2=0):

        print('A = ' + str(A))
        if len(A) == 0:
            return 0
        elif len(A) == 1:
            return 1
        elif len(A)==2:
            if A[0]==2 or A[1] == 2:
                return 0 # no other way of climbing the remaining
            else:
                return 2 # climb both at the same time
        else:

            s = 0 # count number of sums.
            # i2 indicate where the last 2 is. If 0 no 2s

            for i in range(i2,len(A)-1):

                #print('i='+str(i)+ ' A = '+ str(A) + ' s =' + str(s))

                # Check if we can sum 1+1
                if A[i] + A[i+1] == 2:
                    A_aux = A[:]
                    A_aux[i+1] = 2
                    A_aux.pop(i)
                    s += 1 + self._climStairs(A_aux, i2=i+1) # sum the step we found plus any other step we might find

            return s


S = Solution()
S.climbStairs(3) # 3
S.climbStairs(2) # 2
S.climbStairs(4) # 5
S.climbStairs(5) # 8
S.climbStairs(6) # 13
S.climbStairs(7) # 20 !!! Sum the two previous solutions.
S.climbStairs(1)
S.climbStairs(2)
S.climbStairs(17)




# Dynamic solution. Works fine but needs N recursive calls (not very efficient)
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0
        elif n == 1:
            return 1

        sol = [0]*(n+1)
        sol[1] = 1 # Start with the first two cases for n=0,1
        sol[2] = 2
        for i in range(3,n+1):
            sol[i] = sol[i-1] + sol[i-2]

        return sol[n]


S = Solution()
S.climbStairs(3) # 3
S.climbStairs(2) # 2
S.climbStairs(4) # 5
S.climbStairs(5) # 8
S.climbStairs(6) # 13
S.climbStairs(7) # 21 !!! Sum the two previous solutions. Fibonacci?
S.climbStairs(1)
S.climbStairs(2)
S.climbStairs(17)