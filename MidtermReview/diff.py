__author__ = 'QiongchengXu'

def main():
    list_numbers = [8, 67, 100, 34, 23]
    difference = diff(list_numbers)
    print difference


def diff(list_numbers):
    max = list_numbers[0]
    min = list_numbers[0]
    for number in list_numbers:
        if number >= max:
            max = number
        elif number <= min:
            min = number
    print max
    print min
    diff = max - min
    return diff

main()