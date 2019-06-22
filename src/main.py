# -*- coding: utf-8 -*-
import tkinter as tk
import platform
import sqlite3
import webbrowser
import definir_cor
import mostrar_urls
import ajuda_redes

def main():
    wMain = tk.Tk()
    wMain.title('Deep Web URL Aleatório')
    wMain.configure(bg = definir_cor.COR_PRETA)
    
    so = platform.system()
    try:
        if so == 'Linux':
           wMain.wm_iconbitmap('@ico/dw_ico.xbm')
    except TclError:
        print('dw_ico.xbm não foi encontrado na pasta ico.')
    try:
        if so == 'Windows':
           wMain.wm_iconbitmap('ico\dw_ico.ico')
    except TclError:
        print('dw_ico.ico não foi encontrado na pasta ico.')
        
    menubar = tk.Menu(wMain)
    wMain.config(menu = menubar)

    temas = tk.Menu(menubar, tearoff = 0)
    menubar.add_cascade(label = 'Temas', menu = temas)

    ajuda = tk.Menu(menubar, tearoff = 0)
    menubar.add_cascade(label = 'Ajuda', menu = ajuda)
    ajuda.add_command(label = 'URLs', command = mostrar_urls.mostrar_urls)
    ajuda.add_command(label = 'Redes', command = ajuda_redes.ajuda_redes)

    lTitulo = tk.Label(wMain, text = 'Deep Web URL Aleatório', 
                    font = ('Comic Sans MS', '10', 'bold'))
    lTitulo.grid(column = 0, row = 0, sticky = tk.N)
    lTitulo.configure(bg = definir_cor.COR_PRETA, fg = definir_cor.COR_VERDE_CLARO)
    
    def tema_branco():        
        wMain.configure(bg = definir_cor.COR_BRANCA)
        lTitulo.configure(bg = definir_cor.COR_BRANCA, fg = definir_cor.COR_PRETA)
        lURL.configure(bg = definir_cor.COR_BRANCA, fg = definir_cor.COR_PRETA)
        botao_go.configure(bg = definir_cor.COR_BRANCA, fg = definir_cor.COR_PRETA)

    def tema_preto():      
        wMain.configure(bg = definir_cor.COR_PRETA)
        lTitulo.configure(bg = definir_cor.COR_PRETA, fg = definir_cor.COR_VERDE_CLARO)
        lURL.configure(bg = definir_cor.COR_PRETA, fg = definir_cor.COR_VERDE_CLARO)
        botao_go.configure(bg = definir_cor.COR_PRETA, fg = definir_cor.COR_VERDE_CLARO)

    temas.add_command(label = 'Tema Branco', command = tema_branco)
    temas.add_command(label = 'Tema Preto', command = tema_preto)
    
    fonte = ('Comic Sans MS', '10')
    lURL = tk.Label(wMain, text = 'URL', font = fonte)
    lURL.grid(column = 0, row = 2)
    lURL.configure(bg = definir_cor.COR_PRETA, fg = definir_cor.COR_VERDE_CLARO)

    def botao_go_clicado():        
        conn = sqlite3.connect('urls.db')
        cursor = conn.cursor()
        cursor.execute("""
        SELECT url FROM urls  ORDER BY RANDOM() LIMIT 1;
        """)
        url_ = cursor.fetchall()
        url2_ = str(url_).strip('()[],\'\'')
        lURL.configure(text = url_)
        conn.close()
        def clicar_url(event):
            webbrowser.open_new(url2_)
        lURL.bind('<Button-1>', clicar_url)
            
    botao_go = tk.Button(wMain, text = 'Go!', command = botao_go_clicado)
    botao_go.grid(column = 0, row = 4)
    botao_go.configure(bg = definir_cor.COR_PRETA, fg = definir_cor.COR_VERDE_CLARO)

    wMain.mainloop()
        
if __name__ == '__main__':
   main()
