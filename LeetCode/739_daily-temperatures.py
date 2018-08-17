"""
Given a list of daily temperatures, produce a list that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list temperatures = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].
"""


# This is the same as calculating the next bigger number and taking the difference in indeces
# Or, reversed:
#


class Solution:
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """

        # Keep solution here
        N = len(temperatures)
        sol = [0]*N

        # Stack of number of maximums
        st = []
        st_idx = []

        # Loop backwards the list
        for i in range(len(temperatures)-1,0-1,-1):

            t = temperatures[i]
            print(' t = ' + str(t) + ' i = ' + str(i))

            # If stack is empty add element
            if len(st)==0:
                print(' ** First element added')


            # If new element is lower than last element in stack: add it as well
            elif t < st[-1]:
                print(' ** New lower element')
                # Update its solution
                sol[i] = 1

            # If element is greater= than last element in stack: trim stack
            elif t >= st[-1]:
                print(' ** Trim stack')
                while t >= st[-1]:
                    st.pop(-1)
                    st_idx.pop(-1)
                    if len(st) == 0: # if we have reached the end of the stack
                        break

                # Update soution based on the last element in the stack
                if len(st) > 0:
                    sol[i] = st_idx[-1] - i

            # Now add new element
            st.append(t)
            st_idx.append(i)

            print(st)
            print(st_idx)
            print(sol)

        print(' END ')
        # END
        return sol



S = Solution()
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
S.dailyTemperatures(temperatures) # [1, 1, 4, 2, 1, 1, 0, 0]

temperatures = [1,2,1,3]
S.dailyTemperatures(temperatures) # [1,2,1,0]

temperatures = [1,1,1,3]
S.dailyTemperatures(temperatures) # [3,2,1,0]

temperatures = [1,1,1,3,3,3]
S.dailyTemperatures(temperatures) # [3,2,1,0,0,0]

temperatures = [1,1,1,3,3,3,4]
S.dailyTemperatures(temperatures) # [3,2,1,3,2,1,0]

temperatures = [1,4,1,1,4]
S.dailyTemperatures(temperatures) # [1,0,2,1,0]