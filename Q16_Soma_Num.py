def main():
    listaNum = []
    soma =0
    for i in range(0,5):
        num = int(input("Digite um número: "))
        listaNum.append(num)
    print(listaNum)
    for numer in listaNum:
        soma += numer
    print("A soma dos números é: ")
    print(soma)
main()    