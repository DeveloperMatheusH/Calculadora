#Codigo Calculadora Python

import tkinter as tk

class Calculadora:
    def __init__(self, master):


        self.master = master
        self.master.title("Calculadora")

        
        self.entrada_var = tk.StringVar()
        entrada = tk.Entry(self.master, textvariable=self.entrada_var, font=('Arial', 14), bd=20, insertwidth=4, width=14, justify='right')
        entrada.grid(row=0, column=0, columnspan=4, pady=10)  # Adicionado pady=10 para espaçamento

        # Botões
        botoes = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C', 'CE'
        ]

        row_val = 1
        col_val = 0

        for botao in botoes:
            tk.Button(self.master, text=botao, padx=10, pady=10, font=('Arial', 14), command=lambda b=botao: self.clique_bota(b)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def clique_bota(self, valor):

        if valor == '=':
            try:
                resultado = str(eval(self.entrada_var.get()))
                self.entrada_var.set(resultado)
            except:
                self.entrada_var.set("Erro")

        elif valor == 'C':
            self.entrada_var.set('')
        elif valor == 'CE':
            current_text = self.entrada_var.get()
            self.entrada_var.set(current_text[:-1] if current_text else '')


        else:
            current_text = self.entrada_var.get()
            self.entrada_var.set(current_text + str(valor))



# Criar a janela principal
root = tk.Tk()
calc = Calculadora(root)
root.mainloop()