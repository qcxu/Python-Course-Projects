__author__ = 'QiongchengXu'


#This program asks user to input a file name, and output the number of uppercase letter, lowercase letter, digit
#and whitespace in the file.
def main():
    #Enter file name
    file_name = raw_input("Enter the name of your file: ")
    #Open file, mode is "read"
    out_file = open(file_name, "r")
    #Read the entire contents of the file
    file_contents = out_file.readlines()
    count_upper = 0
    count_lower = 0
    count_digit = 0
    count_space = 0
    for line in file_contents:
        for character in line:
            #Count uppercase letter
            if character.isupper():
                count_upper += 1
            #Count lowercase letter
            elif character.islower():
                count_lower += 1
            #Count digit
            elif character.isdigit():
                count_digit += 1
            #Count whitespace
            elif character.isspace():
                count_space += 1
    #Print output
    print "Uppercase count:", count_upper
    print "Lowercase count:", count_lower
    print "Digit count:", count_digit
    print "Space count:", count_space
    #Close the file
    out_file.close()


#Call the main function
main()


