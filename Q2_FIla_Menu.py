from Fila_Base import Fila
fila = Fila()
def main():
    while True:
        print("Menu: ")
        print("1 == Adicionar valor\n2 == Remover valor\n3 == Mostrar tamanho\n4 == Mostrar fila\n 5 == SAIR")
        opc = int(input("== : "))
        match opc:
            case 1: 
                valor = input("Digite o valor: ")
                fila.enfileirar(valor)
                print(f"O valor {valor} foi inserido !")
            case 2:
                num = fila.remover()
                print(f"O número {num} foi removido !!")
            case 3:
                print(f"O tamanho da fila é: {fila.mostrar_tamanho()}")
            case 4: 
                print("Números da fila: ")
                print(fila.mostrar_fila())
            case 5:
                print("Finalizando...")
                break

main()
