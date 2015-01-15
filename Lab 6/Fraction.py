__author__ = 'QiongchengXu'
from math import *

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator


    def add(self, other):
        my_fraction = self.numerator/self.denominator
        other_fraction = other.numerator/other.denominator
        return my_fraction + other_fraction


    def sum(self, other):
