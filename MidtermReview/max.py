__author__ = 'QiongchengXu'


def main():
    num1 = input("Enter num1: ")
    num2 = input("Enter num2: ")
    max_number = max(num1, num2)
    print max_number


def max(num1, num2):
    if num1 >= num2:
        return num1
    else:
        return num2


main()