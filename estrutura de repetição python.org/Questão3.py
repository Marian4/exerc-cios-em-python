nome = input("nome(mais de 3 caracteres):")
while len(nome) <= 3 :
	nome = input("nome(mais de 3 caracteres):")
idade = eval(input("idade:"))
while idade<=0 or idade>150 :
	print("essa idade não é válida!")
	print("")
	idade = eval(input("idade:"))
salário = eval(input("salário:"))
while salário <= 0 :
	print("seu salário deve ser maior que 0")
	salário = eval(input("salário:"))
sexo = eval(input("sexo 1-F 2-M:"))
while sexo != 1 and sexo != 2 :
	sexo = eval(input("sexo 1-F 2-M:"))
estado_civil = eval(input("estado civil 1-S 2-C 3-V 4-D:"))
while estado_civil < 1 or estado_civil > 4 :
	estado_civil = eval(input("estado civil 1-S 2-C 3-V 4-D:"))