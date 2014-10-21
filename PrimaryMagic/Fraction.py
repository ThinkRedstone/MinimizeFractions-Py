from builtins import print
import sys

__author__ = 'ThinkRedstone'
from PrimaryMagic.Primary import PrimeCalculator


class Fraction:
    def __init__(self, string):
        try:
            self.numerator = PrimeCalculator(int(string.split("/")[0]))
            self.denominator = PrimeCalculator(int(string.split("/")[1]))
        except (ValueError , IndexError) as e:
            if e == ValueError:
                print("Only integers!")
                sys.exit("Invalid input!")
            else:
                print("Didn't obey template!(a/b)")
                sys.exit("Invalid input!")

    def __del__(self):
        del self.numerator
        del self.denominator

    def minimize_fraction(self, ):
        if self.numerator.get_number() < self.denominator.get_number():
            while True:
                log = self.numerator.get_number()
                print(
                    "working... Current fraction:", self.numerator.get_number(), "/", self.denominator.get_number())
                numList = self.numerator.primary_factors()
                for i in range(len(numList)):
                    if numList[i] != 0:
                        if self.denominator.get_number() % numList[i] == 0:
                            self.numerator.set_number(int(self.numerator.get_number() / numList[i]))
                            self.denominator.set_number(int(self.denominator.get_number() / numList[i]))
                if log == self.numerator.get_number():
                    break
        else:
            while True:
                log = self.numerator.get_number()
                print(
                    "working... Current fraction:", self.numerator.get_number(), "/", self.denominator.get_number())
                denList = self.denominator.primary_factors()
                for i in range(len(denList)):
                    if denList[i] != 0:
                        if self.numerator.get_number() % denList[i] == 0:
                            self.numerator.set_number(int(self.numerator.get_number() / denList[i]))
                            self.denominator.set_number(int(self.denominator.get_number() / denList[i]))
                if log == self.numerator.get_number():
                    break
        minFraction = "minimum fraction is: {0}/{1}".format(self.numerator.get_number(), self.denominator.get_number())
        return minFraction

while True:
    test = Fraction(input("Enter fraction:"))
    print(test.minimize_fraction())
    del test
