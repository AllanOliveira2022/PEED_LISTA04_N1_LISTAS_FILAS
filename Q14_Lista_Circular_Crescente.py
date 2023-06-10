from Lista_Circular_Base import ListaCircular
lista = ListaCircular()
def main():
    listaAux = []
    print("Ordenar números em ordem crescente: ")
    for i in range(0,3):
        num = int(input("Digite um número: "))
        listaAux.append(num)
    print("Lista não ordenada: ")
    print(listaAux) 
    listaAux.sort()   
    for valor in listaAux:
        lista.inserir_fim(valor)
        
    print("Lista ordenada: ")
    print(lista.mostrar_lista())
main()               