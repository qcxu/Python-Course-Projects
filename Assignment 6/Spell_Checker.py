__author__ = 'QiongchengXu'


#In this program, read in "input.txt" and "dictionary.txt", determine the misspelled words according to the dictionary,
#and print the text into html with misspelled words underlined and bold.
def main():
    #Read files "input.txt" and "dictionary.txt"
    input_file = read_file("input.txt")
    dictionary_file = read_file("dictionary.txt")

    #Transform each file into a list of line of strings
    dictionary_list = file_to_list(dictionary_file)
    input_file_content = file_to_list(input_file)

    #Remove whitespace in the words in dictionary
    normalized_dictionary_list = normalize_dictionary_list(dictionary_list)

    #Determine whether the word in "input.txt" is in the dictionary
    misspelled_word_dictionary = check_misspell(input_file_content, normalized_dictionary_list)

    #Print misspelled words and the number of times they are misspelled in "input.txt"
    print_misspelled_words(misspelled_word_dictionary)

    #Print the text to a file named spelling_correction.html with misspelled words underlined and bold
    output_file = open("spelling_correction.html", "w")
    print_header()
    print_to_html(input_file_content, misspelled_word_dictionary)
    print_footer()

    #Close all files
    input_file.close()
    dictionary_file.close()
    output_file.close()


#Read the file with filename
def read_file(filename):
    out_file = open(filename, "r")
    return out_file


#Transform the file to a list of line of strings
def file_to_list(file_type):
    file_content = file_type.readlines()
    return file_content


#Remove whitespace of the words in dictionary and turn all words to lowercase
def normalize_dictionary_list(dictionary_list):
    normalized_dictionary_list = []
    for word in dictionary_list:
        word = word.strip()
        word = word.lower()
        normalized_dictionary_list.append(word)
    return normalized_dictionary_list


#Determine whether the word in input_file_content is in the dictionary
def check_misspell(input_file_content, dictionary_list):
    #Create a dictionary for misspelled word
    misspelled_word_dictionary = dict()
    for line in input_file_content:
        #Remove punctuation in the line and turn the line into lowercase
        line = remove_punctuation(line)
        #Split the line into a list of words
        line_of_words = line.split(" ")
        for word in line_of_words:
            #Remove whitespace of the word
            word = word.strip()
            #Determine misspelled word and count the number of times occurs
            if word != '':
                if word not in dictionary_list:
                    if word not in misspelled_word_dictionary:
                        misspelled_word_dictionary[word] = 1
                    else:
                        misspelled_word_dictionary[word] += 1

    return misspelled_word_dictionary


#Remove the punctuation from the line, and turn the line into lowercase
def remove_punctuation(line):
    #Transform the line to lowercase
    line = line.lower()
    #Remove punctuation
    line = line.replace(',', '')
    line = line.replace('.', '')
    line = line.replace('<', '')
    line = line.replace('>', '')
    line = line.replace('(', '')
    line = line.replace(')', '')
    line = line.replace('=', '')
    line = line.replace('"', '')
    line = line.replace(':', '')
    line = line.replace('/', '')
    line = line.replace('*', '')
    line = line.replace('[', '')
    line = line.replace(']', '')
    line = line.replace('+', '')
    line = line.replace('?', '')
    line = line.replace('_', '')
    line = line.replace("'", '')
    line = line.replace('-', '')
    line = line.replace('@', ' ')
    return line


#Print misspelled word with the number of times it occurs
def print_misspelled_words(misspelled_word_dictionary):
    for key in misspelled_word_dictionary:
        print key, misspelled_word_dictionary[key]


#Print the text to a file named spelling_correction.html with misspelled words underlined and bold
def print_to_html(input_file_content, misspelled_word_dictionary):
    for line in input_file_content:
        line_of_words = line.split()
        output_file = open("spelling_correction.html", "a")
        for word in line_of_words:
            #Remove punctuation and whitespace in the word for comparison to misspelled word dictionary
            simple_word = remove_punctuation(word).strip()
            #Transform the word to display as plain text in html if the word includes &, ", <, >
            word = replace_for_html(word)
            #Determine whether the word is in misspelled word dictionary
            if simple_word in misspelled_word_dictionary:
                #Print word underlined and bold
                output_file.writelines("<u><b>" + word + "</b></u> ")
            else:
                #Print word normally
                output_file.writelines(word)
            #Add a space after each word
            output_file.writelines("&nbsp;")


#Print html header
def print_header():
    output_file = open("spelling_correction.html", "a")
    output_file.writelines("<html><head><title>Correction</title></head><body><br />")


#Transform word to display as plain text in html if the word includes &, ", <, >
def replace_for_html(word):
    word = word.replace('&', '&amp;')
    word = word.replace('"', '&quot;')
    word = word.replace('<', '&lt;')
    word = word.replace('>', '&gt;')
    return word


#Pring html footer
def print_footer():
    output_file = open("spelling_correction.html", "a")
    output_file.writelines("</body></html>")


#Call the main function
main()