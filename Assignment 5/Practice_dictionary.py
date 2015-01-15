__author__ = 'QiongchengXu'


def main():
    out_file = open("test.txt", "r")
    file_contents = out_file.readlines()
    word_dictionary = dict()
    for line in file_contents:
        line = line.strip()
        line = line.lower()
        line = line.replace(',', '')
        line = line.replace('.', '')
        words = line.split(' ')
        for word in words:
            if word not in word_dictionary:
                word_dictionary[word] = 1
            else:
                word_dictionary[word] += 1
    for key in word_dictionary:
        print key, word_dictionary[key]
    out_file.close()


main()


