import random

# Function to print the current state of the stacks
def print_stacks(stacks):
    for i, stack in enumerate(stacks, start=1):
        print(f"Stack {i}: {' '.join(['|']*stack)}")

# Function for human player's move
def player_move(stacks):
    # Ask the player to choose a stack and number of items to remove
    stack_num = int(input("Enter stack number (1, 2, or 3): "))
    num_to_remove = int(input("Enter number of items to remove: "))
    
    # Remove the specified number of items from the chosen stack
    stacks[stack_num - 1] -= num_to_remove

# Function for computer's move
def computer_move(stacks):
    # Randomly select a non-empty stack and remove a random number of items from it
    stack_num = random.randint(1, 3)
    num_to_remove = random.randint(1, stacks[stack_num - 1])
    print(f"Computer removes {num_to_remove} items from stack {stack_num}.")
    stacks[stack_num - 1] -= num_to_remove

# Function to check if a player has won
def check_winner(stacks):
    return all(stack == 0 for stack in stacks)

# Main function to play Nim against the computer
def nim_game_vs_computer():
    # Initial number of items in each stack
    stacks = [3, 4, 5]

    # Game loop
    while True:
        # Print the current state of the stacks
        print_stacks(stacks)
        # Player's move
        player_move(stacks)
        # Check if the player has won
        if check_winner(stacks):
            print("Congratulations! You win!")
            break
        # Computer's move
        computer_move(stacks)
        # Check if the computer has won
        if check_winner(stacks):
            print("Computer wins. Better luck next time!")
            break

# Start the game
nim_game_vs_computer()
