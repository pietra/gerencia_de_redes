from tkinter import *
 
window = Tk()
window.title("Gerência de Redes")
window.geometry('200x100')

ip_label = Label(window, text="Endereço IP: ")
ip_label.grid(column=0, row=0)
ip = Entry(window,width=10)
ip.grid(column=1, row=0)

usuario_label = Label(window, text="Usuário: ")
usuario_label.grid(column=0, row=2)
usuario = Entry(window,width=10)
usuario.grid(column=1, row=2)

senha_label = Label(window, text="Senha: ")
senha_label.grid(column=0, row=3)
senha = Entry(window,width=10)
senha.grid(column=1, row=3)

window.mainloop()
 