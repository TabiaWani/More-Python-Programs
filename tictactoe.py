import tkinter as tk
from tkinter import messagebox

# Initialize game variables
board = [""] * 9
current_player = "X"

# Function to handle button clicks
def button_click(index):
    global current_player

    if board[index] == "":
        board[index] = current_player
        buttons[index].config(text=current_player)

        if check_winner():
            messagebox.showinfo("Game Over", f"Player {current_player} wins!")
            reset_game()
        elif "" not in board:
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_game()
        else:
            current_player = "O" if current_player == "X" else "X"

# Function to check for a winner
def check_winner():
    win_patterns = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for pattern in win_patterns:
        if board[pattern[0]] == board[pattern[1]] == board[pattern[2]] and board[pattern[0]] != "":
            return True
    return False

# Function to reset the game
def reset_game():
    global board, current_player
    board = [""] * 9
    current_player = "X"
    for button in buttons:
        button.config(text="")

# Create the main window
window = tk.Tk()
window.title("Tic Tac Toe")

# Create the buttons for the game board
buttons = []
for i in range(9):
    button = tk.Button(window, text="", font=("Arial", 24), width=5, height=2,
                       command=lambda i=i: button_click(i))
    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)

# Start the main event loop
window.mainloop()
