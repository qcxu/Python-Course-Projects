__author__ = 'QiongchengXu'

import random


#This program allows user to play game Rock, Paper, Scissors against the computer. The weapon Rock is labeled as 1,
# Paper as 2, Scissors as 3 and Quit as 0 in the program.
def main():
    #Create variables to record game history.
    rounds_comp_win = 0
    rounds_user_win = 0
    rounds_tie = 0
    number_user_rock = 0
    number_user_paper = 0
    number_user_scissor = 0
    #Call the function to get the user input.
    user_weapon = get_user_input()

    #Create a variable to control the loop.
    flag = 0
    while flag == 0:
        #Determine if the user input is Quit.
        if user_weapon == 0:
            print "I'm sorry to see you go! You've proven to be a worthy adversary."
            print "The number of rounds the computer has won:", format(rounds_comp_win, "d") + "."
            print "The number of rounds the user has won:", format(rounds_user_win, "d") + "."
            print "The number of rounds that ended in a tie:", format(rounds_tie, "d") + "."
            print "The number of times the user selected rock:", format(number_user_rock, "d") + "; paper:", format(number_user_paper, "d") +"; scissors:", format(number_user_scissor, "d") +"."
            flag = 1
        else:
            #Record user weapon.
            if user_weapon == 1:
                number_user_rock += 1
            elif user_weapon == 2:
                number_user_paper += 1
            elif user_weapon == 3:
                number_user_scissor += 1
            #Computer generates the weapon.
            computer_weapon = choose_weapon()
            #Determine the winner.
            winner = determine_winner(user_weapon, computer_weapon)
            #Record game history.
            if winner == 0:
                rounds_tie += 1
            elif winner == 1:
                rounds_user_win += 1
            else:
                rounds_comp_win += 1
            #Print game results.
            print "You have chosen", weapon_name(user_weapon), "and the computer chose", weapon_name(computer_weapon), \
                ".", result(winner)
            #Continue the game by getting the user input.
            user_weapon = get_user_input()



#Get the user input and return
def get_user_input():
    #Create variable to control the loop
    flag = 0
    while flag == 0:
        user_weapon = raw_input("Please select You weapon: (R) for rock, (P) for paper, (S) for scissors, or (Q) to quit: ")
        #Determine the user weapon. If user input is "R" or "r", user weapon is labeled as 1. So as P, S and Q.
        #If user input is none of these, user should input again.
        if (user_weapon == "R") or (user_weapon == "r"):
            user_weapon = 1
            flag = 1
        elif (user_weapon == "P") or (user_weapon == "p"):
            user_weapon = 2
            flag = 1
        elif (user_weapon == "S") or (user_weapon == "s"):
            user_weapon = 3
            flag = 1
        elif (user_weapon == "Q") or (user_weapon == "q"):
            user_weapon = 0
            flag = 1
    return user_weapon


#Computer generates the weapon.
def choose_weapon():
    #Get a random number in the range of 1 through 3.
    comp_number = random.randint(1,3)
    return comp_number


#Compare the user weapon and computer weapon and return the winner.
#If the user weapon and computer weapon are the same, it is a tie, and the winner is labeled as 0. If the user wins,
# the winner is labeled as 1, and if the computer wins, the winner is labeled as 2.
#According to the rule that rock wins scissors, scissors wins paper, and paper wins rock, if the subtraction of user
# weapon and computer weapon is 1 or -2, the user wins, which is identical to the subtraction mod 3 equals 1. Else,
# computer wins.
def determine_winner(user_weapon, computer_weapon):
    if user_weapon == computer_weapon:
        winner = 0
    elif (user_weapon - computer_weapon) % 3 == 1:
        winner = 1
    else:
        winner = 2
    return winner


#Determine weapon from its number.
def weapon_name(weapon_number):
    if weapon_number == 1:
        return "Rock"
    elif weapon_number == 2:
        return "Paper"
    elif weapon_number == 3:
        return "Scissors"


#Determine game result from the label of winner.
def result(winner):
    if winner ==0:
        return "It's a tie!"
    elif winner == 1:
        return "You win!"
    else:
        return "You lose!"


#Call the main function.
main()