"""import math
n = int(input())
x = list(map(int, input().split()))
def is_prime(x):
    prime = set()
    primess= [True] * (x+1)
    primess[0] = primess[1] = False

    for i in range(2, int(math.sqrt(x)) +1):
        if primess[i]:
            for j in range(i*i, x+1, i):
                primess[j] = False
   ''' for i in range(len(primess)):
        if primess[i] == True:
            prime.add(i)'''
    return primess
primes = is_prime(1000001)
#print(primes)
for i in x:
    r = int(math.sqrt(i))
    if r*r == i and primes[r]:
        print("YES")
    else:
        print("NO")"""

print((1+ 5+2+2+ 2+3)/6)

"""import sys
import math

def sieve(limit):
    '''Returns a set of prime numbers up to 'limit'.'''
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime

    for i in range(2, int(math.sqrt(limit)) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False

    return {i for i in range(limit + 1) if is_prime[i]}

# Step 1: Precompute prime numbers up to 10^6
LIMIT = 10**6
primes = sieve(LIMIT)

# Step 2: Precompute T-primes (squares of primes)
t_primes = {p * p for p in primes}

# Step 3: Process input
n = int(sys.stdin.readline().strip())
arr = map(int, sys.stdin.readline().split())

for x in arr:
    print("YES" if x in t_primes else "NO")"""