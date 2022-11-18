"""Minhas Senhas App Main File """
from tkinter import *
# Import messagebox
from tkinter import messagebox
# Import do arquivo de base de dados
import database
# Import da biblioteca pyperclip para copiar a senha para área de transferência
import pyperclip

# ---------------------------- FUNÇÕES ------------------------------- #

# ---------------------------- CONEXAO COM O BANCO ------------------- #
conexao = database.cria_conexao()
cursor = database.cria_cursor()

# ---------------------------- SAlVAR DADOS ------------------------------- #
def salva_dados():
    # recuperando dados do usuário
    plataforma = plataforma_entry.get()
    email = email_entry.get()
    senha = password_entry.get()
    # valida os campos e confirma os dados com o usuário
    if len(plataforma) == 0 or len(senha) == 0:
        messagebox.showinfo(title="Oops", message="Não deixe os campos em branco!")
    else:
        ok = messagebox.askokcancel(title="Confirma entradas", message=f"Estes são os dados inseridos\n"
                                                                        f"Email: {email}"
                                                                        f"\Senha: {senha}\nSalvar?")
        if ok:
            # copia a senha para área de tranferência
            pyperclip.copy(senha)
            # insere os dados no banco de dados
            insere_dados = "insert into usuario(plataforma ,email, senha) values ('"+plataforma+"', '"+email+"', '"+senha+"');"
            database.executa_query(insere_dados)


# ---------------------------- RECUPERA A SENHA NO BANCO DE DADOS ------------------------------- #
def procura_senha():
    # recupera a plataforma digitada
    plataforma = plataforma_entry.get()
    # recupera a senha do banco de dados
    if len(plataforma) == 0:
        messagebox.showinfo(title="Oops", message="Insira uma plataforma para procurar!")
    else:
        cursor.execute("select plataforma, email, senha from usuario where plataforma =('"+plataforma+"')")
        result = cursor.fetchall()

        # flag para verificar se encontrou a plataforma no banco ou não
        plataforma_banco = ""

        for r in result:
            plataforma_banco = str(r[0])
            email = str(r[1])
            senha = str(r[2])    

        # validação da flag para verificar se há ou não a senha cadastrada no banco 
        if plataforma_banco == plataforma:            
            # confirma as informações com o usuário
            confirma_dados = messagebox.askokcancel(title=plataforma, message=f"Email: {email}\nSenha: {senha}"
                                                                            f"\n\nCopiar senha?")
            if confirma_dados:
                # copia a senha para área de tranferência
                pyperclip.copy(senha)
                messagebox.showinfo(title="Salvo na área de transferência", message="Senha copiada com sucesso!")
            else:
                messagebox.showinfo(title="Operação cancelada", message=f"Consulta cancelada!")
        else:
            messagebox.showinfo(title="Senha não encontrada", message=f"Senha não encontrada no banco de dados!")

# ---------------------------- PERSONALIZAÇÃO ------------------------------- #
TELA_BG = "#FFA500"
FIELD_COLORS = "#dddddd"
FIELD_FONT_COLOR = "#008080"
LABEL_COLOR = "white"
FONT = ("Courier", 15, "normal")

# ---------------------------- INTERFACE ------------------------------- #
tela = Tk()
tela.title("Minhas Senhas App")
tela.config(padx=20, pady=20, bg=TELA_BG)

# NOME DOS CAMPOS
# CAMPO DO SITE
plataforma_label = Label(text="Plataforma", bg=TELA_BG, padx=20, font=FONT, fg=LABEL_COLOR)
plataforma_label.grid(column=0, row=1, sticky=W)

# CAMPO DO EMAIL/USERNAME
email_label = Label(text="Email/Username", bg=TELA_BG, padx=20, font=FONT, fg=LABEL_COLOR)
email_label.grid(column=0, row=2, sticky=W)

# CAMPO DA SENHA
password_label = Label(text="Password", bg=TELA_BG, padx=20, font=FONT, fg=LABEL_COLOR)
password_label.grid(column=0, row=3,sticky=W)
tela.grid_columnconfigure(1, weight=1)

# ENTRADA DE DADOS
plataforma_entry = Entry(width=30, bg=FIELD_COLORS, fg=FIELD_FONT_COLOR, font=FONT)
plataforma_entry.insert(END, string="")
plataforma_entry.grid(column=1, row=1)

plataforma_entry.focus()
email_entry = Entry(width=30, bg=FIELD_COLORS, fg=FIELD_FONT_COLOR, font=FONT)
email_entry.insert(END, string="")
email_entry.grid(column=1, row=2)

password_entry = Entry(width=30, bg=FIELD_COLORS, fg=FIELD_FONT_COLOR, font=FONT)
password_entry.insert(END, string="")
password_entry.grid(column=1, row=3)

# BOTOES
procura_btn = Button(text="Search", bg='#20B2AA', padx=95, font=FONT, command=procura_senha)
procura_btn.grid(column=3, row=1)

add_btn = Button(text="Add", bg='#20B2AA', width=36, command=salva_dados, font=FONT)
add_btn.grid(column=1, row=5, columnspan=2, sticky=W)

# Dummy widget for to get an empty rows
dummy_label = Label(bg=TELA_BG)
dummy_label.grid(column=0, row=4, sticky=W)

tela.mainloop()

