paisA = eval(input("quantos habitantes tem o país A?"))
taxaA = eval(input("qual a taxa de crescimento do país A?"))
paisB = eval(input("quantos habitantes tem o país B?"))
taxaB = eval(input("qual a taxa de crescimento do país B?"))
anos = 0 
while paisA < paisB :
	paisA = int(paisA + ((paisA/100)*taxaA))
	paisB = int(paisB + ((paisB/100)*taxaB))
	anos = anos + 1 
	if paisA >= paisB :
		print("passaram",anos,"anos, o país A agora tem",paisA,"habitantes e o país B",paisB,"habitantes")

