paisA = eval(input("quantos habitantes tem o pa�s A?"))
taxaA = eval(input("qual a taxa de crescimento do pa�s A?"))
paisB = eval(input("quantos habitantes tem o pa�s B?"))
taxaB = eval(input("qual a taxa de crescimento do pa�s B?"))
anos = 0 
while paisA < paisB :
	paisA = int(paisA + ((paisA/100)*taxaA))
	paisB = int(paisB + ((paisB/100)*taxaB))
	anos = anos + 1 
	if paisA >= paisB :
		print("passaram",anos,"anos, o pa�s A agora tem",paisA,"habitantes e o pa�s B",paisB,"habitantes")

