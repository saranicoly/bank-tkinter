""" O objetivo desse programa é demonstrar a conta de um usuário em certo banco, onde ele pode gerenciar
    seus depósitos e saques, além de ver o saldo da conta. 
    OBS: O usuário não deve ser capaz de sacar valores que não tem em conta. """


from tkinter import *

janela = Tk()
janela.title("Menu")
janela.geometry("300x270+200+90")
janela['bg'] = "gray"

saldo = 0

def tela1():
	janela_saque = Tk()
	janela_saque.title("Saque")
	janela_saque.geometry("300x270+200+90")
	janela_saque['bg'] = "gray"

	def get_saque():
		global saldo
		try:
			valor_saque = sacar.get()
			valor_saque = int(valor_saque)
			if (saldo) < (valor_saque):
				erro = Label(janela_saque, bg="gray", fg="white", text="Desculpe, você não tem esse saldo em conta").pack()
			elif (valor_saque) <0:
				erro = Label(janela_saque, bg="gray", fg="white", text="Desculpe, Proibido Saque Negativo").pack()
			else:
				saldo = saldo-valor_saque
				mensagem_sucesso = Label(janela_saque, bg="gray", fg="white", text="Pronto, saque feito com sucesso!").pack()
		except ValueError:
			mensagem_erro = Label(janela_saque, bg="gray", fg="white", text="Por favor, insira apenas valores inteiros (sem vírgula)").pack()
		
			
	tinicial = Label(janela_saque, bg="gray", fg="white", text="Por favor, digite o valor que deseja sacar \ne depois clique em OK.\n\n\n\n").pack()
	sacar = Entry(janela_saque)
	sacar.pack()
	botao_ok = Button(janela_saque, text="OK", command=get_saque).pack()
	botao_sair = Button(janela_saque, text="Fechar o Programa", command=quit).pack(side=BOTTOM)


def tela2():
	janela_deposito = Tk()
	janela_deposito.title("Depósitos")
	janela_deposito.geometry("300x270+200+90")
	janela_deposito['bg'] = "gray"

	def get_deposito():
		global saldo
		try:
			valor_deposito = depositar.get()
			valor_deposito = int(valor_deposito)
			if valor_deposito < 0:
				erro = Label(janela_deposito, bg="gray", fg="white", text="Desculpe, você não pode depositar valores negativos.").pack()
			else:
				saldo += valor_deposito
				mensagem_sucesso = Label(janela_deposito, bg="gray", fg="white", text="Parabéns, depósito feito com sucesso!").pack()		
		except ValueError:
			mensagem_erro = Label(janela_deposito, bg="gray", fg="white", text="Por favor, insira apenas valores inteiros (sem vírgula)").pack()

	tinicial = Label(janela_deposito, bg="gray", fg="white", text="Por favor, digite o valor que \ndeseja depositar e clique em OK.\n\n\n\n\n").pack()
	depositar = Entry(janela_deposito)
	depositar.pack()
	botao_ok = Button(janela_deposito, text="OK", command=get_deposito).pack()
	botao_sair = Button(janela_deposito, text="Fechar o Programa", command=quit).pack(side=BOTTOM)


def tela3():
	janela_saldo = Tk()
	janela_saldo.title("Saldo da Conta")
	janela_saldo.geometry("300x270+200+90")
	janela_saldo['bg'] = "gray"


	tinicial = Label(janela_saldo, bg="gray", fg="white", text="Seu saldo atual é de:").pack()
	texto2 = Label(janela_saldo, bg="gray", fg="white", text=(saldo, "reais")).pack()
	botao_sair = Button(janela_saldo, text="Fechar o Programa", command=quit).pack(side=BOTTOM)


def menu():


	tinicial = Label(janela, fg="white", bg="gray", text="Por favor, clique na opção que deseja.\n\n").pack()
	op1 = Button(janela, text="1- Saque", command=tela1, width=20).pack()
	op2 = Button(janela, text="2- Depósito", command=tela2, width=20).pack()
	op3 = Button(janela, text="3- Saldo Atual", command=tela3, width=20).pack()	
	op4 = Button(janela, text="4- Sair", command=quit, width=20).pack()


menu()
janela.mainloop()
