import random
import tkinter as tk

def generate_computer_choice():
    """Randomly select a choice for the computer."""
    options = ['rock', 'paper', 'scissors']
    return random.choice(options)

def evaluate_winner(player_choice, ai_choice):
    """Evaluate the winner based on player and AI choices."""
    if player_choice == ai_choice:
        return "It's a draw!"
    elif (player_choice == 'rock' and ai_choice == 'scissors') or \
         (player_choice == 'scissors' and ai_choice == 'paper') or \
         (player_choice == 'paper' and ai_choice == 'rock'):
        return "Congratulations, you win!"
    else:
        return "Sorry, you lost!"

def play(choice):
    """Handle the player's choice and update the game state."""
    ai_choice = generate_computer_choice()
    outcome = evaluate_winner(choice, ai_choice)
    
    # Update the score
    if outcome == "Congratulations, you win!":
        global player_score
        player_score += 1
    elif outcome == "Sorry, you lost!":
        global ai_score
        ai_score += 1

    # Update score labels
    player_score_label.config(text=f"You: {player_score}")
    ai_score_label.config(text=f"AI: {ai_score}")

    # Update the notification label
    notification_label.config(text=f"AI chose: {ai_choice} - {outcome}")

def reset_game():
    """Reset the scores."""
    global player_score, ai_score
    player_score = 0
    ai_score = 0
    player_score_label.config(text=f"You: {player_score}")
    ai_score_label.config(text=f"AI: {ai_score}")
    notification_label.config(text="Scores have been reset!")

# Initialize scores
player_score = 0
ai_score = 0

# Create the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("300x400")
root.configure(bg="#f0f0f0")

# Create a title label
title_label = tk.Label(root, text="Rock-Paper-Scissors", font=("Helvetica", 16), bg="#f0f0f0")
title_label.pack(pady=10)

# Create score labels
player_score_label = tk.Label(root, text=f"You: {player_score}", font=("Helvetica", 14), bg="#f0f0f0")
player_score_label.pack(pady=5)

ai_score_label = tk.Label(root, text=f"AI: {ai_score}", font=("Helvetica", 14), bg="#f0f0f0")
ai_score_label.pack(pady=5)

# Create a notification label
notification_label = tk.Label(root, text="", font=("Helvetica", 12), bg="#f0f0f0", wraplength=250)
notification_label.pack(pady=10)

# Create buttons for player choices
rock_button = tk.Button(root, text="Rock", command=lambda: play('rock'), bg="#4CAF50", fg="white", font=("Helvetica", 12))
paper_button = tk.Button(root, text="Paper", command=lambda: play('paper'), bg="#2196F3", fg="white", font=("Helvetica", 12))
scissors_button = tk.Button(root, text="Scissors", command=lambda: play('scissors'), bg="#FF9800", fg="white", font=("Helvetica", 12))
reset_button = tk.Button(root, text="Reset Scores", command=reset_game, bg="#f44336", fg="white", font=("Helvetica", 12))

# Arrange buttons in the window
rock_button.pack(pady=5)
paper_button.pack(pady=5)
scissors_button.pack(pady=5)
reset_button.pack(pady=10)

# Start the GUI event loop
root.mainloop()
