from tkinter import *
from tkinter import messagebox
from tkinter import ttk

alunos = []
matricula_atual = 0
index = 0


def adicionar_aluno() -> None:
    nome = txt_nome.get()
    curso = cb_curso.get()
    nota = float(txt_nota.get())
    global matricula_atual
    matricula_atual += 1
    aluno = {"matricula": matricula_atual, "nome": nome,
             "curso": curso, "nota": nota}
    alunos.append(aluno)
    limparCampos()
    messagebox.showinfo("Adicionado!", "Aluno cadastrado com sucesso!")
    atualizarTabela()


def preencherCampos(event) -> None:
    linha_clicada = tabela_alunos.selection()[0]
    global index
    index = tabela_alunos.index(linha_clicada)
    aluno = alunos[index]
    limparCampos()
    txt_matricula.config(state="normal")
    txt_matricula.insert(0, aluno["matricula"])
    txt_matricula.config(state=DISABLED)
    txt_nome.insert(0, aluno["nome"])
    txt_nota.insert(0, aluno["nota"])
    cb_curso.set(aluno["curso"])


def atualizarTabela() -> None:
    # limpar a tabela
    for linha in tabela_alunos.get_children():
        tabela_alunos.delete(linha)
    # Atualizando a tabela

    busca = txt_busca.get().lower()
    for aluno in alunos:
        if busca in aluno['nome'].lower():
            tabela_alunos.insert("", END,
                                 values=(aluno["matricula"],
                                         aluno["nome"],
                                         aluno["curso"],
                                         aluno["nota"]))


def limparCampos() -> None:
    txt_matricula.config(state="normal")
    txt_matricula.delete(0, END)
    txt_matricula.config(state=DISABLED)
    txt_nome.delete(0, END)
    txt_nota.delete(0, END)
    cb_curso.set("")


def deletarAluno() -> None:
    opcao = messagebox.askyesno("Tem certeza?",
                                "Deseja apagar o aluno?")
    if opcao:
        alunos.remove(alunos[index])
        limparCampos()
        atualizarTabela()
        messagebox.showinfo("Deletado!", "Aluno deletado com sucesso!")
    else:
        limparCampos()


def editarAluno() -> None:
    novo_nome = txt_nome.get()
    novo_curso = cb_curso.get()
    nova_nota = float(txt_nota.get())
    matricula = int(txt_matricula.get())

    opcao = messagebox.askyesno("Tem certeza?", "Deseja alterar os dados do aluno")

    if opcao:
        alunos[index] = {
            "matricula": matricula,
            "nome": novo_nome,
            "curso": novo_curso,
            "nota": nova_nota
        }
        limparCampos()
        atualizarTabela()
        messagebox.showinfo("Atualizado!", "Dados alterados com sucesso")


def buscarPorNome(event) -> None:
    atualizarTabela()


janela = Tk()
janela.title("Sistema - Infinity School")

label_matricula = Label(janela, text="Matricula:", font="Arial 14 bold",
                        fg="red")
label_matricula.grid(row=0, column=0)
txt_matricula = Entry(janela, font="Arial 14", width=27, state=DISABLED)
txt_matricula.grid(row=0, column=1)

label_nome = Label(janela, text="Nome:", font="Arial 14 bold",
                   fg="red")
label_nome.grid(row=1, column=0, sticky=E)
txt_nome = Entry(janela, font="Arial 14", width=27)
txt_nome.grid(row=1, column=1)

label_curso = Label(janela, text="Curso:", font="Arial 14 bold",
                    fg="red")
label_curso.grid(row=2, column=0, sticky=E)

cb_curso = ttk.Combobox(janela, width=27,
                        values=["Javascript", "Python",
                                "Django", "React"],
                        font="tahoma 14", state="readonly")
cb_curso.grid(row=2, column=1, sticky=W)

label_nota = Label(janela, text="Nota:", font="Arial 14 bold",
                   fg="red")
label_nota.grid(row=3, column=0, sticky=E)
txt_nota = Entry(janela, font="Arial 14", width=27)
txt_nota.grid(row=3, column=1)

btn_adicionar = Button(janela, fg="red", bg="white",
                       text="Adicionar", font="Tahoma 12 bold",
                       command=adicionar_aluno)
btn_adicionar.grid(row=4, column=0)

btn_editar = Button(janela, fg="red", bg="white",
                    text="Editar", font="Tahoma 12 bold", command=editarAluno)
btn_editar.grid(row=4, column=1)

btn_excluir = Button(janela, fg="red", bg="white",
                     text="Excluir", font="Tahoma 12 bold",
                     command=deletarAluno)
btn_excluir.grid(row=4, column=2)

columns = ("Matricula", "Nome", "Curso", "Nota")
tabela_alunos = ttk.Treeview(janela, show="headings",
                             columns=columns)
for coluna in columns:
    tabela_alunos.heading(coluna, text=coluna)
    tabela_alunos.column(coluna, width=110)
tabela_alunos.grid(row=5, columnspan=3)
tabela_alunos.bind("<ButtonRelease-1>", preencherCampos)

# Busca
label_busca = Label(janela, text="Buscar: ", font="Arial 14 bold", fg="red")
label_busca.grid(row=6, column=0)
txt_busca = Entry(janela, font="Arial 14", width=30)
txt_busca.grid(row=6, column=1, columnspan=3, sticky=W)
txt_busca.bind("<KeyRelease>", buscarPorNome)

janela.mainloop()
