import tkinter, sys
from tkinter import *
import webbrowser

#Paramètre de la fenêtre
PasswordG = tkinter.Tk()
PasswordG.title("Portfolio")
PasswordG.minsize(480, 360)
PasswordG.geometry("480x360")
PasswordG.iconbitmap("favicon.ico")
PasswordG.config(background='black')


frameT = Frame(PasswordG, bg='black')
frameC = Frame(PasswordG, bg='black')
#création d'un label  l'argument bg='red' met un cadre autour du label
l1 = Label(frameT, text="Portfolio", font=('consolas', 25), bg='black', fg='white')
l2 = Label(frameC, text="© luidjy Aubel", font=('consolas', 10), bg='black', fg='white')
#importation sur la page de l'application side=LEFT pady=200
l1.pack() #expand=YES
frameT.pack(expand=YES)
l2.pack() #side=BOTTOM
frameC.pack(side=BOTTOM)
def open():
    webbrowser.open_new('https://portfolioluidjyaubel.000webhostapp.com/')

def close():
    quit()

#botton
b1 = Button(text='Portfolio !',font=('consolas', 10), bg='red', fg='white', command=(open))
b1.pack()
b2 = Button(text='close', command=(close))
b2.pack(pady=100)

PasswordG.mainloop()