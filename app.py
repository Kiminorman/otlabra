#!/usr/bin/python
import sys

# Implementation of FizzBuzz v0.00

# Version 1: if number is divisible by 3, print Fizz
#            if number is divisible by 5, print Buzz
#            if both, print FizzBuzz
#            else print number

# Version 2: if number is prime, print "<number> is a prime" instead
#            Take one argument,  and count up to it

class FizzBuzz():
    def __init__(self):
        pass

    # Version 2
    def run(self, end, out=sys.stdout):
        for i in range(3, (end+1)):
            for n in range(2, i):
                if ((i % n) == 0):
                        break
            else:
                        print i, "is a prime"

    # Seems to give correct values. Tested with 1 and 2.
    def calc(self, i):
        return i

if __name__ == "__main__":
    app = FizzBuzz()
    app.run(int(sys.argv[1]))
