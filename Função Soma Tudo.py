def soma(x):
  if x == 1 or x == 0:
    return x
  return soma(x-1)+x
numero = eval(input("Digite um número:"))
print(soma(numero))
