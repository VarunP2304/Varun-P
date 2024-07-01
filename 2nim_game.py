import random

# Function to print the current state of the stacks
def print_stacks(stacks):
    for i, stack in enumerate(stacks, start=1):
        print(f"Stack {i}: {'|' * stack}")

# Function for human player's move
def player_move(stacks):
    stack_num = int(input("Enter stack number (1-3): ")) - 1  # Choose stack number
    num_to_remove = int(input("Enter number of items to remove: "))  # Choose number of items to remove
    stacks[stack_num] -= num_to_remove  # Remove items from chosen stack

# Function for computer's move
def computer_move(stacks):
    stack_num = random.choice([i for i, stack in enumerate(stacks) if stack > 0])  # Select a non-empty stack
    num_to_remove = random.randint(1, stacks[stack_num])  # Random number of items to remove
    print(f"Computer removes {num_to_remove} items from stack {stack_num + 1}.")
    stacks[stack_num] -= num_to_remove  # Remove items from chosen stack

# Function to check if a player has won
def check_winner(stacks):
    return all(stack == 0 for stack in stacks)  # Check if all stacks are empty

# Main function to play Nim against the computer
def nim_game_vs_computer():
    stacks = [3, 4, 5]  # Initial number of items in each stack
    while True:
        print_stacks(stacks)  # Print current state of the stacks
        player_move(stacks)  # Player's move
        if check_winner(stacks):  # Check if player has won
            print("Congratulations! You win!")
            break
        computer_move(stacks)  # Computer's move
        if check_winner(stacks):  # Check if computer has won
            print("Computer wins. Better luck next time!")
            break

# Start the game
nim_game_vs_computer()
