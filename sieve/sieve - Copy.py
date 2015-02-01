def sieve_2(limit):
    numbers = range(limit)
    numbers[0] = 0
    numbers[1] = 0

    for i in range(0, int(limit**0.5 + 1)):
        if numbers[i] > 0:
            for j in range(i * i, limit + 1, i):
                numbers[j] = 0
            #if n in numbers:
                #numbers.remove(n)
    return [w for w in numbers if w > 0]

def sieve2(prime_range):
    """Runs the Sieve of Sieve of Eratosthenes to find all the primes from 2 up to a given number"""
    retlist = xrange(2, prime_range)
    for i in retlist:
        retlist = filter(lambda x: x==i or x%i!=0, retlist)
    return retlist


import math

def sieve(limit):
    numbers = range(3, limit, 2)
    i = 0
    while i < len(numbers):
        p = numbers[i]
        n = 2 * p
        while n < int(sqrt(limit) + 1):
            try:
                numbers.remove(n)
            except:
                pass
            #if n in numbers:
                #numbers.remove(n)
            n += p
        i += 1
    return [2] + numbers

def sieve4(N):
    is_prime = [True] * (N+1)
    is_prime[0:2] = [False, False]
    for i in range(0, int(N**0.5+1)):
        if is_prime[i]:
            for j in range(i*i, N+1, i):
                is_prime[j] = False
    return [i for i in range(0, N+1) if is_prime[i]]


from math import sqrt

def sieve8(prime_range):
    """Runs the Sieve of Sieve of Eratosthenes to find all the primes from 2 up to a given number"""
    if (prime_range%2 == 0):
        prime_range -= 1
    retlist = range(3,prime_range+1,2)
    maxval = sqrt(prime_range)
    for i in retlist:
        if i > maxval:
            break
        retlist = [x for x in retlist if x == i or x % i != 0]
    return [2]+retlist

def time(f, lim):
    import time
    t = time.time()
    f(lim)
    print time.time() - t
    

#[time(i, 100000) for i in (sieve, sieve4, sieve3)]
#sieve3(10000)
time(sieve, 10000)


#t = time.time()
#sieve2(lim)
#print time.time() - t
#t = time.time()
#sieve4(lim)
#print time.time() - t

#t = time.time()
#sieve2(lim)
#print time.time() - t
