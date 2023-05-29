def main():
    listaNum1 = []
    listaNum2 = []
    listaNumUnidos = []

    print("Digite a primeira lista de números: ")
    for i in range(0,5):
        num = int(input("Digite um número: "))
        listaNum1.append(num)
    print("Lista de números 1: ")
    print(listaNum1)    
    print("Digite a segunda lista de números: ")
    for i in range(0,5):
        num2 = int(input("Digite um número: "))
        listaNum2.append(num2)
    print("Lista de números 2: ")
    print(listaNum2)

    for valor in listaNum1:
        if valor in listaNum2:
            listaNumUnidos.append(valor)

    print("LISTA DOS NÚMEROS QUE ESTÃO EM AMBAS: ")
    print(listaNumUnidos)


main()    