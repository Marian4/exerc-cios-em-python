def adicionarSorteado(ListaDeSorteados):
  x=random.randint(1,100)
  ListaDeSorteados.append(x)

def adcionarAluno(dicalunos,matricula,aluno):
  dicalunos[matricula] = aluno
  
def exibirAlunos(dicalunos):
  matriculas = dicalunos.keys()
  for matricula in matriculas:
    print(matricula,end="")
    print("-",dicalunos[matricula])

def buscarAluno(dicalunos, matricula):
  print(dicalunos[matricula])
