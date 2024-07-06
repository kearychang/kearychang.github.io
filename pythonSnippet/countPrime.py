import math

class Solution:
    primeSet = [2]
    
    def countPrimes(self, n: int) -> int:
        def isPrime(n):
            if n in Solution.primeSet:
                return True
            maxCheck = math.ceil(math.sqrt(n))
            for e in Solution.primeSet:
                if e > maxCheck:
                    break
                elif n % e == 0:
                    return False
            if n not in Solution.primeSet:
                Solution.primeSet.append(n)
            return True
        if n <= 2:
            return 0
        counter = 3
        countPrime = 1
        while counter < n:
            if isPrime(counter):
                countPrime += 1
            counter += 2
        return countPrime

x = Solution()
print(x.countPrimes(100))
print(x.countPrimes(500))
print(x.countPrimes(1000))
print(x.countPrimes(10000))
print(x.countPrimes(50000))
print(x.countPrimes(100000))
print(x.countPrimes(500000))
print(x.countPrimes(3))