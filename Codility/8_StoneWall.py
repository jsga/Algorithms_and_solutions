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

	# keep opened blocks with their heights
	open = []
	count = 0

	for i in range(0,len(H)):

		# Starting conditions
		if len(open) == 0:
			# No blocks opened. We need 1 at least
			open.append(H[i])
			print('Start block: ' + str(open))
			continue

		# Nothing to add or remove
		if H[i] == open[-1]:
			print(str(i) + ' same height no block added'+ ' open=' + str(open))

		# close exisintg blocks
		while H[i] < open[-1]:
			# Here we close the block and count it
			open.pop()
			count += 1
			print('Closed block iter ' + str(i) + ' H=' + str(H[i]) + ' open=' + str(open))
			if len(open) == 0:
				break
		# If all blocks are removed re-start loop
		if len(open) == 0:
			open.append(H[i])
			continue

		# Add new bloks
		if H[i] > open[-1]:
			# We need one more block with new height
			open.append(H[i])
			print('New block ' + str(i) + ' H=' + str(H[i])+ ' open=' + str(open))

	# END. add opened blocks
	return (count + len(open))





H = [8,8,5,7,9,8,7,4,8]
solution(H) # 7

H = [5,4,3,2,3,5]
solution(H)

H = [5]
solution(H)

H = [5,1,5,1,5]
solution(H)

