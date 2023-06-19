import ply.lex as lex
from ply import yacc
from cProfile import label
import tkinter as tk #Biblioteca para interfaces gráficas
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import filedialog as fd

reserved = {
    'IFSULDEMINAS': 'IFSULDEMINAS',
    'INICIO': 'INICIO',
    'COMPILADORES': 'COMPILADORES',
    'FIM': 'FIM',
    'SE': 'SE',
    'SENAO': 'SENAO',
    'ENQUANTO': 'ENQUANTO',
    'PARA': 'PARA',
    'INTERROMPA': 'INTERROMPA',
    'DEFINE': 'DEFINE',
    'LEIA': 'LEIA',
    'ESCREVA': 'ESCREVA',
    'AUX' : 'AUX'
}

tokens = [
    'OP_ARIT', #'+', '-', '/', '*'
    'OP_REL', #'<', '>', '<>', '<=', '>=', '=='
    'OP_ATRIBUI', #':='
    'OP_LOGICO',
    'ASPAS',
    'ABRE_CH', #'{'
    'FECHA_CH', #'}'
    'ABRE_CLT', #'['
    'FECHA_CLT', #']'
    'ABRE_P', #'('
    'FECHA_P', #')'
    'COMENT', #'**...'
    'VIRGULA', #','
    'DOIS_PONTOS',
    'DELIMITADOR', #';'
    'VAR',
    'VALOR_NUMINT',
    'VALOR_TEXTO',
    'VALOR_NUMDEC',
    'BOOLEANO',
    
#Verificação de compatibilidade com o ply (biblioteca utilizada)
'ignore', #ignorar tabulação e espaços
'NUMERO_MF', #número mal formado
'TEXTO_MF', #string mal formada
'VARIAVEL_MF', #variável mal formada
] + list(reserved.values()) #Concatenação com as palavras reservadas

t_OP_ARIT = r'[\+\-\/\*]'
t_VIRGULA = r'\,'
t_ASPAS = r'\"'
t_DOIS_PONTOS = r'\:'
t_COMENT =  r'¨(.*)'
t_BOOLEANO = r'\b(VERDADEIRO|FALSO)\b'

t_IFSULDEMINAS = r'IFSULDEMINAS'
t_INICIO = r'INICIO'
t_COMPILADORES = r'COMPILADORES'
t_FIM = r'FIM'
t_SE = r'SE'
t_SENAO = r'SENAO'
t_ENQUANTO = r'ENQUANTO'
t_PARA = r'PARA'
t_INTERROMPA = r'INTERROMPA'
t_DEFINE = r'DEFINE'
t_ESCREVA = r'ESCREVA'
t_LEIA = r'LEIA'

t_OP_REL = r'[<>]=?|==|!='
t_OP_ATRIBUI = r'\:='
t_OP_LOGICO = r'\b(E|OU)\b'
t_ABRE_P = r'\('
t_FECHA_P = r'\)'
t_ABRE_CH = r'\{'
t_FECHA_CH = r'\}'
t_ABRE_CLT = r'\['
t_FECHA_CLT = r'\]'
t_ignore= ' \t' #Ignora espaços e tabulações

def t_VALOR_TEXTO(t):
    r'("[^"]*")'
    return t

def t_TEXTO_MF(t):
    r'("[^"]*)'
    return t

def t_VARIAVEL_MF(t):
    r'([0-9]+[a-z]+)|([@!#$%&*]+[a-z]+|[a-z]+\.[0-9]+|[a-z]+[@!#$%&*]+)'
    return t

def t_NUMERO_MF(t):
    r'([0-9]+\.[a-z]+[0-9]+)|([0-9]+\.[a-z]+)|([0-9]+\.[0-9]+[a-z]+)'
    return t

def t_VALOR_NUMDEC(t):
    r'([0-9]+\.[0-9]+)|([0-9]+\.[0-9]+)'
    return t

def t_VALOR_NUMINT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_VAR(t):
    r'[a-z][a-z_0-9]*'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_DELIMITADOR(t):
    r'\;'
    return t
    t.lexer.lineno += len(t.value)

