__author__ = 'QiongchengXu'

def main():
    lnumber = largest_input()
    print lnumber


def largest_input():
    number = int(input("Enter a number: "))
    largest_number = 0
    while number != -1:
        if number > largest_number:
            largest_number = number
        number = int(input("Enter a number: "))
    return largest_number

main()
