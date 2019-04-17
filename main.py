from tkinter import *
import random

janela = Tk()
janela.title("Deep Web Link Aleatório")
janela.geometry("280x100")
janela.configure(bg="black")

fonte1 = ("Comic Sans MS", "10")

menubar = Menu(janela)
janela.config(menu=menubar)
opcaomenu1 = Menu(menubar)
menubar.add_cascade(label='Temas', menu=opcaomenu1)

def mostrarLinks():
         
         janelaURL = Tk()
         janelaURL.title('Links')
         
         url1 = Label(janelaURL, text="DuckDuckGo - 3g2upl4pq6kufc4m.onion", font=fonte1)
         url2 = Label(janelaURL, text="notEvil - hss3uro2hsxfogfq.onion", font=fonte1)
         url3 = Label(janelaURL, text="Torch - xmh57jrzrnw6insl.onion", font=fonte1)
         url4 = Label(janelaURL, text="The Chess - theches3nacocgsc.onion", font=fonte1)
         url5 = Label(janelaURL, text="Enot - enotegggr635n4lw.onion", font=fonte1)       
         url6 = Label(janelaURL, text="Internet Archive - archivecrfip2lpi.onion", font=fonte1)
         url7 = Label(janelaURL, text="Bible4u - bible4u2kjgjvbxs.onion", font=fonte1)
         url8 = Label(janelaURL, text="TorPaste - 5y5ek6tlzttcxgvlknf5mxybbsntfqsq2q2fngdbfmskgghukfkn5uqd.onion", font=fonte1)
         url9 = Label(janelaURL, text="Facebook - facebookcorewwwi.onion", font=fonte1)
         url10 = Label(janelaURL, text="Example Rendezvous Points Page - duskgytldkxiuqc6.onion", font=fonte1)
         url11 = Label(janelaURL, text="Web Shell Archive - z2huz7tsxluvnxoc.onion", font=fonte1)
                                                                             
         url1.grid(column=0, row=0)
         url2.grid(column=0, row=1)
         url3.grid(column=0, row=3)
         url4.grid(column=0, row=4)
         url5.grid(column=0, row=5)
         url6.grid(column=0, row=6)
         url7.grid(column=0, row=7)
         url8.grid(column=0, row=8)
         url9.grid(column=0, row=9) 
         url10.grid(column=0, row=10)
         url11.grid(column=0, row=11)
                                                                             
opcaomenu2 = Menu(menubar)
menubar.add_cascade(label='Links', menu=opcaomenu2)
opcaomenu2.add_command(label='Mostrar Links', command=mostrarLinks)

def ajudaNavegadores():

    janelaNavegadores = Tk()
    janelaNavegadores.title('Navegadores')

    redeOnion = Label(janelaNavegadores, text="Rede onion: https://www.torproject.org/download/", font=fonte1)
    redeI2P = Label(janelaNavegadores, text="Rede i2p: https://geti2p.net/pt-br/download", font=fonte1)

    redeOnion.grid(column=0, row=0)
    redeI2P.grid(column=0, row=1)
    
opcaomenu3 = Menu(menubar)
menubar.add_cascade(label='Ajuda', menu=opcaomenu3)
opcaomenu3.add_command(label='Navegadores', command=ajudaNavegadores)

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
