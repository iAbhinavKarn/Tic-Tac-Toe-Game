'''
	Project Name: Tic Tac Toe Game
	Developed By: Abhinav Karn
	Start Date:15-08-2018
	Last Edit Date: 15-08-2018
	Language Used: Python 3
'''

'''
	The basic motive of the program is to make a Tic Tac Toe game for 2 players.
	Player 1 playing with 'X' & Player 2 playing it with 'O'.
'''

from tkinter import *  # Imports all module of tkinter
from tkinter import ttk  # Imports ttk module from tkinter
import tkinter as tk  # Calls tkinter as tk
from tkinter import messagebox  # Imports messagebox module from tkinter

# Players Record
ActivePlayer = 1
player1 = []  # List to store all the places where player 1 has marked(X)
player2 = []  # List to store all the places where player 2 has marked(O)
winner = 0

# Making a new Window
window = tk.Tk()
window.title("Tic Tac Toe: Player 1(X)")  # Name the new window as Tic Tac Toe

# Making Buttons for playing the game
# Button 1
button1 = ttk.Button(window, text=" ")
button1.grid(row=0, column=0, sticky=S + N + E + W, ipadx=5,
             ipady=5)  # Sticky stick the button on a position given by directions, ipad(x,y) gives the dimension of the button
button1.config(command=lambda: ClickID(1))

# Button 2
button2 = ttk.Button(window, text=" ")
button2.grid(row=0, column=1, sticky=S + N + E + W, ipadx=5, ipady=5)
button2.config(command=lambda: ClickID(2))

# Button 3
button3 = ttk.Button(window, text=" ")
button3.grid(row=0, column=2, sticky=S + N + E + W, ipadx=5, ipady=5)
button3.config(command=lambda: ClickID(3))

# Button 4
button4 = ttk.Button(window, text=" ")
button4.grid(row=1, column=0, sticky=S + N + E + W, ipadx=5, ipady=5)
button4.config(command=lambda: ClickID(4))

# Button 5
button5 = ttk.Button(window, text=" ")
button5.grid(row=1, column=1, sticky=S + N + E + W, ipadx=5, ipady=5)
button5.config(command=lambda: ClickID(5))

# Button 6
button6 = ttk.Button(window, text=" ")
button6.grid(row=1, column=2, sticky=S + N + E + W, ipadx=5, ipady=5)
button6.config(command=lambda: ClickID(6))

# Button 7
button7 = ttk.Button(window, text=" ")
button7.grid(row=2, column=0, sticky=S + N + E + W, ipadx=5, ipady=5)
button7.config(command=lambda: ClickID(7))

# Button 8
button8 = ttk.Button(window, text=" ")
button8.grid(row=2, column=1, sticky=S + N + E + W, ipadx=5, ipady=5)
button8.config(command=lambda: ClickID(8))

# Button 9
button9 = ttk.Button(window, text=" ")
button9.grid(row=2, column=2, sticky=S + N + E + W, ipadx=5, ipady=5)
button9.config(command=lambda: ClickID(9))


# Marking on Buttons
def ClickID(id):  # Function name ClickID
    global ActivePlayer  # Calling global variable in function to use
    global player1
    global player2
    if (ActivePlayer == 1):
        player1.append(id)
        SetData(id, "X")  # Passing value to another function
        ActivePlayer = 2
        window.title("Tic Tac Toe: Player 2(0)")
    elif (ActivePlayer == 2):
        player2.append(id)
        SetData(id, "O")
        ActivePlayer = 1
        window.title("Tic Tac Toe: Player 1(X)")
    checkwinner()


# Setting Values in the Buttons X or O
def SetData(id, playerdata):
    if (id == 1):
        button1.config(text=playerdata)
        button1.state(['disabled'])  # Disabling the button state so that it may not be used twice
    elif (id == 2):
        button2.config(text=playerdata)
        button2.state(['disabled'])
    elif (id == 3):
        button3.config(text=playerdata)
        button3.state(['disabled'])
    elif (id == 4):
        button4.config(text=playerdata)
        button4.state(['disabled'])
    elif (id == 5):
        button5.config(text=playerdata)
        button5.state(['disabled'])
    elif (id == 6):
        button6.config(text=playerdata)
        button6.state(['disabled'])
    elif (id == 7):
        button7.config(text=playerdata)
        button7.state(['disabled'])
    elif (id == 8):
        button8.config(text=playerdata)
        button8.state(['disabled'])
    elif (id == 9):
        button9.config(text=playerdata)
        button9.state(['disabled'])


# Checking who is the winnner:
def checkwinner():
    global winner
    if ((1 in player1) and (2 in player1) and (3 in player1)):  # checking the value present in the list or not
        winner = 1
    elif ((1 in player2) and (2 in player2) and (3 in player2)):
        winner = 2
    elif ((4 in player1) and (5 in player1) and (6 in player1)):
        winner = 1
    elif ((4 in player2) and (5 in player2) and (6 in player2)):
        winner = 2
    elif ((7 in player1) and (8 in player1) and (9 in player1)):
        winner = 1
    elif ((7 in player2) and (8 in player2) and (9 in player2)):
        winner = 2
    elif ((1 in player1) and (4 in player1) and (7 in player1)):
        winner = 1
    elif ((1 in player2) and (4 in player2) and (7 in player2)):
        winner = 2
    elif ((2 in player2) and (5 in player2) and (8 in player2)):
        winner = 2
    elif ((2 in player1) and (5 in player1) and (8 in player1)):
        winner = 1
    elif ((3 in player2) and (6 in player2) and (9 in player2)):
        winner = 2
    elif ((3 in player1) and (6 in player1) and (9 in player1)):
        winner = 1
    elif ((1 in player2) and (5 in player2) and (9 in player2)):
        winner = 2
    elif ((1 in player1) and (5 in player1) and (9 in player1)):
        winner = 1
    elif ((3 in player2) and (5 in player2) and (7 in player2)):
        winner = 2
    elif ((3 in player1) and (5 in player1) and (7 in player1)):
        winner = 1

    # Checking Winner and Showing a Dialoge Box
    if (winner == 1):
        messagebox.showinfo('Winner', 'Player 1 is the winner')
    elif (winner == 2):
        messagebox.showinfo('Winner', 'Player 2 is the winner')


window.mainloop()
