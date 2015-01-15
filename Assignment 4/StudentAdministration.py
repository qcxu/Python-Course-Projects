__author__ = 'QiongchengXu'


#This program is a student administration.
def main():
    name_lists = ["Ellen", "Sam", "Victoria", "Rachel", "Austin"]
    major_lists = ["Information Library Science", "English", "Computer Science", "History", "Chemistry"]

    #Create a variable stop_flag to check if stop the loop.
    stop_flag = 0
    #Create a variable to store duplicate major's index.
    major_duplicate_index_list = []

    while stop_flag == 0:
        #Print instructions
        option = print_instructions()
        #Option 1: Add a student. If the student's major already exists, print message and print instructions again.
        if option == 1:
            name = raw_input("What is the new student's name? ")
            major = raw_input("What is the new student's major? ")
            #Check if major is already in the list. If not, add student and major into lists.
            if check_list(major, major_lists):
                print major, "is already in the list."
            else:
                #Add student's name and major to the lists.
                name_lists.append(name)
                major_lists.append(major)
        #Option 2: Print all students' name.
        elif option == 2:
            for name_list in name_lists:
                print name_list
        #Option 3: Print all majors.
        elif option == 3:
            for major_list in major_lists:
                print major_list
        #Option 4: Input a student's name and print his/her name and major.
        elif option == 4:
            name = raw_input("Please input a student's name: ")
            major_for_student_name(name, name_lists, major_lists)
        #Option 5: Quit. Print "done".
        elif option == 5:
            print "done"
            #Label the stop_flag as 1 to stop loop.
            stop_flag = 1


#Print instructions and get user input.
def print_instructions():
    print "Please select an action:"
    print "1. Add a student"
    print "2. Print all students"
    print "3. Print all majors"
    print "4. Look up a student's major by their name"
    print "5. Quit"
    option = int(input("Choose an option: "))
    return option


#Check if the item is in the list.
def check_list(list_item, lists):
    if list_item in lists:
        return True
    else:
        return False


#Find student's major from the major_lists according to student's name.
def major_for_student_name(name, name_lists, major_lists):
    if name in name_lists:
        #Get the index of name from name_lists.
        index = name_lists.index(name)
        #Get the major from the index of major_lists.
        major = major_lists[index]
        print name + "'s major is", major
    else:
        print name, "does not exist."


#Call the main() function.
main()