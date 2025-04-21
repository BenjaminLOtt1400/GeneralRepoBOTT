# This project will be built on the idea of a player constructing a team of fighters that go against a computer team
# The teams will work on a 5v5 style with the player entering names with characterists randomly generated
# The game will pit fighters against eachother where the winner will re-enter the party and wait until the next match
# The fighers will have 4 main stats that will calculate against the other fighter in the round
# Strength will determine the damage of the fighter ranging from 3-7
# Health will be the health of the fighter that will move with them between rounds ranging from 20-40
# Speed will determine which of the fighters attacks first ranging from 1-5
# Luck will determine how likely a critical hit will occure ranging from 1-10
# Criticals range on a random number from 1-30 anything past a 25 causes a critical to occure 2x damage
# The fighter with the higher speed will attack first and will go back and forth until one character dies
# The Winning character will regain 20 health
# Once a team has no fighters left, they lose
import os
import pip
import random
import time
from FighterStats import Fighter_stats
import urllib.request

try:
    from playsound import playsound
except ModuleNotFoundError:
    print('Missing necessary import module, playsound')
    print('Program will force exit, please run again with installed module')
    print('Playsound will be installed in 5 seconds')
    time.sleep(5)
    pip.main(['install', 'playsound==1.2.2'])
    os._exit(0)

git_url = 'https://raw.githubusercontent.com/BenjaminLOtt1400/GeneralRepoBOTT/refs/heads/main/FighterFinal/'

# TODO Fighting sounds function
def regular_hit_sound():
    sound_select = random.randint(1,5)
    
    if sound_select == 1:
        playsound(git_url + 'SoundEffects/Punch1.mp3')
    elif sound_select == 2:
        playsound(git_url + 'SoundEffects/Punch2.mp3')
    elif sound_select == 3:
        playsound(git_url + 'SoundEffects/Punch3.mp3')
    elif sound_select == 4:
        playsound(git_url + 'SoundEffects/Punch4.mp3')
    elif sound_select == 5:
        playsound(git_url + 'SoundEffects/Punch2.mp3')

# TODO Critical Sounds function
def critical_hit_sound():
    sound_select = random.randint(1,5)
    
    if sound_select == 1:
        playsound(git_url + 'SoundEffects/CriticalPunch1.mp3')
    elif sound_select == 2:
        playsound(git_url + 'SoundEffects/CriticalPunch1.mp3')
    elif sound_select == 3:
        playsound(git_url + 'SoundEffects/CriticalPunch1.mp3')
    elif sound_select == 4:
        playsound(git_url + 'SoundEffects/CriticalPunch1.mp3')
    elif sound_select == 5:
        playsound(git_url + 'SoundEffects/CriticalPunch1.mp3')

# Function that creates the team for the player
def Player_names():
    player_names = list()
    for i in range(5):
        name = input('Please enter the name of your character: ')
        player_names.append(name)
    forward = input('All Fighters have been named. Press Enter to Continue!')
    return player_names


# Function that creates the team for the computer
def Computer_names():
    computer_names = list()
    total_names = list()
    names = list()
    url_read = urllib.request.urlopen(git_url + 'NamesFile.txt')
    file = url_read.read().decode('utf-8')
    print(type(file))
    file = file.replace('\n', ',')
    names = file.split(',')

    for x in names:
        total_names.append(x)
        
    total_names = list(map(str.strip, total_names))
    names_length = len(total_names)
    for i in range(5):
        i = random.randint(0, names_length)
        computer_names.append(total_names[i-1])
        total_names.pop(i-1)
        names_length = len(total_names)
        random.shuffle(total_names)
    
    return computer_names
    

# Function that has fighters face off against eachother, returns the victories fighter to the team's roster
def Battle(player_fighter, computer_fighter):
    turn_order = [player_fighter,computer_fighter]
    turn_order = sorted(turn_order)
    
    print(f'Current battle {player_fighter.name} VS {computer_fighter.name}')
    
    while turn_order[0].health > 0:
        Crit_potential = 0
        
        print(f'{turn_order[0].name} attacks {turn_order[1].name}!')
        Crit_potential = random.randint(turn_order[0].luck, 30)
        if Crit_potential <= 25:
            turn_order[1].health -= turn_order[0].strength
            regular_hit_sound()
            print(f'{turn_order[1].name} took {turn_order[0].strength} damange!')
            time.sleep(0.5)
        
        elif Crit_potential > 25:
            turn_order[1].health -= (turn_order[0].strength * 2)
            critical_hit_sound()
            print(f'{turn_order[0].name} LANDED A CRITICAL HIT!!')
            print(f'{turn_order[1].name} took {turn_order[0].strength * 2} damage!!!')
            time.sleep(0.5)
        
        if turn_order[1].health <= 0:
            break
        
        elif turn_order[1].health > 0:
            Crit_potential = 0
            Crit_potential = random.randint(turn_order[0].luck, 30)
            print(f'{turn_order[1].name} attacks {turn_order[0].name}!')
            if Crit_potential <= 25:    
                turn_order[0].health -= turn_order[1].strength
                regular_hit_sound()
                print(f'{turn_order[0].name} took {turn_order[1].strength} damage!')
                time.sleep(0.5)
            elif Crit_potential > 25:
                turn_order[0].health -= (turn_order[1].strength * 2)
                critical_hit_sound()
                print(f'{turn_order[1].name} LANDED A CRITICAL HIT!!')
                print(f'{turn_order[0].name} took {turn_order[1].strength * 2} damage!!')
                time.sleep(0.5)
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
        luck = random.randint(1, 10)
        player_team_obj.append(Fighter_stats(name, strength, health, speed, luck))
        print(player_team_obj[i])
        i += 1
        time.sleep(1)
        
    #  Generate the computer's team with their names and generate their stats
    computer_team_data = Computer_names()
    computer_team_obj = []
    
    for i in range(len(computer_team_data)):
        name = computer_team_data[i]
        strength = random.randint(3, 7)
        health = random.randint(20, 40)
        speed = random.randint(1, 5)
        luck = random.randint(1, 10)
        computer_team_obj.append(Fighter_stats(name, strength, health, speed, luck))
        print(computer_team_obj[i])
        i += 1
        time.sleep(1)
    
    # Have fighters from the 2 teams face off 1v1, edit their health stats and winner moves on
    
    player_char_count = len(player_team_obj)
    cpu_char_count = len(computer_team_obj)
    
    while player_char_count > 0 and cpu_char_count > 0:
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
            if elimination_list[i] in player_team_obj:
                player_team_obj.remove(elimination_list[i])
            elif elimination_list[i] in computer_team_obj:
                computer_team_obj.remove(elimination_list[i])
        elimination_list.clear()
        player_char_count = len(player_team_obj)
        cpu_char_count = len(computer_team_obj)
    print('Fighting loop finished')
    print(player_team_obj)
    print(computer_team_obj)

    # TODO Announce winner of the fights

    pass



if __name__ == '__main__':
    main()