#Regras para tratamento de erros
erroslexicos = []
def t_error(t):
    erroslexicos.append(t)
    t.lexer.skip(1)

#Análise Sintática

def p_statements_multiple(p):
    '''
    statements : statements statement
    '''

def p_statements_single(p):
    '''
    statements : statement
    '''

def p_statement_comentarios(p):
    '''
    statement : COMENT
    '''
def p_statement_interrompa(p):
    '''
    statement : INTERROMPA DELIMITADOR

    '''
 
def p_statement_ifsuldeminas(p):
    '''
    statement : IFSULDEMINAS DELIMITADOR
    '''

def p_statement_compiladores(p):
    '''
    statement : COMPILADORES DELIMITADOR
    '''

def p_statement_inicio(p):
    '''
    statement : INICIO ABRE_CH FECHA_CH
    '''

def p_statement_fim(p):
    '''
    statement : FIM ABRE_CH FECHA_CH
    '''
    
def p_statement_define(p):
    '''
    statement : DEFINE ABRE_P VAR FECHA_P ABRE_CLT statement FECHA_CLT
              | DEFINE ABRE_P VAR FECHA_P ABRE_CLT SE ABRE_P cond_param FECHA_P FECHA_CLT FECHA_CLT
              | DEFINE ABRE_P VAR FECHA_P ABRE_CLT SE ABRE_P cond_param FECHA_P statement FECHA_CLT FECHA_CLT
              | DEFINE ABRE_P VAR FECHA_P ABRE_CLT SE ABRE_P cond_param FECHA_P statement FECHA_CLT SENAO ABRE_CLT statement FECHA_CLT FECHA_CLT 
              
    '''
def p_statement_enquanto(p):
    '''
    statement : ENQUANTO ABRE_P cond_param FECHA_P ABRE_CLT statements FECHA_CLT
              
    '''

def p_statement_para(p):
    '''
    statement : PARA ABRE_P VAR OP_ATRIBUI VALOR_NUMINT VIRGULA cond_param VIRGULA VAR OP_ARIT OP_ARIT FECHA_P ABRE_CLT statements FECHA_CLT
    '''

def p_statement_atribuicaoValorVariavel(p):
    '''
    statement : VAR OP_ATRIBUI VALOR_NUMINT DELIMITADOR
             | VAR OP_ATRIBUI VALOR_NUMDEC DELIMITADOR
             | VAR OP_ATRIBUI VALOR_TEXTO DELIMITADOR
             | VAR OP_ATRIBUI VAR OP_ARIT OP_ARIT DELIMITADOR
             | VAR OP_ATRIBUI VAR DELIMITADOR
             | VAR OP_ATRIBUI VAR OP_ARIT VALOR_NUMINT DELIMITADOR
             | VAR OP_ATRIBUI VAR OP_ARIT VALOR_NUMDEC DELIMITADOR
             | VAR OP_ATRIBUI funcao DELIMITADOR
             | VAR DELIMITADOR
             | VAR OP_ATRIBUI VAR OP_ARIT VAR DELIMITADOR
    '''

def p_statement_condicionais(p):
    '''
    statement : SE ABRE_P cond_param FECHA_P ABRE_CLT statements FECHA_CLT
              | SE ABRE_P cond_param FECHA_P ABRE_CLT statements FECHA_CLT SENAO ABRE_CLT statements FECHA_CLT
            
    '''

def p_statement_funcao_invocada(p):
    '''
    statement : funcao DELIMITADOR
    '''

def p_statement_definir_funcao(p):
    '''
    statement : funcao ABRE_CLT statements FECHA_CLT
    '''

def p_parametro_condicional(p):
    '''
    cond_param : VAR OP_REL VALOR_NUMINT
              | VAR OP_REL VALOR_NUMDEC
              | VAR OP_REL VALOR_TEXTO

              | VAR OP_REL VALOR_NUMINT OP_LOGICO VAR OP_REL VALOR_NUMINT
              | VAR OP_REL VALOR_NUMDEC OP_LOGICO VAR OP_REL VALOR_NUMDEC
              | VAR OP_REL VALOR_TEXTO OP_LOGICO VAR OP_REL VALOR_TEXTO
              | BOOLEANO
    '''

