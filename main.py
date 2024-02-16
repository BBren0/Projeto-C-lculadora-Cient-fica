import tkinter as tk
import math 


botao_config ={
    "bg" : "#242742",
    "fg" : "#d1d2de",
    "font" : ("Consolas bold",12),
    "height" : "2",
    "width" : "7",
    "relief" : "flat",
    "activebackground" : "#313454"

}

digitos = ["raiz", "x", "C", "n!", "sin", "cos", "tan", " sin-¹", "cos-¹", "tan-1"]

deg = 1
inversa_deg = 1 
cnt = 0

class Calculadora:
    def __init__(self, master) -> None: # Master faz referência a janela base da aplicação
        self.master = master

        self.displayFrame = tk.Frame(self.master)
        self.displayFrame.pack()

        self.buttonsFrame = tk.Frame(self.master)
        self.buttonsFrame.pack()

        self.output = tk.Entry(self.displayFrame, 
                               width = 30, relief="sunken", bd = 3,
                               font = ("Consolas bold",17), fg="#c9c9c5", bg="#242742")
        self.output.grid(row = 0, column = 0)

        self.converte = tk.Button(self.displayFrame,
                                  botao_config, width = 3, height = 0,
                                  text = "DEG",  bg = "#351242", command = self.degreesRadians)

        self.converte.grid(row = 0, column = 1)

        self.criarBotoes()


    def criarBotoes(self):
        self.botoes = [
            ["Raiz", "x", "**", "(", ")", "/"],
            ["sin", "cos", "7", "8", "9", "+"],
            ["sin-¹", "cos-¹", "4", "5", "6","-"],
            ["tan", "tang-¹", "1", "2", "3", "*"],
            ["n!", "n", ".", "0", "=", "c"]
        ]
        for linha in range(len(self.botoes)):
            for coluna in range(len(self.botoes[linha])):
              texto =   self.botoes [linha][coluna]
              
              # lambda x,y : expressão que o lambda vai ativar
              b = tk.Button(self.buttonsFrame, botao_config, text = texto, command = lambda x = texto : self.acaoBotoes(x))
              b.grid(row = linha, column = coluna)


    def acaoBotoes(self, texto):
        # O lambda  a cada operação sobreescreve o lambda anterior  
        global deg 
        global inversa_deg
        if texto != "=":
            if texto not in digitos:
                self.output.insert('end', texto)
            else:
                if texto == "Raiz":
                    self.addValor(math.sqrt(float(self.output.get())))
        else:
           self.addValor(eval(self.output.get())) # Eval é uma função que captura duas strings e as soma
      
    def addValor(self, valor):
        self.output.delete(0,'end')
        self.output.insert('end', )




    def degreesRadians(self):
        global deg
        global inversa_deg
        global cnt

        if (cnt == 0):
            deg = math.pi / 180
            inversa_deg = 180 / math.pi
            self.converte['text'] = "RAD"
            cnt  = 1
        else:
            deg = 1 
            inversa_deg = 1
            self.converte['text'] = "DEG"
            CNT = 0


            
raiz = tk.Tk()

Calculadora(raiz)

raiz.mainloop()