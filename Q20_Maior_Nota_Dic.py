def main():
    alunos = []
    dicio = {}
    maiorNota = 0
    nomeAluno = ''
    print("Digite o nome do aluno e sua nota: ")
    for i in range(0,2):
        nome = input(f'Digite o nome do aluno {i+1}: ')
        nota = int(input("Nota: "))
        dicio = {"Nome" : nome, "Nota" : nota}
        alunos.append(dicio)
    print("Lista dos dicionários dos alunos: ")
    print(alunos)

    for dic in alunos:
        notas = dic["Nota"]
        nomes = dic["Nome"]
        if notas > maiorNota:
            maiorNota = notas 
            nomeAluno = nomes 
          

    print("O aluno com a maior nota: ")
    print(f"Nome: {nomeAluno} --- Nota: {maiorNota} !!")

main()    