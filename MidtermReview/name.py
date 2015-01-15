__author__ = 'QiongchengXu'


def main():
    print int(2.1+3.7)/2.0
    name1 = raw_input("name1: ")
    name2 =raw_input("name2: ")
    compare_names(name1, name2)


def compare_names(name1, name2):
    if name1 < name2:
        print name1
    else:
        print name2


main()