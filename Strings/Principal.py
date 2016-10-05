import StringUtil as S
texto = input("digite um texto aqui:")
letra = input("digite a letra a ser encontrada:")
S.output(texto)
S.output("tamanho:",S.tamanho(texto))
S.output("texto maiusculo:\n",S.maiuscula(texto))
S.output("texto minusculo:\n",S.minuscula(texto))
S.output(encontraLetra(texto,letra))