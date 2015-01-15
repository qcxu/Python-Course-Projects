__author__ = 'QiongchengXu'




def main():
    list_of_numbers = [1, 2, 3, 4]
    reverselist = reverse(list_of_numbers)
    print reverselist


def reverse(list_of_numbers):
    reverse_list = []
    count = len(list_of_numbers)
    i = 0
    while i < count:
        reverse_list.append(list_of_numbers[count-i-1])
        i += 1
    return reverse_list

main()
