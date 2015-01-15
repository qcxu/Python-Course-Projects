__author__ = 'QiongchengXu'


def main():
    message = winner("David", 55, "Kristen", 50)
    print message


def winner(name1, votes1, name2, votes2):
    message = ""
    if votes1 > votes2:
        message = name1
    elif votes1 == votes2:
        message = "tie"
    else:
        message = name2
    return message


main()