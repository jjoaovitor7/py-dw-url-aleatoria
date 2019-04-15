from tkinter import *
import random

janela = Tk()
janela.title("Deep Web Link Aleatório")
janela.geometry("300x150")
janela.configure(bg="black")

titulo =  Label(janela, text="Deep Web Link Aleatório", font=("Comic Sans MS", "10", "bold", "italic"))
titulo.grid(column=0, row=0)
titulo.configure(bg="black", fg ="#00ff00")

sitesDW = ["Facebook - https://www.facebookcorewwwi.onion/", ]
siteDW = random.choice(sitesDW)

janela.mainloop()
