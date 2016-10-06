import StringUtil as S
texto = input("digite um texto aqui:")
letra = input("digite a letra a ser encontrada:")
S.output("Texto:",texto)
S.output("tamanho:",S.tamanho(texto))
S.output("Texto maiusculo:\n",S.maiuscula(texto))
S.output("Texto minusculo:\n",S.minuscula(texto))
S.output(S.encontraLetra(texto,letra))
