from tkinter import *
import random

janela = Tk()
janela.title("Deep Web Link Aleatório")
janela.geometry("350x100")
janela.configure(bg="black")

titulo = Label(janela, text="Deep Web Link Aleatório", font=("Comic Sans MS", "10", "bold", "italic"))
titulo.grid(column=0, row=0, sticky=W)
titulo.configure(bg="black", fg="#00ff00")

url = Label(janela, text="URL", font=("Comic Sans MS", "9"))
url.grid(column=0, row=2)
url.configure(bg="black", fg ="#00ff00")

def clicado():
        sitesDW = ["Facebook - https://www.facebookcorewwwi.onion", "notEvil - https://hss3uro2hsxfogfq.onion"]
        siteDW = random.choice(sitesDW)
        url.configure(text=siteDW)
        
siteBotao = Button(janela, text = "Go!", command=clicado)
siteBotao.grid(column=0, row=4)
siteBotao.configure(bg="black", fg="#00ff00")

janela.mainloop()
