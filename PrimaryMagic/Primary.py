# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import sys

__author__ = "ThinkRedstone"
__date__ = "$18-Oct-2014 18:36:11$"


def __fill_list(lim):
    list = []
    for i in range(lim):
        list.append(i + 2)
    return list


def primes_up_to_x(lim):
    list = __fill_list(lim)
    for i in range(len(list)):
        if list[i] != 0:
            for j in range(i + 1, len(list)):
                if list[j] % list[i] == 0:
                    list[j] = 0
    return list


class PrimeCalculator:
    def __init__(self, number):
        self.number = number
        if self.number< 0:
            print("Only positives!")
            sys.exit("invalid input")

    def __del__(self):
        del self.number

    def get_number(self):
        return self.number

    def set_number(self, number):
        self.number = number

    def primary_factors(self):
        list = primes_up_to_x(self.number)
        for a in list:
            if a != 0:
                if self.number % a != 0:
                    list.remove(a)
        return list
