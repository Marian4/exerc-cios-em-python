paisA = 80000
paisB = 200000
anos = 0 
while paisA < paisB :
	paisA = int(paisA + ((paisA/100)*3))
	paisB = int(paisB + ((paisB/100)*1.5))
	anos = anos + 1 
	if paisA >= paisB :
		print("passaram",anos,"anos, o país A agora tem",paisA,"habitantes e o país B",paisB,"habitantes")

