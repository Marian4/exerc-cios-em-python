import string
def output(*textos):
    print(*textos)
def tamanho(texto):
    tamanho = len(texto)
    return tamanho
def maiuscula(texto):
    maiuscula = texto.upper()
    return maiuscula
def minuscula(texto):
    minuscula = texto.lower()
    return minuscula
def encontraLetra(texto,letra):
    for i in texto:
        repetições = 0
        if i == letra:
            repetições += 1
    if repetições == 0:
	    print("Letra não encontrada.")
	elif repetições == 1:
	    print("A letra %s foi encontrada 1 vez no texto."%letra)
	else:
	    print("A letra %s foi encontrada %i vezes no texto"%(letra,repetições))
