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


        

def main():
    random.seed() #random selections seed when main is run

    players_choice = 0 #the number of items the player is taking
    computers_choice = 0 #the number of items the computer is taking
    items_left = 15 #the number of items left in the main pile

    print()
    print("In this game, you win if you get me to pick the last item in the pile.")
    print("You lose if you pick the last item in the pile.")
    print("On your turn, you can take 1, 2, or 3 items from the pile.")
    print("We'll keep playing until someone wins!")



    order = prompt_turn_order() #Function 1



    if order == TurnOrder.PLAYER_FIRST: #specific starting instructions if player goes first
        print("You chose to go first")
        print("Let's play! \n")

        print(f"There are {items_left} items in the pile. How many would you like to take?")
        players_choice = int(input()) #player picks the first amount of items from the pile

        while players_choice > 3 or players_choice < 1:
            print("Please pick a number between 1 and 3")
            players_choice = int(input()) #Makes sure the player picks the proper number of items

        items_left -= players_choice #Takes away the player's choice from the pile
        
        print(f"You took {players_choice} items. \n")
        
    else: #Starting instructions for if player decides to go second.
        print("You chose to go second")
        print("Let's play!")

    while items_left > 0: #What you can do with 6 or fewer items if more limited
       #This continues this loop of code (the "normal" portion of the game)
        print(f"There are {items_left} items in the pile.\n")
        
        computers_choice = random.randint(1,min(3, items_left)) #selects a random number 1-3 (for easy mode)
        print(f"I will take {computers_choice} items. \n")
        
        
        items_left -= computers_choice #removes the items from the pile
        #If items_left = 0, then the while loop will end, ending the game.
        
        if items_left == 0:
            print("Looks like I took the last item.\n You win!")
            return #ends the game
        
        print(f"There are {items_left} items in the pile.")

        print("How many items do you want to take?")
        players_choice = int(input()) #Prompts the player to choose

        while players_choice > min(3, items_left) or players_choice < 1:
            print("You cannot take that many items. Try another number.")
            players_choice = int(input()) #prevents the player from picking too many or too few items form the pile, and reprompts them

        
        items_left -= players_choice #removes the player's choice from the pile
        
        
    print("Looks like you took the last item. I win!")
        
        
    
        
        



if __name__ == "__main__":
    main()
