__author__ = 'QiongchengXu'

#Function call divide that takes two parameters and do the quotient and print the result
def main():
    n1 = float(input("Please enter the first operand: "))
    operand = raw_input("Please enter the operator: ")
    n2 = float(input("Please enter the second operand: "))
    if operand == "+":
        addition = add(n1, n2)
        print n1, "+", n2, "=", addition
    elif operand == "-":
        subtraction = subtract(n1, n2)
        print n1, "-", n2, "=", subtraction
    elif operand == "*":
        product = multiply(n1, n2)
        print n1, "*", n2, "=", product
    elif operand == "/":
        if n2 == 0:
            print "Cannot divide by 0"
        else:
            division = divide(n1, n2)
            print n1, "/", n2, "=", division
    check = raw_input("Would you like to perform another calculation? (y for yes and n for no)" )
    while check == "y":
        n1 = float(input("Please enter the first operand: "))
        operand = raw_input("Please enter the operator: ")
        n2 = float(input("Please enter the second operand: "))
        if operand == "+":
            addition = add(n1, n2)
            print n1, "+", n2, "=", addition
        elif operand == "-":
            subtraction = subtract(n1, n2)
            print n1, "-", n2, "=", subtraction
        elif operand == "*":
            product = multiply(n1, n2)
            print n1, "*", n2, "=", product
        elif operand == "/":
            if n2 == 0:
                print "Cannot divide by 0"
            else:
                division = divide(n1, n2)
                print n1, "/", n2, "=", division
        check = raw_input("Would you like to perform another calculation? (y for yes and n for no) ")


def divide(number_one, number_two):
    result = number_one / number_two
    return result


def add(number_one, number_two):
    result = number_one + number_two
    return result


def subtract(number_one, number_two):
    result = number_one - number_two
    return result

def multiply(number_one, number_two):
    result = number_one * number_two
    return result


main()