__author__ = 'QiongchengXu'


def main():
    List_of_numbers = [2, 4, 5, 6, 7, 8, 9]
    count = howManyEvenNumbers(List_of_numbers)
    print count


def howManyEvenNumbers(List_of_numbers):
    count = 0
    for List_of_number in List_of_numbers:
        if List_of_number % 2 == 0:
            count += 1
    return count


main()