#!/usr/bin/python3

class Factor:
    def __init__(self, number):
        self._factors = []
        self._number = number

    ## recursive method seems beyond python default recursive depth 1000
#    def _calculate(self, factor, number):
#        if factor >= number:
#            return

#        if (number % factor == 0):
#            self._factors.append(factor)
#            number = number / factor
#        else:
#            factor += 1
#        self._calculate(factor, number)

    def _calculate(self):
        factor = 2
        number = self._number
        while factor < number:
            if (number % factor == 0):
                number = number / factor
                self._factors.append(factor)
            else:
                factor += 1
        self._factors.append(int(number))

    def factors(self):
        # this is used recursive method
        #self._calculate(2, self._number)

        self._calculate()
        results = set(self._factors)
        return results

class Prime:
    def __init__(self):
        pass

    @staticmethod
    def isPrime(number):
        f = Factor(number)
        if len(f.factors()) == 1:
            return True
        return False


if __name__ == "__main__":
    
    #number = 13195
    number = 600851475143
    fac = Factor(number)

    results = fac.factors()
    print("Factors of number {} is {}".format(number, results))

    primes = []
    for num in results:
        if ( Prime.isPrime(num) ):
            primes.append(num)

    print("In which primes are {}, max prime is {}".format(primes, max(primes)))
