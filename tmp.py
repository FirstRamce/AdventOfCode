# Import the random module
import random

# Initialize a dictionary to map the player's input to their corresponding move
moves = {"rock": "rock", "paper": "paper", "scissors": "scissors"}

# Initialize a variable to keep track of the player's score
score = 0

# Keep the game running until the player quits
while True:
  # Prompt the player to enter their move
  move = input("Enter your move (rock, paper, scissors, or quit): ")

  # Check if the player wants to quit
  if move == "quit":
    break

  # Get the player's move
  player_move = moves.get(move, None)

  # Check if the player entered a valid move
  if player_move is None:
    print("Invalid move, please try again.")
    continue

  # Generate a random move for the computer
  computer_move = random.choice(list(moves.values()))

  # Determine the winner of the round
  if player_move == computer_move:
    print("It's a tie!")
  elif player_move == "rock" and computer_move == "scissors":
    print("You win! Rock beats scissors.")
    score += 1
  elif player_move == "paper" and computer_move == "rock":
    print("You win! Paper beats rock.")
