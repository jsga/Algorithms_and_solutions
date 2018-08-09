"""
A prime is a positive integer X that has exactly two distinct divisors: 1 and X. The first few prime integers are 2, 3, 5, 7, 11 and 13.

A semiprime is a natural number that is the product of two (not necessarily distinct) prime numbers. The first few semiprimes are 4, 6, 9, 10, 14, 15, 21, 22, 25, 26.

You are given two non-empty arrays P and Q, each consisting of M integers. These arrays represent queries about the number of semiprimes within specified ranges.

Query K requires you to find the number of semiprimes within the range (P[K], Q[K]), where 1 ≤ P[K] ≤ Q[K] ≤ N.

For example, consider an integer N = 26 and arrays P, Q such that:

    P[0] = 1    Q[0] = 26
    P[1] = 4    Q[1] = 10
    P[2] = 16   Q[2] = 20
The number of semiprimes within each of these ranges is as follows:

(1, 26) is 10,
(4, 10) is 4,
(16, 20) is 0.
Write a function:

def solution(N, P, Q)

that, given an integer N and two non-empty arrays P and Q consisting of M integers, returns an array consisting of M elements specifying the consecutive answers to all the queries.

For example, given an integer N = 26 and arrays P, Q such that:

    P[0] = 1    Q[0] = 26
    P[1] = 4    Q[1] = 10
    P[2] = 16   Q[2] = 20
the function should return the values [10, 4, 0], as explained above.

Assume that:

N is an integer within the range [1..50,000];
M is an integer within the range [1..30,000];
each element of arrays P, Q is an integer within the range [1..N];
P[i] ≤ Q[i].
Complexity:

expected worst-case time complexity is O(N*log(log(N))+M);
expected worst-case space complexity is O(N+M) (not counting the storage required for input arguments).

"""

# N is the maximum number we can expect
# Start by calculating the primes all the way to N
# then the semi primes
# Then for each pair M, sum

def solution(N, P, Q):

    # 4 is the smalled semiprime. Return zeros in that case
    if N < 4:
        return [0]*len(P)


    # Primes: sieve algorithm
    primes = [1]* N
    primes[0] = primes[1] = 0 # 0 means they are not prime
    i=2
    while i*i < N:
        if primes[i] == 1:
            # When we find a prime, cross out the remaining multipliers. some might be "set" more than once to zero (fx 6 = 2*3)
            k = i*i
            while k < N:
                primes[k] = 0
                k += i
        i += 1
    print(primes)

    # Semi-primes so far
    semi = [0]*(N+1)
    semi[4] = 1 # 2*2
    i=3
    while i <= N/2:
        if primes[i] == 1:
            # Multiply by all the previous primes
            j=2
            while j <= i and i*j <= N:
                if primes[j] == 1:
                    print('i='+str(i) + ' j=' + str(j) + ' prime:' + str(i) + ' semiprime: ' + str(i*j))
                    semi[i*j] = 1
                j += 1
        i += 1
    print(semi)

    # Sum elements in between two indexes
    result = [0] * len(P)
    for i in range(0, len(P)):
        result[i] = sum(semi[(P[i]): Q[i]+1])

    print(result)
    return result





def solution(N, P, Q):

    # 4 is the smalled semiprime. Return zeros in that case
    if N < 4:
        return [0]*len(P)

    # Primes: sieve algorithm
    primes = [1]* N
    primes[0] = primes[1] = 0 # 0 means they are not prime
    i=2
    while i*i < N:
        if primes[i] == 1:
            # When we find a prime, cross out the remaining multipliers. some might be "set" more than once to zero (fx 6 = 2*3)
            k = i*i
            while k < N:
                primes[k] = 0
                k += i
        i += 1
    print(primes)

    # Semi-primes
    semi = [0]*(N+1)
    semi[4] = 1 # 2*2
    i=3
    while i <= N/2:
        if primes[i] == 1:
            # Multiply by all the previous primes
            j=2
            while j <= i and i*j <= N:
                if primes[j] == 1:
                    print('i='+str(i) + ' j=' + str(j) + ' prime:' + str(i) + ' semiprime: ' + str(i*j))
                    semi[i*j] = 1
                j += 1
        i += 1
    print(semi)

    # Sum elements in between two indexes
    semi_cumsum = [0] * (N+1)
    # Do a cum-sum first (a single pass)
    for i in range(1, N+1):
        if semi[i] == 1:
            semi_cumsum[i] =  semi_cumsum[i-1] + 1
        else:
            semi_cumsum[i] = semi_cumsum[i-1]
    print(semi_cumsum)

    # Not take the difference between both cumsum
    result = [0] * len(P)
    for i in range(0, len(P)):
        result[i] =  semi_cumsum[Q[i]] - semi_cumsum[ P[i]-1]
    print(result)

    # END
    return result



N = 26
P = [1,4,16]
Q = [26,10,20]

solution(N,P,Q) # 10 4 0

N = 4
P = [1,1]
Q = [3,3]
solution(N,P,Q)