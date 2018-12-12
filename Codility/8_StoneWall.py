'''
You are going to build a stone wall. The wall should be straight and N meters long, and its thickness should be constant; however, it should have different heights in different places. The height of the wall is specified by an array H of N positive integers. H[I] is the height of the wall from I to I+1 meters to the right of its left end. In particular, H[0] is the height of the wall's left end and H[N−1] is the height of the wall's right end.

The wall should be built of cuboid stone blocks (that is, all sides of such blocks are rectangular). Your task is to compute the minimum number of blocks needed to build the wall.

Write a function:

def solution(H)

that, given an array H of N positive integers specifying the height of the wall, returns the minimum number of blocks needed to build it.

For example, given array H containing N = 9 integers:

  H[0] = 8    H[1] = 8    H[2] = 5
  H[3] = 7    H[4] = 9    H[5] = 8
  H[6] = 7    H[7] = 4    H[8] = 8
the function should return 7. The figure shows one possible arrangement of seven blocks.



Assume that:

N is an integer within the range [1..100,000];
each element of array H is an integer within the range [1..1,000,000,000].
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(N) (not counting the storage required for input arguments).
'''

# a block continues until a lower height is found. We close (count) all previous blocks.

# if a higher height is found, we need to add a new block.

def solution(H):

    st = []
    count = 0


    for h in H:
        if len(st) == 0: #Initialize stack
            st.append(h)
        else:
            # Compare h with the stack.
			# If higher, add. If lower, trim stack and add count. If same, no action.
            while len(st) > 0:
                if h > st[-1]:
                    st.append(h)
                    break
                elif h == st[-1]:
                    break
                else:
                    aux = st.pop()
                    count += 1
                    continue

        # If all block are closed, open new one
        if len(st) == 0:
            st.append(h)

    # Finally count opened blocks
    return count + len(st)



H = [8,8,5,7,9,8,7,4,8]
solution(H) # 7

H = [5,4,3,2,3,5]
solution(H)

H = [5]
solution(H)

H = [5,1,5,1,5]
solution(H) # 4

