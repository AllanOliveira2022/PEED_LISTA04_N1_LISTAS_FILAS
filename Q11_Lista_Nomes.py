from Lista_Dupla_Base import ListaEncadeadaDupla
lista = ListaEncadeadaDupla()
def ordenar(nomes):
    nomes.sort() #função do python que ordena valores(Nesse caso em ordem alfabetica)
    for no in nomes:
        lista.inserir_fim(no)
    return lista.mostrar_lista()    
print("Preencha com os nomes: ")
nome = []
for i in range(0,3):
    nome.append(input(f"Nome {i + 1}: "))
nomeOrdenado = ordenar(nome)  
print("Lista em ordem alfabética: ")
print(nomeOrdenado)  
