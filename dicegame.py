import random

def roll():
    return random.randint(1, 6)

# Get the number of players between 2 and 4
while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid input, please try again.")

max_score = 50
player_scores = [0 for _ in range(players)]  # Initialize scores for all players
game_over = False  # Flag to track if the game should end

# Main game loop
while not game_over:
    for player_idx in range(players):
        print(f"\nPlayer number {player_idx + 1}'s turn has just started!\n")
        print(f"Your total score is: {player_scores[player_idx]}\n")
        current_score = 0  # Reset current turn score

        # Player's turn loop
        while True:
            should_roll = input("Would you like to roll (y/n)? ").lower()
            if should_roll == 'n':
                break  # Player chooses to pass the turn
            elif should_roll == 'y':
                value = roll()  # Roll the dice
                if value == 1:
                    print("You rolled a 1! Turn done!")
                    # Add current turn score to player's total score before resetting
                    player_scores[player_idx] += current_score
                    current_score = 0  # Reset current turn score
                    break  # End the player's turn
                else:
                    current_score += value  # Add rolled value to current score
                    print(f"You rolled a: {value}")
                print(f"Your score for this turn is: {current_score}")
            else:
                print("Invalid input, please enter 'y' to roll or 'n' to pass.")

        # Add current turn score to player's total score if not rolled a 1
        if current_score > 0:
            player_scores[player_idx] += current_score
        
        print(f"Your total score is now: {player_scores[player_idx]}")

        # Check if the player has won
        if player_scores[player_idx] >= max_score:
            print(f"\nPlayer number {player_idx + 1} is the winner with a score of: {player_scores[player_idx]}")
            game_over = True  # End the game
            break  # Break out of the player's turn loop

    # Break out of the main game loop if game_over is True
    if game_over:
        break


