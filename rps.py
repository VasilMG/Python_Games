from tkinter import *
from random import *
import time


root = Tk()
root.title("RPS Game")

root.geometry("1200x700",)

rock = PhotoImage(file="path to the picture")
paper = PhotoImage(file="path to the picture")
scissors = PhotoImage(file="path to the picture")
small_rock = PhotoImage(file="path to the picture")
small_paper = PhotoImage(file="path to the picture")
small_scissors = PhotoImage(file="path to the picture")

user_choice = 0

def on_click(button):
    global user_choice
    new_laber = Label(root, text="", bg="Purple", font=("Calibri", 18))
    new_laber.pack(pady=30)
    new_laber.place(x=800, y=500)
    if button == "Rock":
        user_choice = 0
        new_laber.config(text="You picked Rock!     ")

    elif button == "Paper":
        user_choice = 1
        new_laber.config(text="You picked Paper!   ")


    elif button == "Scissors":
        user_choice = 2
        new_laber.config(text="You picked Scissors!")

def play(user_pick):
    pc_pick = randint(0,2)
    time.sleep(0.5)
    image_label.config(image=image_list[pc_pick])
    if user_pick == 0:
        if pc_pick == 0:
            win_lose_lagel.config(text="It is a tie!", bg="Purple")
        elif pc_pick == 1:
            win_lose_lagel.config(text="Paper covers Rock. You lose!", bg="Red")
        elif pc_pick == 2:
            win_lose_lagel.config(text="Rock breaks Scissors. You Win!", bg="Green")

    if user_pick == 1:
        if pc_pick == 0:
            win_lose_lagel.config(text="Paper covers Rock. You WIN!", bg="Green")
        elif pc_pick == 1:
            win_lose_lagel.config(text="It is a tie!", bg="Purple")
        elif pc_pick == 2:
            win_lose_lagel.config(text="Scissors cuts Paper! You lose!", bg="Red")

    if user_pick == 2:
        if pc_pick == 0:
            win_lose_lagel.config(text="Rock breaks Scissors. You lose!", bg="Red")
        elif pc_pick == 1:
            win_lose_lagel.config(text="Scissors cuts Paper! You win!", bg="Green")
        elif pc_pick == 2:
            win_lose_lagel.config(text="It is a tie!", bg="Purple")


image_list = [rock, paper, scissors]
pc_pick = randint(0,2)
button_list = [small_rock, small_paper, small_scissors]

image_label = Label(root, image=image_list[pc_pick])
image_label.pack(pady=20)


lower_text = Label(root, text="Pick Something", font=("Arial", 15), bg="Purple",)
lower_text.pack()
lower_text.place(x=550, y=500)


rock_button = Button(root, image=button_list[0], command=lambda:on_click("Rock"))
rock_button.pack()
rock_button.place(x=280, y=350)

paper_button = Button(root, image=button_list[1], command=lambda:on_click("Paper"))
paper_button.pack()
paper_button.place(x=560, y=350)

scissors_button = Button(root, image=button_list[2], command=lambda:on_click("Scissors"))
scissors_button.pack()
scissors_button.place(x=820, y=350)

play_button =Button(root, text="Play", height=5, width=20, command=lambda : play(user_choice))
play_button.pack()
play_button.place(x= 300, y=500)

win_lose_lagel = Label(root, text="", font=("Calibri",18), bg="Purple")
win_lose_lagel.pack(pady=300)
win_lose_lagel.place(x= 600, y= 300)

root.config(bg="Purple")

root.mainloop()