import random
numeros= [1,2,3,4,5]
alunos= {"1":"Jose","2":"Maria", "3":"Alice"}
mensagemprova4=""

print("Seja bem vindo(a) ao Programa da Prova 4")
print("Lista é um conjunto de valores")
print("Dicionario é constituido por uma chave e valor. A chave em um dicionario normal seria a palavra e o valor seria o significado")
print("Estou pronto para manipular listas e dicionários na prova!")
print()
sorteados= []
for i in range(20):
  x= random.randint(1,100)
  sorteados.append(x)
  
for j in range (20):
  print("o valor da linha %i "%j,end="")
  print("é",sorteados[j])
mensagemprova4 += "Prova sobre manipulação de listas e dicionários."
print(len(mensagemprova4))
mensagemprova4 += " Prova  de  número  4."


