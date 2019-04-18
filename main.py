from tkinter import *
import random
from mostrarURLs import *

janela = Tk()
janela.title("Deep Web Link Aleatório")
janela.geometry("280x100")
janela.configure(bg="black")

fonte1 = ("Comic Sans MS", "10")

menubar = Menu(janela)
janela.config(menu=menubar)
opcaomenu1 = Menu(menubar)
menubar.add_cascade(label='Temas', menu=opcaomenu1)

def ajudaNavegadores():

    janelaNavegadores = Tk()
    janelaNavegadores.title('Navegadores')

    redeOnion = Label(janelaNavegadores, text="Rede onion: https://www.torproject.org/download/", font=fonte1)
    redeI2P = Label(janelaNavegadores, text="Rede i2p: https://geti2p.net/pt-br/download", font=fonte1)

    redeOnion.grid(column=0, row=0)
    redeI2P.grid(column=0, row=1)
    
opcaomenu2 = Menu(menubar)
menubar.add_cascade(label='Ajuda', menu=opcaomenu2)
opcaomenu2.add_command(label='URLs', command=mostrarURLs)
opcaomenu2.add_command(label='Navegadores', command=ajudaNavegadores)

titulo = Label(janela, text="Deep Web Link Aleatório", font=("Comic Sans MS", "10", "bold"))
titulo.grid(column=0, row=0, sticky=W)
titulo.configure(bg="black", fg="#00ff00")

url = Label(janela, text="URL", font=fonte1)
url.grid(column=0, row=2)
url.configure(bg="black", fg ="#00ff00")

def botaoGoClicado():
         
        sitesDW = ["Facebook - facebookcorewwwi.onion", "notEvil - hss3uro2hsxfogfq.onion", "The Chess - theches3nacocgsc.onion", 
                   "Internet Archive - archivecrfip2lpi.onion", "DuckDuckGo - 3g2upl4pq6kufc4m.onion", "TorPaste - 5y5ek6tlzttcxgvlknf5mxybbsntfqsq2q2fngdbfmskgghukfkn5uqd.onion", 
                   "Bible4u - bible4u2kjgjvbxs.onion/", "Torch - xmh57jrzrnw6insl.onion", "Enot - enotegggr635n4lw.onion", 
                   "Example Rendezvous Points Page - duskgytldkxiuqc6.onion", "Web Shell Archive - z2huz7tsxluvnxoc.onion"]
        siteDW = random.choice(sitesDW)
        url.configure(text=siteDW)
        
siteBotao = Button(janela, text="Go!", command=botaoGoClicado)
siteBotao.grid(column=0, row=4)
siteBotao.configure(bg="black", fg="#00ff00")

def TemaBranco():
         
        janela.configure(bg="white")
        titulo.configure(bg="white", fg="black")
        url.configure(bg="white", fg="black")
        siteBotao.configure(bg="white", fg="black")

def TemaPreto():
         
        janela.configure(bg="black")
        titulo.configure(bg="black", fg="#00ff00")
        url.configure(bg="black", fg="#00ff00")
        siteBotao.configure(bg="black", fg="#00ff00")

opcaomenu1.add_command(label='Tema Branco', command=TemaBranco)
opcaomenu1.add_command(label='Tema Preto', command=TemaPreto)

janela.mainloop()
