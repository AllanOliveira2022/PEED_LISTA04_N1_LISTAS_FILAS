from Lista_Dupla_Base import ListaEncadeadaDupla
lista = ListaEncadeadaDupla()
def main():
    inforContato = {}
    opc = 0
    while opc != 4:
        print("")
        print("")
        print("Menu: ")
        print("1 -- Inserir contato")
        print("2 -- Buscar contato")
        print("3 -- Remover contato")
        print("4 -- Sair")
        opc = int(input("==: "))
   
        if opc == 1:
            print("Informações do contato: ")
            nome = input("Nome: ")
            num = int(input("Número: "))
            inforContato = {"nome" : nome, "numero" : num}
            lista.inserir_fim(inforContato)
            print(f"Pronto!!\n O contato {nome} foi inserido")
        if opc == 2:
            listaBusca = []
            contatoBuscar = input("Digite o nome do contato que quer pesquisar: ")
            while not lista.esta_vazia():   
                contato = lista.remover_inicio()
                if contato["nome"] == contatoBuscar:
                    print("Informações do contato: ")
                    print(f"Nome: {contato['nome']}")
                    print(f"Número: {contato['numero']}")
                else:
                    print("Contato não encontrado !")
                listaBusca.append(contato)
            for i in listaBusca:
                lista.inserir_fim(i)    
                 
        if opc ==  3:
            listaRemove = []
            contatoRemove = input("Digite o nome do contato que você deseja apagar: ")
            while not lista.esta_vazia():
                cont = lista.remover_inicio()
                if not cont['nome'] == contatoRemove:
                    listaRemove.append(cont)
                elif cont['nome'] == contatoRemove :
                    print(f"Contato '{cont['nome']}' foi apagado !")
            for com in listaRemove:
                lista.inserir_fim(com)                              
                
        if opc == 4:
            print("Finalizando...")
            break


main()     
