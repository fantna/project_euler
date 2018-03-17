#!/usr/bin/python3

class Fibonacci:
    def __init__(self, limit):
        self._limit = limit
        self._series = [1, 2]

    def _calculate(self, num1, num2, limit):
        temp = num2
        num2 += num1
        num1 = temp
        if num2 > limit:
            return
        
        self._series.append(num2)
        self._calculate(num1, num2, limit)

    def series(self):
        self._calculate(1, 2, self._limit)
        return self._series


if __name__ == "__main__":
    fib = Fibonacci(4000000)
    numbers = fib.series()
    
    total = 0
    for even in numbers[1::3]:
        total += even

    print("Sum of even numbers are:", total)
 
