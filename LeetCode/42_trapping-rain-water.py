"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""


# Obvious solution: keep a stack

class Solution:

    def trap(self, height):

        # Keep stack indexes and water amount
        st = []
        water = 0


        for i,h in enumerate(height):


            # if the stack is not empty
            if len(st) > 0:

                if h > height[st[-1]]: # This means we fill up with water some blocks and remove them

                    print('Trim stack, new element h: ' + str(h) + ' idx st = ' + str(st))

                    while st and h > height[st[-1]]:
                        # the new element is bounded on the left by last
                        last = st.pop()

                        if len(st) == 0: # if nothing else remaining then stop
                            break

                        # Find the latest element closing the swimming pool. Think of it as a horizontal filling of water
                        distance = i - st[-1] - 1

                        # Pour water up to the level of the last element in the stack. Here we calculate the vertical distance of the block
                        pour = min(h ,  height[st[-1]]) - height[last]

                        # Add to the counter both distance and vertical pour
                        water += distance * pour

                        print('\tlast = ' + str(last) + ' pour = ' + str(pour) + ' distance = '+ str(distance))

                    print('Trimmed: ' + str(st) + ' Water = ' + str(water))

            # Always append the latest element
            st.append(i)

        print('**END** st = ' + str(st))
        # END
        return water


S = Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
S.trap(height) # 6


height = [1,2,3,4,3,2,1]
S.trap(height) # 0

height = [1,4,0,4]
S.trap(height) # 4

height = [4,2,0,3,2,5]
S.trap(height) # 9


# First idea I tried, quick to code and re-using code from temperature problem.
# Loop two times to calculate next big item on the left and on the right.
# If an element has a next big on the left and right, then it must contain sme water. Fill up up to min(nextL,nextR) - height
# Repeat this until no more wholes can be filled.
# This approach is time consuming: many unnecessary loops

class Solution:


    def nextB(self, height,is_prev):
        """
        Returns index of the next big element
        if is_prev == False then it returns the indexes of the previous big element
        """

        # Keep solution here
        N = len(height)
        sol = [-1]*N

        # Stack of number of maximums
        st = []
        st_idx = []

        # Loop backwards the list if is_next = True. Else, loop normally (namely, find the previous big)
        if is_prev == True:
            R = range(N-1,0-1,-1)
        else:
            R = range(0,N)

        for i in R:

            t = height[i]

            # If stack is empty add element
            if len(st) == 0:
                pass

            # If new element is lower than last element in stack: add it as well
            elif t < st[-1]:
                # Update its solution
                sol[i] = st_idx[-1]

            # If element is greater= than last element in stack: trim stack
            elif t >= st[-1]:
                while t >= st[-1]:
                    st.pop(-1)
                    st_idx.pop(-1)
                    if len(st) == 0: # if we have reached the end of the stack
                        break

                # Update soution based on the last element in the stack
                if len(st) > 0:
                    sol[i] = st_idx[-1]

            # Now add new element
            st.append(t)
            st_idx.append(i)

        # END
        return sol

    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        water = 0
        not_water = 0 # Count whenever we do not add water. Used to stop while loop.

        while not_water < len(height):

            # previous and next heights
            P = self.nextB(height, is_prev=True)
            N = self.nextB(height, is_prev=False)

            # Re-start stopping criteria
            not_water = 0

            for i in range(0,len(height)):

                p = P[i]
                n = N[i]
                if p == -1 or n == -1:
                    # Do not count this one
                    not_water += 1
                else:
                    # add water counter
                    pour = min(height[p], height[n])
                    water += pour - height[i]
                    # Update height
                    height[i] = pour
            print('water count ' + str(water) + ' not_water ' + str(not_water))
            print(height)
            print('---')
        return water


S = Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
# S.nextB(height,is_prev=True)
# S.nextB(height,is_prev=False)
S.trap(height) # 6
