import tkinter as tk
from tkinter import messagebox
import random

# List of words to choose from
WORDS = ["PYTHON", "JAVA", "JAVASCRIPT", "TKINTER", "PROGRAMMING", "COMPUTER"]

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        self.word = random.choice(WORDS)
        self.guessed_letters = set()  #  user guessed-word store in this function
        self.remaining_attempts = 6  #total chance of attemp
        
        self.setup_ui()  # set-up enviroment
        self.update_display()  # hidding result and update the game
    
    def setup_ui(self):
        self.canvas = tk.Canvas(self.root, width=300, height=300)  # set thhe height
        self.canvas.pack(fill=tk.BOTH, expand=True) # increase the size according to the windows
        
        self.word_display = tk.Label(self.root, font=("Arial", 24))  # set the level : E.x :----- 
        self.word_display.pack(pady=20)  # set the Padding
        
        self.entry = tk.Entry(self.root, font=("Arial", 18))  # for user input
        self.entry.pack(pady=10)
        
        self.guess_button = tk.Button(self.root, text="Guess", font=("Arial", 18), command=self.make_guess) # create a button & call the (make_guess function)
        self.guess_button.pack(pady=10)
        
        self.remaining_label = tk.Label(self.root, text=f"Remaining attempts: {self.remaining_attempts}", font=("Arial", 16))  
        self.remaining_label.pack(pady=10)
        
        self.root.bind("<Return>", lambda event: self.make_guess())  # if the user press the enter during the time automattically call make-guess function call
        self.root.bind("<Configure>", self.redraw_canvas) # if the user guess the wrong size increase not overflow the screen
     
      # if the letter  will correct show the letter (---)this place show letter e.g guess letter = python  user input ('p','t') then, P-T--- 
     
    def update_display(self): 
        display_word = " ".join([letter if letter in self.guessed_letters else "_" for letter in self.word])
        self.word_display.config(text=display_word)
        self.remaining_label.config(text=f"Remaining attempts: {self.remaining_attempts}")
        self.redraw_canvas()  # user behaviour according draw and update this function using for drawaing
        
        
        if "_" not in display_word:  # cheack the - dot line if was full win the game
            messagebox.showinfo("Hangman", "Congratulations! You won!")
            self.root.quit()
        elif self.remaining_attempts == 0:
            messagebox.showinfo("Hangman", f"Game Over! The word was {self.word}")
            self.root.quit()
    
    def make_guess(self):
        guess = self.entry.get().upper()
        self.entry.delete(0, tk.END)   # if the user guuess the letter A and press the enter button clear
        
        if len(guess) != 1 or not guess.isalpha(): # check user input single or double if single no error if double print the below message
            messagebox.showwarning("Invalid Input", "Please enter a single letter.")
            return
        
        if guess in self.guessed_letters:
            messagebox.showwarning("Already Guessed", "You already guessed that letter.")
            return
        
        self.guessed_letters.add(guess)  # store guess leter
        if guess not in self.word:
            self.remaining_attempts -= 1
            self.guess_button.config(state=tk.NORMAL)#"If the user enters 'Z' and 'Z' is not  present in the word, the button will become active again so that they can make another guess."
        else:
            self.guess_button.config(state=tk.DISABLED)
        
        self.update_display()
        
         # update the drawing according the user input
    def redraw_canvas(self, event=None): #redrawing hangman game windows size change  or update
        self.canvas.delete("all")  # if game win or loss during the created a drawing refresh the drawing
        width, height = self.canvas.winfo_width(), self.canvas.winfo_height()  # heigh and width update and display
        
         # create a drawing (gallows) or ready to stand
        self.canvas.create_line(width * 0.2, height * 0.8, width * 0.8, height * 0.8, width=4)
        self.canvas.create_line(width * 0.4, height * 0.8, width * 0.4, height * 0.2, width=4)
        self.canvas.create_line(width * 0.4, height * 0.2, width * 0.7, height * 0.2, width=4)
        self.canvas.create_line(width * 0.7, height * 0.2, width * 0.7, height * 0.3, width=4)
        
        if self.remaining_attempts <= 5:
            self.canvas.create_oval(width * 0.65, height * 0.3, width * 0.75, height * 0.4, width=4)  # Head
        if self.remaining_attempts <= 4:
            self.canvas.create_line(width * 0.7, height * 0.4, width * 0.7, height * 0.6, width=4)  # Body
        if self.remaining_attempts <= 3:
            self.canvas.create_line(width * 0.7, height * 0.45, width * 0.65, height * 0.55, width=4)  # Left Arm
        if self.remaining_attempts <= 2:
            self.canvas.create_line(width * 0.7, height * 0.45, width * 0.75, height * 0.55, width=4)  # Right Arm
        if self.remaining_attempts <= 1:
            self.canvas.create_line(width * 0.7, height * 0.6, width * 0.65, height * 0.75, width=4)  # Left Leg
        if self.remaining_attempts == 0:
            self.canvas.create_line(width * 0.7, height * 0.6, width * 0.75, height * 0.75, width=4)  # Right Leg

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x500") # Set windows size
    game = HangmanGame(root) # this game or this project oobject
    root.mainloop() # start gul loop
