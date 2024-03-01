from tkinter import *
import tkinter.messagebox


#cores---------------------

cor0 = "#444466"  # Preta   \  black
cor1 = "#feffff"  # branca  \  white
cor2 = "#004338"

#criando  a janela---------

janela = Tk()
janela.geometry("530x205")
janela.configure(bg=cor1)


# configurando a janela ----


tela = Label(janela, bg=cor0, width=40, height=10,)
tela.grid(row=0, column=0)

Frame_direita = Frame(janela, bg=cor1)
Frame_direita.grid(row=0, column=1, padx=5)

Frame_baixo = Frame(janela, bg=cor1)
Frame_baixo.grid(row=1, column=0, columnspan=2, pady=15)


#função scale

def escala(valor):
    r = s_red.get()
    g = s_green.get()
    b = s_blue.get()

    rgb = f'{r}, {g}, {b}'


    hexadecimal = "#%02x%02x%02x" % (r, g, b)
    
    # alterando a cor do fundo da tela
    tela['bg'] = hexadecimal


    #aletrando a entry
    e_cor.delete(0, END)
    e_cor.insert(0, hexadecimal)


#função clicar deslizar
    
def onClick():

    # informar 
    tkinter.messagebox.showinfo('Cor', "A cor foi copiada")

    #serve para criar botão copiar
    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append(e_cor.get())
    clip.destroy()













# configurando o frame direita

#vermelho

l_red = Label(Frame_direita,text='Red',width=7, bg=cor1, fg='red', anchor="nw", font=("Time New Roman", 12, "bold" ))
l_red.grid(row=0, column=0)

s_red=Scale(Frame_direita,command=escala,from_= 0, to=255, length=150, bg=cor1, fg="red", orient=HORIZONTAL)
s_red.grid(row=0, column=1)

#verde

l_green = Label(Frame_direita,text='Green',width=7, bg=cor1, fg='green', anchor="nw", font=("Time New Roman", 12, "bold" ))
l_green.grid(row=1, column=0)

s_green=Scale(Frame_direita,command=escala, from_= 0, to=255, length=150, bg=cor1, fg="green", orient=HORIZONTAL)
s_green.grid(row=1, column=1)

#azul

l_blue = Label(Frame_direita,text='Blue',width=7, bg=cor1, fg='blue', anchor="nw", font=("Time New Roman", 12, "bold" ))
l_blue.grid(row=2, column=0)

s_blue=Scale(Frame_direita,command=escala, from_= 0, to=255, length=150, bg=cor1, fg="Blue", orient=HORIZONTAL)
s_blue.grid(row=2, column=1)


#configurando frame baixo -----

l_rgb = Label(Frame_baixo,text='CÓDIGO RGB :', bg=cor1, font=("Ivy", 10, "bold" ))
l_rgb.grid(row=0, column=0, padx=5)

#entry

e_cor = Entry(Frame_baixo, width=12, font=("Ivy", 10, "bold" ), justify=CENTER )
e_cor.grid(row=0, column=1, padx=5)

#botão copiar

b_copiar = Button(Frame_baixo,command=onClick ,text='Copiar a cor', bg=cor1, font=("Ivy", 8, "bold" ), relief=RAISED, overrelief=RIDGE)
b_copiar.grid(row=0, column=2, padx=5)



# app nome

l__app_nome = Label(Frame_baixo,text='Seletor de Cores', bg=cor1, font=("Ivy", 15, "bold" ))
l__app_nome.grid(row=0, column=3, padx=40)

janela.mainloop()