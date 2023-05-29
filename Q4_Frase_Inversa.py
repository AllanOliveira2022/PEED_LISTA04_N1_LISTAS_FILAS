from Fila_Base import Fila
fila = Fila()
def inversa(frase):
    for palavra in frase:
        aux = ''.join(reversed(palavra))
        fila.enfileirar(aux)
    return fila.mostrar_fila()

frase = input("Digite uma frase: ").split()
frase_inversa = inversa(frase)
if frase == frase_inversa:
    print("A frase é um palíndromo !")
else:
    print("A frase não é um palíndromo !")
   