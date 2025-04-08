# This project will be built on the idea of a player constructing a team of fighters that go against a computer team
# The teams will work on a 5v5 style with the player entering names with characterists randomly generated
# The game will pit fighters against eachother where the winner will re-enter the party and wait until the next match
# The fighers will have 3 main stats that will calculate against the other fighter in the round
# Strength will determine the damage of the fighter ranging from 1-5
# Health will be the health of the fighter that will move with them between rounds ranging from 10-20
# Speed will determine which of the fighters attacks first ranging from 1-5
# The fighter with the higher speed will attack first and will go back and forth until one character dies
# Once a team has no fighters left, they lose

import random
from FighterStats import Fighter_stats


# Function that creates the team for the player
def Player_names():
    player_names = list()
    for i in range(5):
        i = input('Please enter the name of your character')
        player_names += i
    return player_names


# Function that creates the team for the computer
def Computer_names():
    computer_names = list()
    total_names = list()
    file = open('NamesFile.txt', 'r')
    
    for x in file:
        total_names.append(x)
    file.close
    total_names = list(map(str.strip, total_names))
    names_length = len(total_names)
    
    for i in range(5):
        i = random.randint(0, names_length)
        computer_names.append(total_names[i])
        total_names.pop(i)
        random.shuffle(total_names)
    
    return computer_names
    

# TODO Function that has fighters face off against eachother, returns the victories fighter to the team's roster
def Battle(player_fighter, computer_fighter):
    turn_order = []
    for fast in sorted(player_fighter, computer_fighter):
        turn_order.append(fast)
    if player_fighter.speed == computer_fighter.speed:
        random.shuffle(turn_order)
 
    position_1 = turn_order[0]
    position_2 = turn_order[1]
    
    while position_1.health > 0:
        position_2.health - position_1.strength
        if position_2.health > 0:
            position_1.health - position_2.strength
    if position_1.health > 0:
        return position_1
    else:
        return position_2
    





def main():
    # TODO introduce that player to the game and explain the rules
    
    # Have the player name their 5 fighters and generate thier stats
    player_team_data = Player_names()
    player_team_obj = []
    for i in range(len(player_team_data)):
        name = player_team_data[i]
        strength = random.randint(1, 5)
        health = random.randint(10, 20)
        speed = random.randint(1, 5)
        fighter = Fighter_stats(name, strength, health, speed)
        player_team_obj.append(fighter)
        print(player_team_obj)
        
    # TODO Generate the computer's team with their names and generate their stats
    computer_team_data = Computer_names()
    computer_team_obj = []
    for i in range(len(computer_team_data)):
        name = computer_team_data[i]
        strength = random.randint(1, 5)
        health = random.randint(10, 20)
        speed = random.randint(1, 5)
        fighter = Fighter_stats(name, strength, health, speed)
        computer_team_obj.append(fighter)
    
    # TODO Have fighters from the 2 teams face off 1v1, edit their health stats and winner moves on
    Battle(player_team_obj[1], computer_team_obj[1])
    # TODO Announce winner of the fights
    # 
    pass



if __name__ == '__main__':
    main()