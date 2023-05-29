def main():
    listaPalavra = []
    palavraLonga =""
    for i in range(0,3):
        palavra = input("Digite uma palavra: ")
        listaPalavra.append(palavra)

    for string in listaPalavra:
        if len(string) > len(palavraLonga):
            palavraLonga = palavra 
    print("A palavra mais longa é: ")
    print(palavraLonga)

main()    