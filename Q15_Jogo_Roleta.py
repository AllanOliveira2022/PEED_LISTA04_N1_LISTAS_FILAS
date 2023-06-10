from Lista_Circular_Base import ListaCircular
import random
import time
lista = ListaCircular()
def main():
    listaAux = []
    print("Jogo da roleta :")
    print("A roleta tem números de 20 a 30: ")
    #criando a roleta
    for num in range(20,31):
        lista.inserir_fim(num)
        
        
    palpite = int(input("Diga qual número você acha que vai cair: "))
    print("Girando a roleta...")
    numSort = random.choice(lista)

    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    
    print(f"O número da roleta foi: {numSort}")
    if palpite == numSort:
        print("Parabéns !!!\nVocê acertou !!!")
    else:
        print("Não foi dessa vez... \nGire a roleta de novo !")    
    
    
    
main()    