__author__ = 'QiongchengXu'


def main():
    num1 = float(input("Enter num1: "))
    num2 = float(input("Enter num2: "))
    num3 = float(input("Enter num3: "))
    avg = calculateAverage(num1, num2, num3)
    print avg


def calculateAverage(num1, num2, num3):
    avg = (num1 + num2 + num3) / 3
    return avg


main()