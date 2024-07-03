import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock, Paper, Scissors")
        self.root.geometry("500x400")
        self.root.resizable(False, False)
        
        self.player_score = 0
        self.computer_score = 0
        
        self.create_widgets()
        
    def create_widgets(self):
        title_label = tk.Label(self.root, text="Rock, Paper, Scissors", font=("Helvetica", 24, "bold"))
        title_label.pack(pady=20)
        
        self.score_label = tk.Label(self.root, text=f"Player: {self.player_score}  Computer: {self.computer_score}", font=("Helvetica", 16))
        self.score_label.pack(pady=10)
        
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=20)
        
        self.rock_button = tk.Button(button_frame, text="Rock", font=("Helvetica", 14), width=10, command=lambda: self.determine_winner("Rock"))
        self.rock_button.grid(row=0, column=0, padx=10)
        
        self.paper_button = tk.Button(button_frame, text="Paper", font=("Helvetica", 14), width=10, command=lambda: self.determine_winner("Paper"))
        self.paper_button.grid(row=0, column=1, padx=10)
        
        self.scissors_button = tk.Button(button_frame, text="Scissors", font=("Helvetica", 14), width=10, command=lambda: self.determine_winner("Scissors"))
        self.scissors_button.grid(row=0, column=2, padx=10)
        
        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 14))
        self.result_label.pack(pady=20)
        
        self.reset_button = tk.Button(self.root, text="Reset", font=("Helvetica", 14), command=self.reset_game)
        self.reset_button.pack(pady=10)
        
    def determine_winner(self, player_choice):
        choices = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(choices)
        
        result_text = f"Computer chose: {computer_choice}\n"
        
        if player_choice == computer_choice:
            result_text += "It's a tie!"
        elif (player_choice == "Rock" and computer_choice == "Scissors") or \
             (player_choice == "Paper" and computer_choice == "Rock") or \
             (player_choice == "Scissors" and computer_choice == "Paper"):
            result_text += "You win!"
            self.player_score += 1
        else:
            result_text += "You lose!"
            self.computer_score += 1
            
        self.result_label.config(text=result_text)
        self.score_label.config(text=f"Player: {self.player_score}  Computer: {self.computer_score}")
    
    def reset_game(self):
        self.player_score = 0
        self.computer_score = 0
        self.result_label.config(text="")
        self.score_label.config(text=f"Player: {self.player_score}  Computer: {self.computer_score}")

# Create the main application window
root = tk.Tk()
game = RockPaperScissorsGame(root)

# Run the application
root.mainloop()
