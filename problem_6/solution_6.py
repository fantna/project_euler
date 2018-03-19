#!/usr/bin/python3

limit = 100
series = range(1, limit+1)
squareSum = 0
sumSquare = 0
for number in series:
    squareSum += number*number
total = sum(series)
sumSquare = total*total

result = sumSquare - squareSum

print("Difference between the sum of the squares of the first {} natural numbers and the square of the sum is {}".format(limit, result))
