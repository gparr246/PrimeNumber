import math

def isPrime(n):
    if n == 1:
        return False
    
    if n//2 == n/2 and n!=2:
        return False

    if n == 2 or n == 3:
        return True
    
    if not(isMillerRabinPrime(n)):
        return False
    
    return True

def isMillerRabinPrime(n):
    N = n-1
    i = 0
    k = 0
    m = 0
    while True:
        testK = N/2**i
        if not(testK.is_integer()):
            k = i - 1
            m = N/2**k
            break
        i += 1

    b = (2**m)%n

    if((b+1)%n == 0 or(b-1)%n == 0):
        return True
    depth = 0 
    while True:
        if ((b**2)-1)%n == 0:
            return False
        elif ((b**2)+1)%n == 0:
            return True
        b = (b**2%n)
        depth += 1
        if depth > 10:
            return False

def testCorrectPrimes(primes,limit):
    correct = []
    for num in range(1, limit+1):
       if num > 1:
           for i in range(2, num):
               if (num % i) == 0:
                   break
           else:
               correct.append(num)
    
    print("Test Pass: " + str(correct == primes))
        
primes = []
limit = 100
for i in range(1,limit+1):

    if isPrime(i):
        primes.append(i)
        if i < 10:
            print("0" + str(i),end=' ')
        else:
            print(i,end=' ')
    else:
        print("__",end=' ')
    if i//10 == i/10:
        print('')
#testCorrectPrimes(primes,limit)





