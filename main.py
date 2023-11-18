from tkinter import *
import json
import os


user = {}


def salvar_usuarios(user):
    try:
        with open('usuarios.json', 'w', encoding='utf-8') as arquivo_usuarios:
            json.dump(user, arquivo_usuarios)
    except FileNotFoundError:
        print("Caminho e/ou arquivo inexistente")


def carregar_usuarios():
    try:
        with open('usuarios.json', 'r') as arquivo_usuarios:
            return json.load(arquivo_usuarios)
    except FileNotFoundError:
        return {}


def is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def monitorar_batimentos():
    batimentos = Tk()
    batimentos.title("EaseSync")
    batimentos.geometry("600x500")
    batimentos.configure(bg="darkseagreen1")

    titulo = Label(batimentos, font="Cambria 20 bold", text="EaseSync",
                   pady=15, padx=10, bg="darkseagreen1")
    titulo.pack()
    subtitulo = Label(batimentos, font="Arial 14", text="Frequência cardíaca",
                      pady=10, padx=10, bg="darkseagreen1")
    subtitulo.pack()
    texto = Label(batimentos, font="Arial 12", text="Digite a frequência cardíaca atual:",
                  pady=10, padx=10, bg="darkseagreen1")
    texto.pack()

    caixa = Entry(batimentos)
    caixa.pack()

    def sair_app():
        batimentos.quit()

    def enviar():
        if is_number(caixa.get()):
            frequencia_cardiaca = float(caixa.get())
            if frequencia_cardiaca > 80:
                container = Frame(batimentos, pady=15, padx=15, bg="darkseagreen1")
                container.pack()
                alerta = Label(container, font="Arial 14 bold",
                               text="Frequência cardíaca elevada. Iniciando terapia mindfulness...",
                               pady=10, padx=15)
                alerta.pack()
                iniciar_terapia()
            else:
                container = Frame(batimentos, pady=15, padx=15, bg="darkseagreen1")
                container.pack()
                alerta = Label(container, font="Arial 14 bold",
                               text="Frequência cardíaca normal.",
                               pady=10, padx=15)
                alerta.pack()
                sair = Button(container, font="Arial 10", text="Sair",
                              pady=5,padx=5, command=sair_app)
                sair.pack()

    btn = Button(batimentos, font="Arial 10", text="Enviar",
                 pady=5, padx=5, command=enviar)
    btn.pack()


def iniciar_terapia():
    def play_yt():
        url = video.get()
        os.system("vlc " + url)

    def sair():
        terapia.destroy()

    terapia = Tk()
    terapia.title("EaseSync")
    terapia.configure(bg="plum")

    titulo = Label(terapia, font="Cambria 20 bold", text="EaseSync",
                   pady=10, padx=10, bg="darkseagreen1")
    titulo.pack()
    subtitulo = Label(terapia, font="Arial 16", text="Iniciando terapia mindfulness",
                      pady=10, padx=10, bg="darkseagreen1")

    subtitulo.pack()
    video = StringVar()
    txt = Entry(terapia, textvariable=video)
    txt.pack()

    btn_play = Button(terapia, text="Play", command=play_yt)
    btn_play.pack()

    btn_sair = Button(terapia, text="Sair", command=sair)
    btn_sair.pack()


def menu():
    home_page = Tk()
    home_page.title("EaseSync")
    home_page.geometry("500x300")
    home_page.configure(bg="darkseagreen1")

    heading = Label(home_page, font="Cambria 20 bold", text="EaseSync",
                    pady=10, padx=10, bg="darkseagreen1")
    heading.pack()
    texto = Label(home_page, font="Arial 14", text="O que gostaria de fazer?",
                  pady=5, padx=5, bg="darkseagreen1")
    texto.pack()

    container = Frame(home_page, pady=15, padx=10)
    container.pack()
    monitorar = Button(container, font="Arial 10", text="Monitorar batimentos cardíacos",
                       pady=5, padx=5, command=monitorar_batimentos)
    monitorar.pack(side=TOP)
    terapia = Button(container, font="Arial 10", text="Iniciar terapia mindfulness",
                     pady=5, padx=5, command=iniciar_terapia)
    terapia.pack(side=BOTTOM)


