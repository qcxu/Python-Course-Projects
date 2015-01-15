__author__ = 'QiongchengXu'


def main():
    all_numbers = [7, 9, 10, 5]
    summation = add_all_numbers(all_numbers)
    smallest = smallest_int(all_numbers)
    print summation
    print smallest


def add_all_numbers(all_numbers):
    sum = 0
    for numbers in all_numbers:
        sum = sum + numbers
    return sum


def smallest_int(all_numbers):
    small = all_numbers[0]
    for numbers in all_numbers:
        if numbers < small:
            small = numbers
    return small


main()