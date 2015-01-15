__author__ = 'QiongchengXu'


def main():
    #read file
    file_contents = read_file()

    #Initiate highest of other stats
    minutes = ["", "", 0]
    games_played = ["", "", 0]
    points = ["", "", 0]
    rebounds = ["", "", 0]
    penalties = ["", "", 0]
    freethrows = ["", "", 0]

    #Create list to store all players' efficiency stats
    all_player_stats = []

    for line in file_contents:
        #Split stats by ',' to get a list of single player's stats
        player_stats = line.split(',')
        #Remove space in player's stats and convert string to int if necessary
        player = standardize_player(player_stats)
        #Calculate efficiency of each player
        player_efficiency = calculate_stats(player)
        #Append player to all players' efficiency list
        all_player_stats.append(player_efficiency)

        #Get the highest number of other stats
        minutes = compare_other_stats(player[7], minutes, player)
        games_played = compare_other_stats(player[6], games_played, player)
        points = compare_other_stats(player[8], points, player)
        rebounds = compare_other_stats(player[11], rebounds, player)
        penalties = compare_other_stats(player[16], penalties, player)
        freethrows = compare_other_stats(player[20], freethrows, player)

    #Sort all players' efficiency list
    ordered_list = sorted(all_player_stats, key=lambda x: x[2], reverse=True)
    #Write top 50 players' stats into "player efficiency.txt"
    out_file = open("player efficiency.txt", "w")
    i = 0
    while i < 50:
        out_file.write(ordered_list[i][0] + " " + ordered_list[i][1] + ", " + format(ordered_list[i][2], ".2f") + "\n")
        i += 1
    out_file.close()

    #Print other stats
    print "Most minutes played:", minutes[0], minutes[1] + ", " + format(minutes[2], ".0f")
    print "Most games played:", games_played[0], games_played[1] + ", " + format(games_played[2], ".0f")
    print "Most points scored:", points[0], points[1] + ", " + format(points[2], ".0f")
    print "Most rebounds got:", rebounds[0], rebounds[1] + ", " + format(rebounds[2], ".0f")
    print "Most penalties got", penalties[0], penalties[1] + ", " + format(penalties[2], ".0f")
    print "Most freethrows made", freethrows[0], freethrows[1] + ", " + format(freethrows[2], ".0f")


def read_file():
    #read file
    out_file = open("player_regular_season.csv", "r")
    file_contents = out_file.readlines()
    out_file.close()
    #file preprocessing
    file_contents.remove(file_contents[0])
    file_length = len(file_contents)
    file_contents.remove(file_contents[file_length-1])
    file_contents.remove(file_contents[file_length-2])
    file_contents.remove(file_contents[file_length-3])

    return file_contents


def standardize_player(single_player):
    #Remove space in elements of player_stats and store into player
        player = []
        for element in single_player:
            if element.strip() == "NULL" or element.strip() == '0':
                element = 0
            else:
                if element.strip().isdigit():
                    element = float(element.strip())
                else:
                    element = element.strip()
            player.append(element)

        return player


#Calculate player's efficiency
def calculate_stats(player):
    player_efficiency = []
    efficiency = (player[8] + player[11] + player[12] + player[13] + player[14] - (player[17] - player[18] + player[19] - player[20] + player[15])) / player[6]
    player_efficiency.append(player[2])
    player_efficiency.append(player[3])
    player_efficiency.append(efficiency)

    return player_efficiency


#Compare player's score with highest in other stats
def compare_other_stats(player_score, highest_score, player):
    if player_score > highest_score[2]:
        highest_score[0] = player[2]
        highest_score[1] = player[3]
        highest_score[2] = player_score

    return highest_score


main()