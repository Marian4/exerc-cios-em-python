#A recursividade acontece quando uma função chama ela mesma para realizar um proposito

def soma(x):
  if x == 1:
    return 1
  return soma(x-1)+x
print(soma(3))