def fazer_login():
    def validacao_login():
        usuarios = carregar_usuarios()
        if nome_caixa.get() in usuarios and usuarios['senha'] == senha_caixa.get():
            menu()
        else:
            container4 = Frame(login, pady=15, padx=10, bg="darkseagreen1")
            container4.pack()
            novamente = Label(container4, font="Arial 12 bold", text="Usuário não encontrado. Tente novamente.",
                              pady=10, padx=10, bg="darkseagreen1")
            novamente.pack()

    window.destroy()
    login = Tk()
    login.title("EaseSync")
    login.geometry("350x250")
    login.configure(bg="darkseagreen1")

    titulo = Label(login, font="Arial 20 bold", text="Faça seu login:",
                   pady=10, padx=10, bg="darkseagreen1")
    titulo.pack()

    container = Frame(login, pady=15, padx=10)
    container.pack()
    nome = Label(container, font="Arial 10", text="Nome:",
                 pady=5, padx=5)
    nome.pack(side=LEFT)
    nome_caixa = Entry(container)
    nome_caixa.pack(side=RIGHT)

    container2 = Frame(login, pady=15, padx=9)
    container2.pack()
    senha = Label(container2, font="Arial 10", text="Senha:",
                  pady=5, padx=5)
    senha.pack(side=LEFT)
    senha_caixa = Entry(container2, show="*")
    senha_caixa.pack(side=LEFT)

    container3 = Frame(login, pady=15, padx=10, bg="darkseagreen1")
    container3.pack()
    enviar = Button(container3, pady=5, padx=5, font="Arial 10",
                    text="Entrar", command=validacao_login)
    enviar.pack(side=BOTTOM)


def fazer_cadastro():
    def validacao_cadastro():
        usuarios = carregar_usuarios()
        if nome_caixa.get() in usuarios:
            container4 = Frame(cadastro, pady=15, padx=10, bg="darkseagreen1")
            container4.pack()
            novamente = Label(container4, font="Arial 12 bold", text="Usuário já cadastrado.",
                              pady=10, padx=10, bg="darkseagreen1")
            novamente.pack()

        else:
            users = {'nome': nome_caixa.get(), 'senha': senha_caixa.get()}
            salvar_usuarios(users)
            menu()

    window.destroy()
    cadastro = Tk()
    cadastro.title("EaseSync")
    cadastro.geometry("350x250")
    cadastro.configure(bg="darkseagreen1")

    titulo = Label(cadastro, font="Arial 20 bold", text="Cadastre-se:",
                   pady=10, padx=10, bg="darkseagreen1")
    titulo.pack()

    container = Frame(cadastro, pady=15, padx=10)
    container.pack()
    nome = Label(container, font="Arial 10", text="Nome:",
                 pady=5, padx=5)
    nome.pack(side=LEFT)
    nome_caixa = Entry(container)
    nome_caixa.pack(side=RIGHT)

    container2 = Frame(cadastro, pady=15, padx=9)
    container2.pack()
    senha = Label(container2, font="Arial 10", text="Senha:",
                  pady=5, padx=5)
    senha.pack(side=LEFT)
    senha_caixa = Entry(container2, show="*")
    senha_caixa.pack(side=LEFT)

    container3 = Frame(cadastro, pady=15, padx=10, bg="darkseagreen1")
    container3.pack()
    enviar = Button(container3, pady=5, padx=5, font="Arial 10",
                    text="Cadastrar", command=validacao_cadastro)
    enviar.pack(side=BOTTOM)


window = Tk()
window.title("EaseSync")
window.geometry("350x250")
window.configure(bg="darkseagreen1")

rotulo = Label(window, font="Arial 20 bold",
               text="Escolha uma opção:", pady=10,
               padx=10, bg="darkseagreen1")
rotulo.pack()

btn_login = Button(window, font="Arial 14", text="Fazer login",
                   pady=5, padx=5, command=fazer_login)
btn_login.pack()
btn_cadastro = Button(window, font="Arial 14", text="Fazer cadastro",
                      pady=5, padx=5, command=fazer_cadastro)
btn_cadastro.pack()

window.mainloop()
