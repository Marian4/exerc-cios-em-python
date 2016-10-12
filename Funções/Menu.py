import Cor 
lista = []
opção = eval(input("O que você quer fazer?(1)Adicionar uma cor/(2)Listar cores/(3)Encerrar programa."))
if opção == 2:
	print("Ainda não foi adicionada nenhuma cor a caixa de cores.\n")
	opção = eval(Input("O que você quer fazer?(1)Adicionar uma cor/(2)Listar cores/(3)Encerrar programa."))
while opção == 1:
	cor = input("\nDigite o nome da cor:")
	Cor.AddCor(lista,cor)
	opção = eval(input("\nO que você quer fazer?(1)Adicionar uma cor/(2)Listar cores/(3)Encerrar programa."))
	while opção == 2:
		Cor.ListarCores(lista)
		opção = eval(input("\nO que você quer fazer?(1)Adicionar uma cor/(2)Listar cores/(3)Encerrar programa."))
print("Programa encerrado.")
