__author__ = 'QiongchengXu'


def main():
    numbers = [10, 20, 24, 46, 65, 86, 98]
    avg = findAverage(numbers)
    print avg


def findAverage(numbers):
    sum = 0
    for number in numbers:
        sum += number
        avg = float(sum) / len(numbers)
    return avg


main()