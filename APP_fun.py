# Créé par luidjy, le 15/09/2021 en Python 3.7
import tkinter, sys
from tkinter import *
import webbrowser

#Paramètre de la fenêtre
PasswordG = tkinter.Tk()
PasswordG.title("APP BETA")
PasswordG.minsize(480, 360)
PasswordG.geometry("480x360")
#PasswordG.iconbitmap("favicon.ico")

def writeT():
        res = input1.get()
        n = len(res)
        print(n)
        if n >= 12:
            l1 = Label(frameM, text="Votre mot de passe est assez long !", font=('consolas, 15'),bg="lime")
            l1.pack()
        else:
            l2 = Label(frameM, text="Votre mot de passe est trop court !", font=('consolas, 15'),bg="red")
            l2.pack()
        #l1 = Label(frameM, text="Votre Mot de passe : "+res, font=('consolas', 15))
        #l1.pack()

        input1.pack_forget()
        bouton1.pack_forget()



frameM = Frame(PasswordG, bd=1, relief=SUNKEN)
input1 = Entry(frameM, font=('consolas', 15))
input1.pack()
bouton1 = Button(frameM,text="Vérifier", font=('consolas', 15), command=(writeT))
bouton1.pack()



frameM.pack()
PasswordG.mainloop()