#!/usr/bin/python3

class Adder:
    def __init__(self):
        pass

    @staticmethod
    def add(base, limit):
        count = base
        result = 0
        while count < limit:
            result += count
            count += base
        return result

if __name__ == "__main__":
    adder = Adder()
    result = adder.add(3, 1000) + adder.add(5, 1000) - adder.add(15, 1000)
    print("result is", result)

