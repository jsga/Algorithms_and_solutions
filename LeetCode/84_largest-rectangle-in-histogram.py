'''
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

The largest rectangle is shown in the shaded area, which has area = 10 unit.


Example:

Input: [2,1,5,6,2,3]
Output: 10
'''


# First approach using a stack. This takes too long. Some elements can be removed.
class Solution:

    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        N = len(heights)
        if N == 0: return 0

        # Initialize stack stackid and area
        st, stid, area, maxarea = [], [], [], 0

        for i,x in enumerate(heights):

            if len(st) == 0: # nothing on the stack so we add whatever comes
                print('Add 1st element')
                st.append(x)
                stid.append(i)
                area.append(x)
                maxarea = x

            elif x <= st[-1]: # element is lower so keep on adding. Update area of stack
                print('Trim element, update block, and add block')

                # First close/remove blocks higher than x (possibly not needed a full for loop)
                print('st before trimming = ' + str(st))
                j = 0
                Nst = len(st)
                area_new = 0 # add as many elements as we remove. Since we can remove more than 1 block, add the biggest block we remove
                while j < Nst:
                    if st[j] > x:
                        # Before we close it update corresponding blocks
                        area_new = max( area_new, x * (area[j] //st[j]))
                        # Now we can close it
                        st.pop(j)
                        stid.pop(j)
                        area.pop(j)
                        Nst -= 1
                    else:
                        j += 1
                print('st after trimming = ' + str(st) + ' area_new = ' + str(area_new))


                # Add now new element
                st.append(x)
                stid.append(i)
                if len(area)>0: # Beware, the stack might be empty
                    # add x to all the opened blocks
                    area = [a + st_aux for a,st_aux in zip(area,st)]
                area.append(x + area_new) # append latest area block

                # Re-calculate max
                maxarea = max(maxarea, max(area))


            else: # x > st # here we update the stack before adding new area
                print('Add block bigger')
                # Add now new block
                st.append(x)
                stid.append(i)

                # add x to all the opened blocks
                if len(area)>0: # Beware, the stack might be empty
                    # add x to all the opened blocks
                    area = [a + st_aux for a, st_aux in zip(area,st)]
                area.append(x) # append latest area block

                # Re-calculate max
                maxarea = max(maxarea, max(area))

            # PRINT
            print('i = '+ str(i) + ' x = ' + str(x))
            print('st = ' + str(st) + ' stID = ' + str(stid))
            print('area = ' + str(area) + ' maxarea = ' + str(maxarea))
            print('-------')

        # END
        return maxarea




class Solution:

    def largestRectangleArea(self,heights):
        max_area = 0
        stack = []

        for index, height in enumerate(heights):
            # If a lower element is seen, then we need to trim the stack. Start by the end always
            if stack and height < stack[-1][1]:

                while stack and height < stack[-1][1]:
                    prev_index, prev_height = stack.pop() # Removed element
                    max_area = max((index - prev_index) * prev_height, max_area) # Update max area. Might be the block we just removed.
                # After the popping, add the last dropped element to the stack "trimmed" to height. This will be the highest block so far
                stack.append((prev_index, height))

            stack.append((index, height)) # in any case, add the newcoming block (highest so far)

        # Finish calculating the blocks left in the stack
        while stack:
            prev_index, prev_height = stack.pop()
            max_area = max((len(heights) - prev_index) * prev_height, max_area)
        #END
        return max_area


S = Solution()
heights = [i for i in range(1,19999)]
S.largestRectangleArea(heights)


heights = [2,1,5,6,2,3]
S.largestRectangleArea(heights) # 10

heights = [2,1,6,5,2,3]
S.largestRectangleArea(heights) # 10

heights = [3,6,5,7,4,8,1,0] # 20
S.largestRectangleArea(heights)

heights = [2,1,2]
S.largestRectangleArea(heights) # 3


heights = [5,1,1]
S.largestRectangleArea(heights) # 5

heights = [5,1,1,5,5]
S.largestRectangleArea(heights) # 10

heights = [5]
S.largestRectangleArea(heights) # 5

heights = [2,5,5]
S.largestRectangleArea(heights) # 10

heights = [2,5]
S.largestRectangleArea(heights) # 5

heights = [4,1,2,5]
S.largestRectangleArea(heights) # 5

heights = [5,2]
S.largestRectangleArea(heights) # 5

heights = [5,5]
S.largestRectangleArea(heights) # 10

S.largestRectangleArea([]) # 5




## The function below calculated the nextGreater element. I finally did not used it even though a similar approach was used.

def nextGreater(nums):
    """
    Allows for repeated elements in nums.
    Returns a list with values and indices. -1 means do not exist.
    """
    N = len(nums)
    cache, cacheidx, st, stidx = [-1] * N, [-1] * N, [], []

    for i, x in enumerate(nums):

        if len(st) == 0:  # starting point: nothing to compare with
            st.append(x)
            stidx.append(i)

        elif x <= st[-1]:  # if lower then they might share the same nextMax
            st.append(x)
            stidx.append(i)
        else:
            while st and st[-1] < x:  # Here we have a new nextMax!
                # Add elements to the cache
                cache[stidx[-1]] = x
                cacheidx[stidx[-1]] = i
                # Remove elements we have saved
                stidx.pop()
                st.pop()

            st.append(x)  # When done attach the "max" to the stack, for later check
            stidx.append(i)  # also the index of the max

        print('---')
        print('x = ' + str(x) + ' i = ' + str(i))
        print('st = ' + str(st))
        print('cache = ' + str(cache) + ' cacheidx = ' + str(cacheidx))

    return cache, cacheidx  # the next greater & the corresponding index

nums = [4,3,2,1,5]
nextGreater(nums)