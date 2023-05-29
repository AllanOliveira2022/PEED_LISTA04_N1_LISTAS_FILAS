def main():
    listaString = []
    novaLista = []
    for i in range(0,5):
        string = input("Digite uma palavra: ")
        listaString.append(string)
    print("Lista que você digitou: ")
    print(listaString)
    tam =0
    for palavra in listaString:
        tam += len(palavra)
        if tam > 5:
            novaLista.append(palavra)             
    print("Nova lista com palavras com mais de 5 letras: ")
    print(novaLista)

main()    