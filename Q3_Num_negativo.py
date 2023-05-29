from Fila_Base import Fila
fila = Fila()
def main():
    num = 0
    print("Digite números positivos: ")
    while num >= 0:
        num = int(input("Digite um número: "))
        if num >= 0:
            fila.enfileirar(num)
    if num < 0:
        print("Um número negativo foi inserido !!")
    print("Veja a lista completa: ")
    print(fila.mostrar_fila())

main()        
