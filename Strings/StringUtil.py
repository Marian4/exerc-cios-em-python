def output(texto):
    print("texto:",texto)
def tamanho(texto):
    tamanho = len(texto)
    return tamanho
def maiuscula(texto):
    maiuscula = upper(texto)
    return maiuscula
def minuscula(texto):
    minuscula = lower(texto)
    return minuscula
def encontraLetra(texto,letra):
    for i in texto:
        repetições = 0
        if i == letra:
            repetições += 1
    print("a letra %s foi encontrada %i vezes no texto"%(letra,repetições))
