__author__ = 'QiongchengXu'

def main():
    age = int(input("Please enter your age: "))
    legalize(age)


def legalize(age):
    if age >= 21:
        print("You are allowed to drink alcohol!")
    else:
        print("You are not allowed to drink alcohol!")


main()