def p_aux(p):
    'statement : AUX'

def p_impressao(p):
    '''
    statement : ESCREVA ABRE_P VAR FECHA_P DELIMITADOR
              | ESCREVA ABRE_P ASPAS statements ASPAS FECHA_P DELIMITADOR
              | ESCREVA ABRE_P param FECHA_P DELIMITADOR
              | ESCREVA ABRE_P param DOIS_PONTOS
    '''

def p_true_false(p):
    '''statement : BOOLEANO
                    '''

def p_leitura(p):
    '''
    statement : LEIA ABRE_P VAR FECHA_P DELIMITADOR

    '''

def p_parametros_condicionais_grupo(p):
    '''
    cond_param : cond_param OP_REL cond_param
    '''

def p_parametro_vazio(p):
    '''
    param_vazio :
    '''

def p_parametro(p):
    '''
    param : VALOR_NUMINT
          | VALOR_NUMDEC
          | VALOR_TEXTO
          | VAR
    '''

def p_parametro_grupo(p):
    '''
    param : param VIRGULA param
    '''

def p_regra_funcao(p):
    '''
    funcao : ABRE_P param_vazio FECHA_P
          | ABRE_P param FECHA_P
    '''

errossintaticos = []
def p_error(p):
    errossintaticos.append(p)
    print('ERRO: ', p)

parser = yacc.yacc()

#Execução do algoritmo começa aqui
erros = 0

#Função para adicionar as classficações dos tokens para ser impressa pelo compilador
'''"append" pega a linha, a posição da coluna (no caso, em relação ao início), o Token, o Lexema
  # e a mensagem'''
def add_lista_saida(t, notificacao):
    saidas.append((t.lineno, t.lexpos, t.type, t.value, notificacao))

saidas = []

root = tk.Tk()

