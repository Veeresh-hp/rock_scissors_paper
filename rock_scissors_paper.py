import os
from tkinter import *
from PIL import Image, ImageTk
from random import randint

# Initialize main window
root = Tk()
root.title("Rock Scissors Paper")
root.configure(background="#34495E")
root.geometry("600x500")
root.resizable(False, False)

# Get correct image path
IMG_DIR = os.path.join(os.path.dirname(__file__), "images")

# Load images
rock_img = ImageTk.PhotoImage(Image.open(os.path.join(IMG_DIR, "rock-user.png")))
paper_img = ImageTk.PhotoImage(Image.open(os.path.join(IMG_DIR, "paper-user.png")))
scissor_img = ImageTk.PhotoImage(Image.open(os.path.join(IMG_DIR, "scissors-user.png")))
rock_img_comp = ImageTk.PhotoImage(Image.open(os.path.join(IMG_DIR, "rock.png")))
paper_img_comp = ImageTk.PhotoImage(Image.open(os.path.join(IMG_DIR, "paper.png")))
scissor_img_comp = ImageTk.PhotoImage(Image.open(os.path.join(IMG_DIR, "scissors.png")))

# Choices
choices = ["rock", "paper", "scissor"]

# Score Variables
user_score = 0
computer_score = 0
round_counter = 0
max_rounds = 20

# UI Components
Label(root, text="ROCK PAPER SCISSORS", font=("Arial", 18, "bold"), bg="#34495E", fg="white").pack(pady=10)

frame = Frame(root, bg="#34495E")
frame.pack()

comp_label = Label(frame, image=scissor_img_comp, bg="#34495E")
user_label = Label(frame, image=scissor_img, bg="#34495E")
comp_label.grid(row=0, column=0, padx=40)
user_label.grid(row=0, column=2, padx=40)

playerScore = Label(frame, text=user_score, font=("Arial", 20, "bold"), bg="#34495E", fg="white")
computerScore = Label(frame, text=computer_score, font=("Arial", 20, "bold"), bg="#34495E", fg="white")
playerScore.grid(row=1, column=2, pady=10)
computerScore.grid(row=1, column=0, pady=10)

comp_indicator = Label(frame, text="COMPUTER", font=("Arial", 14, "bold"), bg="#34495E", fg="white")
user_indicator = Label(frame, text="USER", font=("Arial", 14, "bold"), bg="#34495E", fg="white")
comp_indicator.grid(row=2, column=0, pady=5)
user_indicator.grid(row=2, column=2, pady=5)

msg = Label(root, text="Make your choice!", font=("Arial", 14, "bold"), bg="#34495E", fg="white")
msg.pack(pady=10)

round_label = Label(root, text="Rounds Played: 0", font=("Arial", 12, "bold"), bg="#34495E", fg="white")
round_label.pack()

# Game Logic
def updateMessage(x):
    msg["text"] = x

def updateUserScore():
    global user_score
    user_score += 1
    playerScore.config(text=str(user_score))

def updateCompScore():
    global computer_score
    computer_score += 1
    computerScore.config(text=str(computer_score))

def checkWin(player, computer):
    if player == computer:
        updateMessage("It's a tie!")
    elif (player == "rock" and computer == "scissor") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissor" and computer == "paper"):
        updateMessage("You win!")
        updateUserScore()
    else:
        updateMessage("You lose!")
        updateCompScore()

def disableButtons():
    """Disable choice buttons when max rounds are reached."""
    rock.config(state=DISABLED)
    paper.config(state=DISABLED)
    scissor.config(state=DISABLED)

def checkFinalWinner():
    """Check if 20 rounds are reached and announce the winner."""
    if round_counter >= max_rounds:
        disableButtons()
        if user_score > computer_score:
            updateMessage("Game Over! You are the Winner! 🎉")
        elif user_score < computer_score:
            updateMessage("Game Over! Computer Wins! 🤖")
        else:
            updateMessage("Game Over! It's a Tie! 😐")

def updateChoice(x):
    global round_counter
    if round_counter >= max_rounds:
        return
    
    compChoice = choices[randint(0, 2)]
    
    comp_label.configure(image=rock_img_comp if compChoice == "rock" else paper_img_comp if compChoice == "paper" else scissor_img_comp)
    user_label.configure(image=rock_img if x == "rock" else paper_img if x == "paper" else scissor_img)
    
    checkWin(x, compChoice)
    
    round_counter += 1
    round_label.config(text=f"Rounds Played: {round_counter}")

    checkFinalWinner()

# Buttons
btn_frame = Frame(root, bg="#34495E")
btn_frame.pack(pady=10)

rock = Button(btn_frame, text="ROCK", font=("Arial", 12, "bold"), width=10, bg="#E74C3C", fg="white", command=lambda: updateChoice("rock"))
paper = Button(btn_frame, text="PAPER", font=("Arial", 12, "bold"), width=10, bg="#F1C40F", fg="white", command=lambda: updateChoice("paper"))
scissor = Button(btn_frame, text="SCISSOR", font=("Arial", 12, "bold"), width=10, bg="#3498DB", fg="white", command=lambda: updateChoice("scissor"))

rock.grid(row=0, column=0, padx=10)
paper.grid(row=0, column=1, padx=10)
scissor.grid(row=0, column=2, padx=10)

def reset_game():
    global user_score, computer_score, round_counter
    user_score, computer_score, round_counter = 0, 0, 0
    playerScore.config(text="0")
    computerScore.config(text="0")
    round_label.config(text="Rounds Played: 0")
    user_label.configure(image=scissor_img)
    comp_label.configure(image=scissor_img_comp)
    updateMessage("Make your choice!")

    # Enable buttons again
    rock.config(state=NORMAL)
    paper.config(state=NORMAL)
    scissor.config(state=NORMAL)

reset_button = Button(root, text="Reset Game", font=("Arial", 12, "bold"), bg="#2ECC71", fg="white", command=reset_game)
reset_button.pack(pady=10)

root.mainloop()
