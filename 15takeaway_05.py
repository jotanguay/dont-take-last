import random
from enum import Enum

def trim(s: str) -> str:
    return s.strip()


def lower(s: str) -> str:
    return s.lower()


class TurnOrder(Enum):
    PLAYER_FIRST = 1
    PLAYER_SECOND = 2


#Function 1
def prompt_turn_order():
    while True: #when it is prompted
        print("Do you want to go first or second?")
        print("  1) First (you start)")
        print("  2) Second (CPU starts)")
        line = input("Choice: ")
        line = lower(trim(line)) #Prevents an extra line from being created to help keep input consistent.

        if line in {"1", "first", "FIRST", "First"}: #I think people are most likely to spell First and Second these ways if they will spell it out
            return TurnOrder.PLAYER_FIRST

        if line in {"2", "second", "SECOND", "Second"}:
            return TurnOrder.PLAYER_SECOND

        print("Invalid choice. Enter 1 or 2.\n") #Restarts the loop so they are prompted again if it did not exit the function on either "if".



#Function 2
def prompt_pile_size():
    while True:
        print("How many items should the pile start with?")
        pile_size = prompt_int()
            
        return pile_size
        

#Function 3
def prompt_take_limit(pile_size: int):
    while True:
        print("Up to how many items can you take from the pile at a time?")

        take_limit = prompt_int() #Function 4
            
        if take_limit < 2 or take_limit > 9: #Make sure it is not too large
            print("Please pick a number between 2 and 9.")
            continue
            
        if take_limit > pile_size: #Makes sure the game takes at least one full turn.
            print("Please choose a smaller number.")
            continue
            
        return take_limit
        
        
#Function 4
def prompt_int():
    while True:
        player_input = trim(input("Choice: "))
        
        try:
            player_int = int(player_input)
        except ValueError:
            print("Please enter a whole number.")
            continue
        
        if player_int < 1:
            print("Please enter a positive number.")
            continue
        return player_int

        

def main():
    random.seed() #random selections seed when main is run

    players_choice = 0 #the number of items the player is taking
    computers_choice = 0 #the number of items the computer is taking
    items_left = 15 #the number of items left in the main pile

    print()
    print("In this game, you win if you get me to pick the last item in the pile.")
    print("You lose if you pick the last item in the pile.")
    
    items_left = prompt_pile_size() #Function 2
    
    print()
    print(f"The pile will start with {items_left} items.")
    
    take_limit = prompt_take_limit(items_left) #Function 3
    
    print(f"On your turn, you can take up to {take_limit} items from the pile.")
    print("We'll keep playing until someone wins!")
    print("Remember, the person to take the last item from the pile loses!")





    order = prompt_turn_order() #Function 1



    if order == TurnOrder.PLAYER_FIRST: #specific starting instructions if player goes first
        print("You chose to go first")
        print("Let's play! \n")

        print(f"There are {items_left} items in the pile. How many would you like to take?")
        players_choice = int(input()) #player picks the first amount of items from the pile

        while players_choice > take_limit or players_choice < 1:
            print(f"Please pick a number between 1 and {take_limit}.")
            players_choice = int(input()) #Makes sure the player picks the proper number of items

        items_left -= players_choice #Takes away the player's choice from the pile
        
        print(f"You took {players_choice} items. \n")
        
        
        
    else: #Starting instructions for if player decides to go second.
        print("You chose to go second")
        print("Let's play!")

    while items_left > 0: #What you can do with 6 or fewer items if more limited
       #This continues this loop of code (the "normal" portion of the game)
        print(f"There are {items_left} items in the pile.\n")
        
        computers_choice = random.randint(1,min(take_limit, items_left)) #selects a random number 1-3 (for easy mode)
        print(f"I will take {computers_choice} items. \n")
        
        
        items_left -= computers_choice #removes the items from the pile
        #If items_left = 0, then the while loop will end, ending the game.
        
        if items_left == 0:
            print("Looks like I took the last item.\n You win!")
            return #ends the game
        
        print(f"There are {items_left} items in the pile.")

        print("How many items do you want to take?")
        players_choice = int(input()) #Prompts the player to choose

        while players_choice > min(take_limit, items_left) or players_choice < 1:
            print("You cannot take that many items. Try another number.")
            players_choice = int(input()) #prevents the player from picking too many or too few items form the pile, and reprompts them

        
        items_left -= players_choice #removes the player's choice from the pile
        
        
    print("Looks like you took the last item. I win!")
        
        
    
        
        



if __name__ == "__main__":
    main()
