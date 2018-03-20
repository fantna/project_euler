#!/usr/bin/python3

class Prime:
    
    def __init__(self):
        pass

    @staticmethod
    def isNotPrime(number, primes):
        for prime in primes:
            if number % prime == 0:
                return True
        primes.append(number)
        return False

if __name__ == '__main__':
    count = 2
    number = 3
    limit = 10001
    primes = [2, 3]
    while count < limit:
        number += 2
        if not Prime.isNotPrime(number, primes):
            count += 1
    print("{}nd prime number is: {}".format(limit, number))

    
