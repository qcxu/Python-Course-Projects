__author__ = 'QiongchengXu'
#This program asks the buyer for the price of their item and determines their change in terms of quarters, dimes,
# and nickels.


def main():
    #Call the function to get the cost of the item.
    cost = get_user_input()
    #Check if the item price is $1, if so then print "1 dollar" instead of "cents".
    if cost == 100:
        unit = "dollar"
        price_to_print = 1
    else:
        unit = "cents"
        price_to_print = cost
    print "You bought an item for", format(price_to_print, "d"), unit, "and gave me a dollar."
    #Call the function to determine the change and output the change.
    calculate_correct_amount_of_change(cost)


#Get the cost of the item.
def get_user_input():
    item_price = int(input("Enter price of item (from 25 cents to $1, in 5-cent increments): "))
    #Check if user enters 1 for $1, if so change the price to 100 cents.
    if item_price == 1:
        item_price = 100
    return item_price


#Calculate the change in terms of quarters, dimes and nickels, and output the change.
def calculate_correct_amount_of_change(cost_of_item):
    #Calculate the amount of change.
    change = 100 - cost_of_item
    #Calculate the number of quarters in change.
    number_of_quarters = change / 25
    #Calculate the number of dimes in change.
    remain_after_quarter = change % 25
    number_of_dimes = remain_after_quarter / 10
    #Calculate the number of nickels in change.
    remain_after_nickels = remain_after_quarter % 10
    number_of_nickels = remain_after_nickels / 5
    #Check the grammar for singular or plural.
    if number_of_quarters == 1:
        quarter_string = "quarter,"
    else:
        quarter_string = "quarters,"
    if number_of_dimes == 1:
        dime_string = "dime,"
    else:
        dime_string = "dimes,"
    if number_of_nickels == 1:
        nickel_string = "nickel."
    else:
        nickel_string = "nickels."
    #Output the amount of change in terms of quarter, dime and nickel.
    print "Your change is", format(number_of_quarters, "d"), quarter_string, format(number_of_dimes, "d"), dime_string,\
        format(number_of_nickels, "d"), nickel_string

#Call main function
main()