from Lista_Base import Lista
lista = Lista()
def main():
    cliente = []
    infoCliente = {}
    for i in range(0,3):
        nome = input(f"Digite o nome do cliente {i+1}: ")
        num = int(input("Número da conta: "))
        saldo = float(input("Saldo do cliente: "))
        infoCliente = {"Nome" : nome, "Numero" : num, "Saldo" : saldo}
        cliente.append(infoCliente)
    
    #opções
    opc = 0
    while opc != 3:
        print("Qual opção você deseja execultar: \n1 --- Ver todos clientes\n2 --- Pesquisar\n3 --- Sair")
        opc = int(input("==: "))
        if opc == 2:
            nomeP = input("Qual cliente você deseja buscar? :")
            nomeuser =""
            print("VEJA OS DADOS EM TABELA: ")
            print("|   NOME   | NÚMERO CONTA |   SALDO  |")
            for clien in cliente:
                lista.inserir_fim(clien)
            while not lista.esta_vazia():
                userDic = dict(lista.remover_inicio())
                if userDic["Nome"] == nomeP:
                    conta = userDic["Numero"]
                    salduC = userDic["Saldo"]
                    nomeuser = userDic["Nome"] 
                    print("|   ",nomeuser, "   |   ", conta, "   |   R$", salduC,",00   |")     
        if opc == 1:
            print("VEJA OS DADOS EM TABELA: ")
            print("|   NOME   | NÚMERO CONTA |   SALDO  |")
            for clien in cliente:
                lista.inserir_fim(clien)
            while not lista.esta_vazia():
                userDic = dict(lista.remover_inicio())
                conta = userDic["Numero"]
                salduC = userDic["Saldo"]
                nomeuser = userDic["Nome"] 
                print("|   ",nomeuser, "   |   ", conta, "   |   R$", salduC,",00   |")
        if opc == 3:
            break
    print("Encerrando...")    
main()    