from Tkinter import *
from easysnmp import Session, snmp_walk

def interface(agente):
    def entra():
        agente.ip = ip_txt.get()
        agente.usuario = usuario_txt.get()
        agente.senha = senha_txt.get()
        agente.session = Session(hostname=agente.ip, community='public', version=3,
                security_level='auth_with_privacy',
                security_username=agente.usuario,
                privacy_protocol=agente.criptografia,
                privacy_password=agente.senha,
                auth_protocol=agente.autenticacao,
                auth_password=agente.senha)

        window.destroy()

    window = Tk()
    window.title("Gerencia de Redes")
    window.geometry('200x180')

    ip_label = Label(window, text="Endereco IP: ")
    ip_label.grid(column=0, row=0)
    ip_txt = Entry(window,width=10)
    ip_txt.grid(column=1, row=0)

    usuario_label = Label(window, text="Usuario: ")
    usuario_label.grid(column=0, row=2)
    usuario_txt = Entry(window,width=10)
    usuario_txt.grid(column=1, row=2)

    senha_label = Label(window, text="Senha: ")
    senha_label.grid(column=0, row=3)
    senha_txt = Entry(window,width=10)
    senha_txt.grid(column=1, row=3)

    senha_label = Label(window, text="Criptografia: ")
    senha_label.grid(column=0, row=4)
    senha_txt = Entry(window,width=10)
    senha_txt.grid(column=1, row=4)

    senha_label = Label(window, text="Autenticacao: ")
    senha_label.grid(column=0, row=5)
    senha_txt = Entry(window,width=10)
    senha_txt.grid(column=1, row=5)

    btn = Button(window, text="Entra", command=entra)
    btn.grid(column=1, row=6)

    window.mainloop()
