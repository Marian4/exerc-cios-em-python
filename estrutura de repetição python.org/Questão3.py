nome = input("nome(mais de 3 caracteres):")
while len(nome) <= 3 :
	nome = input("nome(mais de 3 caracteres):")
idade = eval(input("idade:"))
while idade<=0 or idade>150 :
	print("essa idade n�o � v�lida!")
	print("")
	idade = eval(input("idade:"))
sal�rio = eval(input("sal�rio:"))
while sal�rio <= 0 :
	print("seu sal�rio deve ser maior que 0")
	sal�rio = eval(input("sal�rio:"))
sexo = eval(input("sexo 1-F 2-M:"))
while sexo != 1 and sexo != 2 :
	sexo = eval(input("sexo 1-F 2-M:"))
estado_civil = eval(input("estado civil 1-S 2-C 3-V 4-D:"))
while estado_civil < 1 or estado_civil > 4 :
	estado_civil = eval(input("estado civil 1-S 2-C 3-V 4-D:"))