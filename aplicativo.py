from tkinter import *
import random

janela = Tk()
janela.title("Deep Web Link Aleatório")
janela.geometry("300x150")
janela.configure(bg="black")

sitesDW = ["Facebook - https://www.facebookcorewwwi.onion/", ]
siteDW = random.choice(sitesDW)

janela.mainloop()
