from tkinter import *

def mostrarURLs():      
         janelaURL = Tk()
         janelaURL.title('URLs')
         janelaURL.wm_iconbitmap("dw_ico.ico")
         
         urlsDoPrograma = ["Bible4u - bible4u2kjgjvbxs.onion", "notEvil - hss3uro2hsxfogfq.onion", "The Chess - theches3nacocgsc.onion", "SearX - 5plvrsgydwy2sgce.onion", "SearX - juy4e6eicawzdrz7.onion", "SearX - searchb5a7tmimez.onion", "SearX - nxhhwbbxc4khvvlw.onion", "SearX - nrybuqtxgxnavtla.onion", "SearX - eljwdzi4pgrrlwwq.onion", 
                   "Internet Archive - archivecrfip2lpi.onion", "DuckDuckGo - 3g2upl4pq6kufc4m.onion", "Web Shell Archive - z2huz7tsxluvnxoc.onion", "The New York Times - nytimes3xbfgragh.onion", "Stronghold Paste - nzxj65x32vh2fkhk.onion",
                   "Enot - enotegggr635n4lw.onion", "TorPaste - 5y5ek6tlzttcxgvlknf5mxybbsntfqsq2q2fngdbfmskgghukfkn5uqd.onion", "Planet Debian - gnvweaoe2xzjqldu.onion",
                   "Example Rendezvous Points Page - duskgytldkxiuqc6.onion", "CryptoShare - qtx6d2ggmma6hgio.onion", "Facebook - facebookcorewwwi.onion"]

         x=0
         for url in urlsDoPrograma:
             urlPrograma = Label(janelaURL, text=url, font=("Times New Roman", "11"))
             urlPrograma.grid(column=0, row=x)
             x+=1
