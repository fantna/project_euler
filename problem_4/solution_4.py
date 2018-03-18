#!/usr/bin/python3

class Palindrome:
    def __init__(self):
        pass

    @staticmethod
    def isPalindrome(number):
        digits = []
        temp = number
        while temp > 0:
            digits.append( temp % 10)
            temp = int( temp / 10 )

        origin = list(digits)
        digits.reverse()
        return origin == digits

if __name__ == "__main__":
    # There should be a better solution
    result = 0
    for i in range(999, 99, -1):
        for j in range(i, 99, -1):
            number = i * j
            if Palindrome.isPalindrome(number):
                if number > result: 
                    result = number

    print("Found number is", result)
