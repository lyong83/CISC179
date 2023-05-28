from tkinter import *
import random

class Module4Class:
    def __init__(self):
        pass

    def execute(self):
        # Define global variables
        options = ['rock', 'paper', 'scissors']
        player_score = 0
        computer_score = 0

        # Define all functions
        def clicked(option):
            nonlocal player_score, computer_score
            computer_choice = random.choice(options)

            if option == 'rock':
                if computer_choice == 'rock':
                    result = ""
                elif computer_choice == 'paper':
                    result = ""
                    computer_score += 1
                else:
                    result = ""
                    player_score += 1
            elif option == 'paper':
                if computer_choice == 'rock':
                    result = ""
                    player_score += 1
                elif computer_choice == 'paper':
                    result = ""
                else:
                    result = ""
                    computer_score += 1
            else:
                if computer_choice == 'rock':
                    result = ""
                    computer_score += 1
                elif computer_choice == 'paper':
                    result = ""
                    player_score += 1
                else:
                    result = ""

            # Update the labels
            player_choice_label.config(text="Your choice: " + option)
            computer_choice_label.config(text="My choice: " + computer_choice)
            player_score_label.config(text="Your score: " + str(player_score))
            computer_score_label.config(text="Computer score: " + str(computer_score))

        # Create window
        window = Tk()
        window.title("Rock, Paper, Scissors - A Game for All!")
        window.geometry("400x300")

        # Create main frame and set background color to yellow
        top_frame = Frame(window)
        top_frame.pack()
        main_frame = Frame(window, bg="yellow")
        main_frame.pack(fill=BOTH, expand=True)

        # Create widgets
        rock_button = Button(top_frame, text="Rock", command=lambda: clicked('rock'))
        paper_button = Button(top_frame, text="Paper", command=lambda: clicked('paper'))
        scissors_button = Button(top_frame, text="Scissors", command=lambda: clicked('scissors'))
        empty_label = Label(main_frame, text="", bg="yellow", height=2)
        player_choice_label = Label(main_frame, text="Your choice:", bg="yellow", width=23,
                                    font=("Times New Roman", 22, "bold"))
        computer_choice_label = Label(main_frame, text="My choice:", bg="yellow",
                                        font=("Times New Roman", 22, "bold"))
        player_score_label = Label(main_frame, text="Your score:", bg="yellow",
                                    font=("Times New Roman", 22, "bold"))
        computer_score_label = Label(main_frame, text="Computer score:", bg="yellow",
                                        font=("Times New Roman", 22, "bold"))
        result_label = Label(main_frame, text="")

        # Place widgets into main_frame using a grid layout
        rock_button.grid(row=1, column=0, padx=30)
        paper_button.grid(row=1, column=1, padx=30)
        scissors_button.grid(row=1, column=2, padx=30)
        empty_label.grid(row=2, column=0)
        player_choice_label.grid(row=3, column=1)
        computer_choice_label.grid(row=4, column=1)
        player_score_label.grid(row=5, column=1)
        computer_score_label.grid(row=6, column=1)

        # Open window
        window.mainloop()
