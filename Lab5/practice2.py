__author__ = 'QiongchengXu'


def main():
    sentence = raw_input("Please input a sentence: ")
    number_space = 0
    for character in sentence:
        if character.isspace():
            number_space += 1
    print number_space


main()