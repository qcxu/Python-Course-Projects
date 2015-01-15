__author__ = 'jasocarter'
from MyPoint import *


def main():
    first_point = MyPoint(3, 4)

    another_point = MyPoint(4, 5)

    distance_between_two_points = first_point.distance(another_point)

    print "The value of of the first x is:", first_point.x, \
        "The value of the first y is:", first_point.y

    print "The value of of the second x is:", another_point.x, \
        "The value of the second y is:", another_point.y

    print "The distance between the two points are: ", distance_between_two_points


main()

