from Lista_Base import Lista
lista = Lista()
def inversa(listaAtual):
    for valor in listaAtual:
        lista.inserir_fim(valor)
    mostrar = []
    while not lista.esta_vazia():  
        num = lista.remover_fim()
        mostrar.append(num)
    return mostrar 

listaNum = []
for i in range(0,5):
    listaNum.append(input("Digite um valor: "))
listaInversa = inversa(listaNum)   
print("Veja a lista inversa: ")
print(listaInversa)     
    
   