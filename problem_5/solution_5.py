#!/usr/bin/python3

class Factor:
    def __init__(self, number):
        self._number = number
        self._factors = []

    def _calculate(self, number):
        base = 2
        while base < number:
            if number % base == 0:
                self._factors.append(base)
                number = int( number / base )
            else:
                base = base + 1
        self._factors.append(number)

    def factors(self):
        self._calculate(self._number)
        return self._factors

class LeastCommonMultiple:
    
    def __init__(self, limit):
        self._limit = limit
        self._multiples = []

    def _calculate(self):
        for number in range(self._limit, 1, -1):
            fac = Factor(number)
            factors = fac.factors()
            for factor in factors:
                exists = self._multiples.count(factor)
                current = factors.count(factor)
                if current > exists:
                    for i in range(current - exists):
                        self._multiples.append(factor)

    def multiples(self):
        self._calculate()
        print("DEBUG: least common factors from 1 to {} are: {}".format(self._limit, self._multiples))
        result = 1
        for i in self._multiples:
            result = result * i
        return result

if __name__ == "__main__":

    number = 20
    lcm = LeastCommonMultiple(number)
    multiples = lcm.multiples()
    print("Least common multiple of number {} is {}".format(number, multiples))
        
