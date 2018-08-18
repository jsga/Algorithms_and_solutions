"""
Two positive integers N and M are given. Integer N represents the number of chocolates arranged in a circle, numbered from 0 to N − 1.

You start to eat the chocolates. After eating a chocolate you leave only a wrapper.

You begin with eating chocolate number 0. Then you omit the next M − 1 chocolates or wrappers on the circle, and eat the following one.

More precisely, if you ate chocolate number X, then you will next eat the chocolate with number (X + M) modulo N (remainder of division).

You stop eating when you encounter an empty wrapper.

For example, given integers N = 10 and M = 4. You will eat the following chocolates: 0, 4, 8, 2, 6.

The goal is to count the number of chocolates that you will eat, following the above rules.

Write a function:

def solution(N, M)

that, given two positive integers N and M, returns the number of chocolates that you will eat.

For example, given integers N = 10 and M = 4. the function should return 5, as explained above.

Assume that:

N and M are integers within the range [1..1,000,000,000].
Complexity:

expected worst-case time complexity is O(log(N+M));
expected worst-case space complexity is O(log(N+M)).
"""


# https://app.codility.com/demo/results/trainingPU9WRV-757/
# Not good performance
def solution(N,M):

	wrap = [0] * N
	count = 0
	i = 0
	while wrap[i] == 0:
		# We eat this candy
		wrap[i] = 1
		count += 1
		# move to the next one
		i = (i+M) % N
		print('Eat: ' + str(i) + ' wraps: ' + str(wrap))

	return count


def solution(N,M):

	# We start eating the first candy
	start_eating = 0
	count = 0

	while True:
		# we eat the follwing candies.
		# Remember we ate one already
		count += 1 + ( (N - start_eating - 1) // M)
		# Some are left at the end
		left_candies = (N - start_eating - 1) % M
		# In the next iteration we start eating at a different place
		start_eating = M - left_candies - 1

		print('count = ' + str(count) + '  left_candies: ' + str(left_candies) + '  start_eating: ' + str(start_eating))

		if start_eating == 0:
			break

	return count


def gcd(a, b):
    # Get the greatest common divisor
    if (a % b == 0):
        return b
    else:
        return gcd(b, a % b)

def solution2(N, M):
    lcm = N * M / gcd(N, M) # Least common multiple
    return lcm / M

gcd(10,4)


M = 4
N = 10
solution(N,M) # 5

M = 3
N = 10
solution(N,M) # 10

M = 1
N = 1
solution(N,M) # 1

M = 10
N = 10
solution(N,M) # 1