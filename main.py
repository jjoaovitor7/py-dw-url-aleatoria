from tkinter import *
import random, webbrowser
from mostrarURLs import *
from ajudaNavegadores import *

janela=Tk()
janela.title('Deep Web Link Aleatório')
janela.wm_iconbitmap('dw_ico.ico')
janela.geometry('300x100')
janela.configure(bg='black')

fonte1=('Comic Sans MS', '10')

menubar=Menu(janela)
janela.config(menu=menubar)
temas=Menu(menubar)
menubar.add_cascade(label='Temas', menu=temas)
    
ajuda = Menu(menubar)
menubar.add_cascade(label='Ajuda', menu=ajuda)
ajuda.add_command(label='URLs', command=mostrar_urls)
ajuda.add_command(label='Navegadores', command=ajuda_navegadores)

titulo=Label(janela, text='Deep Web Link Aleatório', font=('Comic Sans MS', '10', 'bold'))
titulo.grid(column=0, row=0, sticky=N)
titulo.configure(bg='black', fg='#00ff00')

url=Label(janela, text="URL", font=fonte1)
url.grid(column=0, row=2)
url.configure(bg='black', fg ='#00ff00')

def botaoGoClicado():        
        sitesDW=["facebookcorewwwi.onion", "hss3uro2hsxfogfq.onion", "theches3nacocgsc.onion", "qtx6d2ggmma6hgio.onion" 
                   "archivecrfip2lpi.onion", "3g2upl4pq6kufc4m.onion", "5y5ek6tlzttcxgvlknf5mxybbsntfqsq2q2fngdbfmskgghukfkn5uqd.onion", 
                   "bible4u2kjgjvbxs.onion", "enotegggr635n4lw.onion", "nytimes3xbfgragh.onion", "juy4e6eicawzdrz7.onion", "nzxj65x32vh2fkhk.onion",
                   "duskgytldkxiuqc6.onion", "z2huz7tsxluvnxoc.onion", "gnvweaoe2xzjqldu.onion" "5plvrsgydwy2sgce.onion", "searchb5a7tmimez.onion", "nxhhwbbxc4khvvlw.onion", "nrybuqtxgxnavtla.onion", "eljwdzi4pgrrlwwq.onion"]
        siteDW=random.choice(sitesDW)
        def clicarLink(event):
                webbrowser.open_new(siteDW)
        url.configure(text=siteDW)
        url.bind("<Button-1>", clicarLink)
        
siteBotao=Button(janela, text='Go!', command=botaoGoClicado)
siteBotao.grid(column=0, row=4)
siteBotao.configure(bg='black', fg='#00ff00')

def TemaBranco():        
        janela.configure(bg='white')
        titulo.configure(bg='white', fg='black')
        url.configure(bg='white', fg='black')
        siteBotao.configure(bg='white', fg='black')

def TemaPreto():      
        janela.configure(bg='black')
        titulo.configure(bg='black', fg='#00ff00')
        url.configure(bg='black', fg='#00ff00')
        siteBotao.configure(bg='black', fg='#00ff00')

temas.add_command(label='Tema Branco', command=TemaBranco)
temas.add_command(label='Tema Preto', command=TemaPreto)

janela.mainloop()
