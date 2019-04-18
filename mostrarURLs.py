from tkinter import *

def mostrarURLs():
         
         janelaURL = Tk()
         janelaURL.title('URLs')
         
         urlsDoPrograma = ["notEvil - hss3uro2hsxfogfq.onion", "The Chess - theches3nacocgsc.onion", "Torch - xmh57jrzrnw6insl.onion",
                   "Internet Archive - archivecrfip2lpi.onion", "DuckDuckGo - 3g2upl4pq6kufc4m.onion", "Web Shell Archive - z2huz7tsxluvnxoc.onion", "The New York Times - nytimes3xbfgragh.onion",
                   "Bible4u - bible4u2kjgjvbxs.onion", "Enot - enotegggr635n4lw.onion", "TorPaste - 5y5ek6tlzttcxgvlknf5mxybbsntfqsq2q2fngdbfmskgghukfkn5uqd.onion",
                   "Example Rendezvous Points Page - duskgytldkxiuqc6.onion", "Facebook - facebookcorewwwi.onion"]

         x=0
         for url in urlsDoPrograma:
             urlPrograma = Label(janelaURL, text=url, font=("Times New Roman", "11"))
             urlPrograma.grid(column=0, row=x)
             x+=1
