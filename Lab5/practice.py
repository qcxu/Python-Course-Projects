__author__ = 'QiongchengXu'

import random


def main():
    write_file()
    read_file()


def write_file():
    out_file = open("random_numbers.txt","w")
    n = 0
    while n < 1000:
        random_number = random.randint(0, 1000)
        out_file.write(str(random_number))
        out_file.write("\n")
        n += 1
    out_file.close()


def read_file():
    in_file = open("random_numbers.txt","r")
    total = 0
    numbers_contents = in_file.readlines()
    for number in numbers_contents:
        total += int(number)
    in_file.close()
    avg = total/1000
    print "sum:", total
    print "average:", avg


main()