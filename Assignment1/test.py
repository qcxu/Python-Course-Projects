__author__ = 'QiongchengXu'

def main():
    n1 = float(input("Enter number 1: "))
    n2 = float(input("Enter number 2: "))
    n3 = float(input("Enter number 3: "))
    avgN = average(n1, n2, n3)
    p = "a"
    print "The average:", p, format(avgN, ".1f")

def average(number1, number2, number3):
    avg = (number1 + number2 + number3) / 3
    return avg

main()