class Application():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.botoes()
        self.Menus()
        root.mainloop()

    def limpa_telaentrada(self):
        self.codigo_entry.delete(1.0, END)
        for i in self.saida.get_children():
            self.saida.delete(i)
        saidas.clear()
        erroslexicos.clear()
        errossintaticos.clear()
        global erros
        erros = 0
        self.frame_1.update()
        self.frame_2.update()
        root.update()

    def tela(self):
        
        self.root.title("Compilador Simlish")
        self.root.configure(background = "green")
        self.root.geometry("700x500")
        self.root.resizable(True, True)
        self.root.minsize(width = 500, height = 350)

    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, bd = 4, bg = "#DCDCDC", highlightbackground = "grey", highlightthickness = 3)
        self.frame_1.place(relx = 0.02, rely = 0.07, relwidth = 0.96, relheight = 0.55)
        self.frame_2 = Frame(self.root, bd = 4, bg = "#DCDCDC", highlightbackground = "grey", highlightthickness = 3)
        self.frame_2.place(relx = 0.02, rely = 0.70, relwidth = 0.96, relheight = 0.20)

    def chama_analisador(self):
        columns = ('linha', 'posicao', 'token', 'lexema', 'notificacao')
        self.saida = ttk.Treeview(self.frame_2, height = 5, columns = columns, show = 'headings')
        self.saida.heading("linha", text = 'Linha')
        self.saida.heading("posicao", text = 'Posição referente ao início da entrada')
        self.saida.heading("token", text = 'Token')
        self.saida.heading("lexema", text = 'Lexema')
        self.saida.heading("notificacao", text = 'Notificação')

        data = self.codigo_entry.get(1.0, "end-1c")
        data.lower()
        lexer = lex.lex()
        lexer.input(data)

   


        #Tokenizar a entrada para passar para o analisar léxico
        for tok in lexer:
            global erros
            if tok.type == "TEXTO_MF":
                erros += 1
                add_lista_saida(tok, f"Ops... String mal formada!")
            elif tok.type == "VARIAVEL_MF":
                erros += 1
                add_lista_saida(tok, f"Ops... Variável mal formada!")
            elif tok.type == "NUMERO_MF":
                erros += 1
                add_lista_saida(tok, f"Ops... Número mal formado!")
            elif tok.type == "VALOR_NUMINT":
                max = (len(str(tok.value)))
                if (max > 15):
                    erros += 1
                    add_lista_saida(tok, f"Ops... Entrada maior que o limite suportado!")
                else:
                    add_lista_saida(tok, f"")
            elif tok.type == "SE" or tok.type == "SENAO" or tok.type == "ENQUANTO" or tok.type == "PARA" or tok.type == "INTERROMPA" or tok.type == "DEFINE" or tok.type == "LEIA" or tok.type == "ESCREVA" or tok.type == "IFSULDEMINAS" or tok.type == "COMPILADORES" or tok.type == "INICIO" or tok.type == "FIM":
                max = (len(tok.value))
                if (max < 20):
                    if tok.value in reserved:
                        tok.type = reserved[tok.value]
                        add_lista_saida(tok, f"Palavra reservada!") 
                    else:
                        add_lista_saida(tok, f"")

                else:
                    erros += 1
                    add_lista_saida(tok, f"Ops... Tamanho da variável maior que o limite suportado!")
            else:
                add_lista_saida(tok, f"")

        if (saidas[0][3] == "IFSULDEMINAS"):
            if (saidas[1][3] != ";"):
                erros += 1
                self.saida.insert('', tk.END, values = "Falta IFSULDEMINAS no início!")
            else:
                pass
        else:
            erros += 1
            self.saida.insert('', tk.END, values = "Falta IFSULDEMINAS no início!")

        if (saidas[2][3] == "COMPILADORES"):
            if (saidas[3][3] != ";"):
                erros += 1
                self.saida.insert('', tk.END, values = "Falta COMPILADORES no seu algoritmo!")
            else:
                pass
        else:
            erros += 1
            self.saida.insert('', tk.END, values = "Falta COMPILADORES no seu algoritmo!")
        if (saidas[4][3] == "INICIO"):
            if (saidas[5][3] != "{" and saidas[6][3] != "}"):
                erros += 1
                self.saida.insert('', tk.END, values = "Falta INICIO no seu algoritmo!")
            else:
                pass
        else:
            erros += 1
            self.saida.insert('', tk.END, values = "Falta INICIO no seu algoritmo!")
        for tok in erroslexicos:
            add_lista_saida(tok, f"Ops... Esta linguagem não aceita esse caracter.")
        
        tamerroslex = len(erroslexicos)
        if tamerroslex == 0 and erros == 0:
            self.saida.insert('', tk.END, values = "Análise Léxica OK!")
            parser.parse(data)
            tamerrosin = len(errossintaticos)
            if tamerrosin == 0:
                self.saida.insert('', tk.END, values = "Análise Sintática OK!")
            else:
                self.saida.insert('', tk.END, values = "Erro Sintático")
        else:
            self.saida.insert('', tk.END, values = "Ops... Erro Léxico.") 

        for retorno in saidas:
            self.saida.insert('', tk.END, values = retorno)

        self.saida.place(relx = 0.001, rely = 0.01, relwidth = 0.999, relheight = 0.95)

        self.scrollAnalise = ttk.Scrollbar(self.frame_2, orient = 'vertical', command = self.saida.yview)
        self.scrollAnalise.place(relx = 0.979, rely = 0.0192, relwidth = 0.02, relheight = 0.92)
        self.saida['yscrollcommand'] = self.scrollAnalise 

    def botoes(self):
        #Botão para limpar
        self.bt_limpar = Button(text = "Limpar", bd = 2, bg = "#FF6347", font = ('', 11), command = self.limpa_telaentrada)
        self.bt_limpar.place(relx = 0.74, rely = 0.92, relwidth = 0.1, relheight = 0.05)

        #Botão para executar
        self.bt_executar = Button(text = "Executar", bd = 2, bg = "lightgreen", font = ('', 11), command = self.chama_analisador)
        self.bt_executar.place(relx = 0.85, rely = 0.92, relwidth = 0.1, relheight = 0.05)

        #Espaço (label) para a entrada do código
        self.lb_codigo = Label(text = "Código fonte", bg = "white", font = ('', 12))
        self.lb_codigo.place(relx = 0.001, rely = -0.001, relwidth = 0.2, relheight = 0.07)

        #Espaço (label) para a Análise Léxica e Análise Sintática
        self.lb_analise = Label(text = "Análise Léxica e Análise Sintática", bg = "white", font = ('', 12))
        self.lb_analise.place(relx = 0.001, rely = 0.62, relwidth = 0.5, relheight = 0.07)

        self.codigo_entry = tk.Text(self.frame_1)
        self.codigo_entry.place(relx = 0.001, rely = 0.001, relwidth = 0.995, relheight = 0.995)

        self.scroll_bar = ttk.Scrollbar(self.frame_1, orient = 'vertical', command = self.codigo_entry.yview)
        self.scroll_bar.place(relx = 0.982, rely = 0.0019, relwidth = 0.99, relheight = 0.99)
        self.codigo_entry['yscrollcommand'] = self.scroll_bar

    def Menus(self):
        menubar = Menu(self.root)
        self.root.config(menu = menubar)
        filemenu = Menu(menubar)
        filemenu2 = Menu(menubar)

        def Quit(): self.root.destroy()

        def onOpen():
            tf = fd.askopenfilename(
                initialdir = "C:/Users/MainFrame/Desktop",
                title = "Abrir arquivo de texto",
                filetypes = (("Arquivos de texto", "*.txt"),)
            )
            tf = open(tf, 'r')
            entrada = tf.read()
            self.codigo_entry.insert(END, entrada)
            tf.close()
        
        def onSave():
            files = filedialog.asksaveasfile(mode = 'w', defaultextension = ".txt")
            t = self.codigo_entry.get(0.0, END)
            files.write(t.rstrip())
        
        def tokens():
            newWindow = Toplevel(root)
            newWindow.title("Tabela de Tokens")
            newWindow.configure(background = "white")
            newWindow.geometry("800x800")
            newWindow.resizable(True, True)
            newWindow.minsize(width = 550, height = 350)

            newWindow = ttk.Treeview(newWindow, height = 3, column = ('col1', 'col2', 'col3', 'col4'))
            newWindow.heading("#0", text='')
            newWindow.heading("#1", text='Tokens')
            newWindow.heading("#2", text='Lexemas')
            newWindow.heading("#3", text='Expressão Regular')
            newWindow.heading("#4", text='Descrição')

            newWindow.column("#0", width = 1, stretch = NO)
            newWindow.column("#1", width = 50,)
            newWindow.column("#2", width = 200)
            newWindow.column("#3", width = 125)
            newWindow.column("#4", width = 125)

            newWindow.place(relx = 0.001, rely = 0.01, relwidth = 0.999, relheight = 0.95)

            newWindow.insert("", 1, text = "", values = ("IFSULDEMINAS", "IFSULDEMINAS", "IFSULDEMINAS", "Palavra reservada 'IFSULDEMINAS'"))
            newWindow.insert("", 2, text = "", values = ("INICIO", "INICIO", "INICIO", "Palavra reservada 'INICIO'"))
            newWindow.insert("", 3, text = "", values = ("COMPILADORES", "COMPILADORES", "COMPILADORES", "Palavra reservada 'COMPILADORES'"))
            newWindow.insert("", 4, text = "", values = ("FIM", "FIM", "FIM", "Palavra reservada 'FIM'"))
            newWindow.insert("", 5, text = "", values = ("SE", "SE", "SE", "Palavra reservada 'SE'"))
            newWindow.insert("", 6, text = "", values = ("SENAO", "SENAO", "SENAO", "Palavra reservada 'SENAO'"))
            newWindow.insert("", 7, text = "", values = ("ENQUANTO", "ENQUANTO", "ENQUANTO", "Palavra reservada 'ENQUANTO'"))
            newWindow.insert("", 8, text = "", values = ("PARA", "PARA", "PARA", "Palavra reservada 'PARA'"))
            newWindow.insert("", 9, text = "", values = ("INTERROMPA", "INTERROMPA", "INTERROMPA", "Palavra reservada 'INTERROMPA"))
            newWindow.insert("", 10, text = "", values = ("DEFINE", "DEFINE", "DEFINE", "Palavra reservada 'DEFINE'"))
            newWindow.insert("", 11, text = "", values = ("LEIA", "LEIA", "LEIA", "Palavra reservada 'LEIA'"))
            newWindow.insert("", 12, text = "", values = ("ESCREVA", "ESCREVA", "ESCREVA", "Palavra reservada 'ESCREVA'"))
            newWindow.insert("", 13, text = "", values = ("BOOLEANO", "VERDADEIRO,FALSO", "VERDADEIRO|FALSO", "Palavra reservada 'BOOLEANO'"))
            newWindow.insert("", 14, text = "", values = ("OP_ARIT", "+, -, /, *", "+, -, /, *", "+, -, /, *", "+, -, /, *", "Operadores aritméticos"))
            newWindow.insert("", 15, text = "", values = ("OP_REL", "<, >, <>, <=, >=, ==", "<, >, <>, <=, >=, ==", "Operadores relacionais"))
            newWindow.insert("", 16, text = "", values = ("OP_ATRIBUI", ":=", ":=", "Operador de 'atribuição'"))
            newWindow.insert("", 17, text = "", values = ("ABRE_CH", "{", "{", "Operador de 'abre chaves'"))
            newWindow.insert("", 18, text = "", values = ("FECHA_CH", "}", "}", "Operador de 'fecha chaves'"))
            newWindow.insert("", 19, text = "", values = ("ABRE_CLT", "[", "[", "Operador de 'abre colchetes'"))
            newWindow.insert("", 20, text = "", values = ("FECHA_CLT", "]", "]", "Operaode de 'fecha colchetes'"))
            newWindow.insert("", 21, text = "", values = ("ABRE_P", "(", "(", "Operador de 'abre parênteses'"))
            newWindow.insert("", 22, text = "", values = ("FECHA_P", ")", ")", "Operador de 'fecha parênteses'"))
            newWindow.insert("", 23, text = "", values = ("COMENT", "¨", "¨", "Operador de 'comentário em linha'"))
            newWindow.insert("", 24, text = "", values = ("VIRGULA", ",", ",", "Operador de execução 'vírgula'"))
            newWindow.insert("", 25, text = "", values = ("OP_LOGICO", "E, OU,", "E|OU", "Operador lógico (“e”, “ou”)"))
            newWindow.insert("", 26, text = "", values = ("DELIMITADOR", ";", ";", "Operador de 'delimitador (fim delinha)'"))
            newWindow.insert("", 27, text = "", values = ("VAR", "temperatura, mensagem, mensagem2,", "[a-z][a-z_0-9]*", "Variável"))
            newWindow.insert("", 28, text = "", values = ("VALOR_NUMINT", "0, 1, 2, 3", "4, 5, 6", "Digito numérico 'INTEIRO'"))
            newWindow.insert("", 29, text = "", values = ("VALOR_TEXTO", "'Ciência da Computação'", "REGEX NÃO PERMITIDO", "Texto"))
            newWindow.insert("", 30, text = "", values = ("VALOR_NUMDEC", "0.1, 0.01, 0.001", "3.14, 3.141", "Digito numérico 'DECIMAL'"))
            newWindow.insert("", 31, text = "", values = ("ASPAS", "", "", "Operador de execução 'aspas'"))
    
         

            label.pack(pady = 10)
            mainloop()
        
        menubar.add_cascade(label = "Arquivo", menu = filemenu)
        menubar.add_cascade(label = "Tabela de Tokens", menu = filemenu2)

        filemenu.add_command(label = "Abrir Script", command = onOpen)
        filemenu.add_command(label = "Salvar como", command = onSave)
        filemenu.add_separator()
        filemenu.add_command(label = "Sair", command = Quit)
        filemenu2.add_command(label = "Tokens", command = tokens)

Application()
    







