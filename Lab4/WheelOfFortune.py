from Player import Player
from string import maketrans
import random


def main():
    # read information from file
    wheel_values = read_wheel_values()
    wheel_puzzles = read_wheel_puzzles()

    # randomly choose a puzzle
    puzzle = choose_puzzle(wheel_puzzles)
    puzzle = puzzle.lower()

    # call the change_to_underscore_puzzle(puzzle) function to change the puzzle to underscores
    underscore_puzzle = change_to_underscore_puzzle(puzzle)

    #call the play_game function to play the game
    play_game(underscore_puzzle, puzzle, wheel_values)


# read wheel puzzles from a file, store them in a list, and return the list
def read_wheel_puzzles():
    wheel_puzzles_file = open("wheel_puzzles.txt")
    wheel_puzzles = list()

    for line in wheel_puzzles_file:
        wheel_puzzles.append(line)

    wheel_puzzles_file.close()

    return wheel_puzzles


#read wheel values from a file, store them in a list, and return the list
def read_wheel_values():
    wheel_values_file = open("wheel_values.txt")

    wheel_values = list()
    for line in wheel_values_file:
        wheel_values.append(line)

    wheel_values_file.close()

    return wheel_values


#changes a puzzle from letters to underscores
def change_to_underscore_puzzle(puzzle):
    intab = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "
    outtab = "____________________________________________________ "
    trantab = maketrans(intab, outtab)

    return puzzle.translate(trantab)


#do not call this function	
def get_index_list(user_guess, puzzle, blank_puzzle):
    index_list = list()
    index = 0
    for letter in puzzle:
        if letter == user_guess:
            index_list.append(index)
        index += 1

    return index_list


#do not call this function
def swap_letters(user_guess, puzzle, blank_puzzle, index_list):
    index = 0
    blank_puzzle_list = list(blank_puzzle)
    for letter in blank_puzzle_list:
        if index in index_list:
            blank_puzzle_list[index] = user_guess

        index += 1

    return blank_puzzle_list


#this function replaces underscores with the correct user_guess
def transform_puzzle(user_guess, puzzle, blank_puzzle):
    index_list = get_index_list(user_guess, puzzle, blank_puzzle)
    transformed_puzzle = swap_letters(user_guess, puzzle, blank_puzzle, index_list)
    return transformed_puzzle


#randomly choose wheel_value from the wheel_values list
def spin_wheel(wheel_values):
    length = len(wheel_values)
    chosed_index = random.randint(0, length - 1)
    chosed_wheel_value = int(wheel_values[chosed_index])
    return chosed_wheel_value


#randomly choose wheel_puzzle from the wheel_puzzles list
def choose_puzzle(wheel_puzzles):
    length = len(wheel_puzzles)
    chosed_index = random.randint(0, length - 1)
    chosed_wheel_puzzle = wheel_puzzles[chosed_index]
    return chosed_wheel_puzzle


#Check if user guess is equal to puzzle
def is_guess_in_puzzle(user_guess, puzzle):
    if user_guess in puzzle:
        return True
    else:
        return False


#Compute player's current score
def compute_player_score(number_of_times_letter_is_in_puzzle, spin_value):
    score = number_of_times_letter_is_in_puzzle * spin_value
    return score


def play_game(under_score_puzzle, puzzle, wheel_values):
    player1_name = raw_input("Player 1 please enter your name: ")
    player2_name = raw_input("Player 2 please enter your name: ")
    player3_name = raw_input("Player 3 please enter your name: ")
    player1 = Player(player1_name, 0)
    player2 = Player(player2_name, 0)
    player3 = Player(player3_name, 0)
    player_lists = [player1, player2, player3]
    user_guess_list = []
    number_of_player = 0
    flag_keep_on = 1
    while flag_keep_on == 1:
        print player_lists[number_of_player].name
        print "The puzzle is", under_score_puzzle.rstrip()
        print "You have", player_lists[number_of_player].score, "dollars"
        action = raw_input("What would you like to do Spin (spin) or Solve (solve): ")
        while action != "spin" and action != "solve":
            action = raw_input("What would you like to do Spin (spin) or Solve (solve): ")
        if action == "spin":
            spin_value = spin_wheel(wheel_values)
            #Check spin value
            if spin_value == -1:
                player_lists[number_of_player].score = 0
                number_of_player = (number_of_player + 1) % 3
                print "Your spin is: Bankrupt"
                print "You lose and Your turn"
            elif spin_value == -2:
                number_of_player = (number_of_player + 1) % 3
                print "Your spin is: Lose Turn"
                print "You lose and Your turn"
            else:
                print "Your spin is:", spin_value
                user_guess = raw_input("Please guess a vowel or a consonant: ")
                #Check if user_guess has already been guessed.
                if user_guess in user_guess_list:
                    number_of_player = (number_of_player + 1) % 3
                    print "Your letter", user_guess, "has already been guessed."
                else:
                    #Record user_guess in the user_guess_list.
                    user_guess_list.append(user_guess)
                    #Check if user_guess is in the puzzle.
                    if is_guess_in_puzzle(user_guess, puzzle):
                        puzzle_with_underscores_and_letters = transform_puzzle(user_guess, puzzle, under_score_puzzle)
                        puzzle_with_underscores_and_letters = "".join(puzzle_with_underscores_and_letters)
                        number_of_times_letter_is_in_puzzle = puzzle.count(user_guess)
                        score = compute_player_score(number_of_times_letter_is_in_puzzle, spin_value)
                        player_lists[number_of_player].score += score
                        under_score_puzzle = puzzle_with_underscores_and_letters
                        #Check if user solved the puzzle
                        if puzzle_with_underscores_and_letters == puzzle:
                            print "You win!"
                            print "You won", player_lists[number_of_player].score, "dollars total!"
                            print "The phrase was", puzzle
                            flag_keep_on = 0
                    else:
                        number_of_player = (number_of_player + 1) % 3
                        print "Your letter is not in the puzzle"
        else:
            solve_puzzle = raw_input("Please enter the letters of the puzzle: ")
            if solve_puzzle == puzzle.rstrip():
                print "You win!"
                print "You won", player_lists[number_of_player].score, "dollars total!"
                print "The phrase was", puzzle
                flag_keep_on = 0
            else:
                print "Wrong. You lose your turn."
                number_of_player = (number_of_player + 1) % 3


main()
