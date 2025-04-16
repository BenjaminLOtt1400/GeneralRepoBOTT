# This project will be built on the idea of a player constructing a team of fighters that go against a computer team
# The teams will work on a 5v5 style with the player entering names with characterists randomly generated
# The game will pit fighters against eachother where the winner will re-enter the party and wait until the next match
# The fighers will have 3 main stats that will calculate against the other fighter in the round
# Strength will determine the damage of the fighter ranging from 3-7
# Health will be the health of the fighter that will move with them between rounds ranging from 20-40
# Speed will determine which of the fighters attacks first ranging from 1-5
# The fighter with the higher speed will attack first and will go back and forth until one character dies
# The Winning character will regain 20 health
# Once a team has no fighters left, they lose

import random
from FighterStats import Fighter_stats
import time


# Function that creates the team for the player
def Player_names():
    player_names = list()
    for i in range(5):
        i = input('Please enter the name of your character')
        player_names += i
    forward = input('All Fighters have been named. Press Enter to Continue!')
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
        computer_names.append(total_names[i-1])
        total_names.pop(i-1)
        names_length = len(total_names)
        random.shuffle(total_names)
    
    return computer_names
    

# TODO Function that has fighters face off against eachother, returns the victories fighter to the team's roster
def Battle(player_fighter, computer_fighter):
    turn_order = [player_fighter,computer_fighter]
    turn_order = sorted(turn_order)
    print(f'current battle {player_fighter.name} {computer_fighter.name}')
    while turn_order[0].health > 0:
        print(f'{turn_order[0].name} attacks {turn_order[1].name}!')
        turn_order[1].health -= turn_order[0].strength
        print(f'{turn_order[1].name} took {turn_order[0].strength} damange!')
        if turn_order[1].health <= 0:
            break
        if turn_order[1].health > 0:
            print(f'{turn_order[1].name} attacks {turn_order[0].name}!')
            turn_order[0].health -= turn_order[1].strength
            print(f'{turn_order[0].name} took {turn_order[1].strength} damage!')
            if turn_order[0].health <= 0:
                break
    if turn_order[0].health > 0:
        turn_order[0].health += 20
        print(f'{turn_order[0].name} is victorious, regain 20 health!')
        print(turn_order[0])
        forward = input('Press Enter to proceed to the next battle!')
        
        return turn_order[0], turn_order[1]
    else:
        print(f'{turn_order[1].name} is victorious, regain 20 health!')
        turn_order[1].health += 20
        print(turn_order[1])
        forward = input('Press Enter to proceed to the next battle!')

        return turn_order[1], turn_order[0]


def main():
    # TODO introduce that player to the game and explain the rules
    
    # Have the player name their 5 fighters and generate thier stats
    player_team_data = Player_names()
    player_team_obj = []
    for i in range(len(player_team_data)):
        name = player_team_data[i]
        strength = random.randint(3, 7)
        health = random.randint(20, 40)
        speed = random.randint(1, 5)
        player_team_obj.append(Fighter_stats(name, strength, health, speed))
        print(player_team_obj[i])
        i += 1
        time.sleep(0)
        
    # TODO Generate the computer's team with their names and generate their stats
    computer_team_data = Computer_names()
    computer_team_obj = []
    for i in range(len(computer_team_data)):
        name = computer_team_data[i]
        strength = random.randint(3, 7)
        health = random.randint(20, 40)
        speed = random.randint(1, 5)
        computer_team_obj.append(Fighter_stats(name, strength, health, speed))
        print(computer_team_obj[i])
        i += 1
        time.sleep(0)
    
    # TODO Have fighters from the 2 teams face off 1v1, edit their health stats and winner moves on
    player_char_count = len(player_team_obj)
    cpu_char_count = len(computer_team_obj)
    while player_char_count > 0 or cpu_char_count > 0:
        elimination_list = list()
        lower_count = player_char_count if player_char_count < cpu_char_count else cpu_char_count
        for i in range(lower_count):
            Battle(player_team_obj[i], computer_team_obj[i])
            if player_team_obj[i].health <= 0:
                elimination_list.append(player_team_obj[i])
            if computer_team_obj[i].health <= 0:
                elimination_list.append(computer_team_obj[i])
        elimination_range = len(elimination_list)
        for i in range(elimination_range):
            if elimination_list[i].name in player_team_obj:
                player_team_obj.remove(elimination_list[i])
            elif elimination_list[i].name in computer_team_obj:
                computer_team_obj.remove(elimination_list[i])
        elimination_list.clear()
        player_char_count = len(player_team_obj)
        cpu_char_count = len(computer_team_obj)
    print('Fighting loop finished')
    # TODO Announce winner of the fights
    # 
    pass



if __name__ == '__main__':
    main()