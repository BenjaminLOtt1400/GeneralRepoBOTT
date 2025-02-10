import random

STARTUP_STR = 'Welcome to Rock-Paper-Scissors!'

RESULT_STR = '''You chose {player}
The computer chose: {computer}
You {results}!
'''

class User_error(Exception):
    """Custom exception to handle invalid user entry
    """    
    pass

def computer_seleciton():
    """Calls random.randint to select computer's play

    Raises:
        ValueError: Raises if random.randint returns a value outside range 1,3
                    SHOULD NEVER EXECUTE

    Returns:
        String: Returns the play of the computer based on the randint value
    """    
    selection = random.randint(1,3)
    if selection == 1:
        return 'Rock'
    elif selection == 2:
        return 'Paper'
    elif selection == 3:
        return 'Scissors'
    else:
        raise ValueError('Randint Error')
    
def Winner(user, computer):
    """Compares the values chosen by the player and the computer
    Decides the winner based on the rules of Rock Paper Scissors

    Args:
        user (str): User's entry string for their play
        computer (str): Computer's entry string for their play

    Raises:
        User_error: Raises if the user entry is anything except Rock, Paper, or Scissors

    Returns:
        String: Returns the results of the game
                Result can be Win, Lose, or Draw
    """    
    if user.title() == 'Rock':
        if computer == 'Rock':
            return 'Draw'
        elif computer == 'Paper':
            return 'Lose'
        elif computer == 'Scissors':
            return 'Win'
        
    elif user.title() == 'Paper':
        if computer == 'Rock':
            return 'Win'
        elif computer == 'Paper':
            return 'Draw'
        elif computer == 'Scissors':
            return 'Lose'

    elif user.title() == 'Scissors':
        if computer == 'Rock':
            return 'Lose'
        elif computer == 'Paper':
            return 'Win'
        elif computer == 'Scissors':
            return 'Draw'
    
    else:
        raise User_error('Invalid User Entry')

def main():
    """Primary function for the program
    Prints out STARTUP_STR string to welcome player to the game
    repeater is initialized with 'Cont' to enter while loop
    Takes user input for their play in Rock Paper Scissors
    Executes the computer_selection function to take computer's play
    Prints out the results using the RESULTS_STR string
    If any exception is Raised during the program except blocks will catch them
    Finally block asks the player if they wish to play again
    User input taken into variable repeater to either continue or exit while loop
    Program Ends when while loop is exited
    """
    
    repeater = 'Cont'
    
    print(STARTUP_STR)
    
    while repeater.lower() != 'quit':
        try:
            user_play = input('Please enter your selection - rock, paper, scissors\n')
            computer_play = computer_seleciton()
            result = Winner(user_play, computer_play)
            print(RESULT_STR.format(player=user_play, computer=computer_play, results=result))
        
        except ValueError as e:
            print(f'Error: {e}')
            
        except User_error as e:
            print(f'Error: {e}')

        finally:
            repeater = input('Enter any key to play again, or type "quit"\n')
            
        


if __name__ == '__main__':
    main()