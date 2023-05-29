from Fila_Base import Fila
import time #importa a biblioteca/modulo de tempo do python
def main():
    fila = Fila()
    print("Digite os números de indentificação do cliente: ")
    for i in range(0,3):
        num = int(input(f"Cliente {i+1}: "))
        fila.enfileirar(num)
    print("Hora de chamar a fila de clientes !")
    for j in range(0,3):
        time.sleep(5) #vai contar 5 segundos antes de executar a próxima função
        print(f"Chamando o {j+1}º cliente... ")
        print("CÓDIGO: ",fila.remover())
    print("Todos foram chamados !!!")
main()    