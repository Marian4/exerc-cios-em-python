import random
import time
def carregando():
    print("Carregando...")
    time.sleep(1)
print("Bem vindo ao jogo de adivinhação!")
print("Regras:\nA cada nova jogada,haverá um número de 1 a 100 que será escolhido de forma aleatória.\nVocê não saberá que número é esse.\nVocê terá 3 chances para tentar adivinhar o número.\n")
jogar = eval(input("(1)Jogar (2)Sair:"))
carregando()
print()
while jogar == 1:
    num = random.randint(1,100)
    contador = 0
    resposta = eval(input("Adivinhe o número:"))
    while resposta!= num:
        if contador == 2:
            print("Aah,você perdeu.O número era",num)
            jogar = eval(input("(1)Jogar (2)Sair:"))
            carregando()
            print()
            break
        elif resposta < num:
            if resposta + 20 >= num:
                print("O número escolhido é um pouco maior.tente novamente.")
                resposta = eval(input("Adivinhe o número:"))
            elif resposta + 20 < num:
                print("O número escolhido é bem maior.Tente novamente.")
                resposta = eval(input("Adivinhe o número:"))
        elif resposta > num:
            if resposta - 20 > num:
                print("O número é bem menor.Tente novamente.")
                resposta = eval(input("Adivinhe o número:"))
            elif resposta - 20 <= num:
                print("O número escolhido é um pouco menor.Tente novamente.")
                resposta = eval(input("Adivinhe o número:"))
        contador += 1
    if resposta == num:
        print("Parabéns!Você venceu o jogo.")
        jogar = eval(input("(1)Jogar Novamente (2)Sair:"))
        carregando()
        print()
      
print("Você saiu do jogo.")
