class Item:
    def __init__(self,dado):
        self.valor = dado
        self.prev = None
        self.proximo = None

class ListaEncadeadaDupla:
    def __init__(self):
        self.frente = None
        self.calda = None
        self.tamanho = 0
    
    def inserir_inicio(self,valor):
        novo_valor = Item(valor)
        if self.frente is None:
            self.frente = novo_valor
            self.calda = novo_valor
        else:
            novo_valor.proximo = self.frente
            self.frente.prev = novo_valor
            self.frente = novo_valor
        self.tamanho += 1
    def inserir_fim(self,valor):
        novo_valor = Item(valor)
        if self.calda is None:
            self.frente = novo_valor
            self.calda = novo_valor
        else:
            novo_valor.prev = self.calda
            self.calda.proximo = novo_valor
            self.calda = novo_valor
        self.tamanho += 1
    def remover_inicio(self):
        if self.frente is None:
            raise IndexError("A lista está vazia !!")
        valor = self.frente.valor
        if self.frente == self.calda:
            self.frente = None
            self.calda = None
        else:
            self.frente = self.frente.proximo
            self.frente.prev = None
        self.tamanho -= 1   
        return valor 
    def remover_fim(self):
        if self.frente is None:
            raise IndexError("A lista está vazia !!")
        else:
            valor = self.calda.valor
            self.calda = self.calda.prev
            self.calda.proximo = None
        self.tamanho -= 1
        return valor
    def mostrar_tamanho(self):
        return self.tamanho
    def esta_vazia(self):
        return self.frente == None
    def mostrar_lista(self):
        listaAux = []
        while not self.esta_vazia():
            valor = self.remover_inicio()
            listaAux.append(valor)
        return listaAux    

lista = ListaEncadeadaDupla()
lista.inserir_inicio(10)
lista.inserir_fim(20)
lista.inserir_fim(30)
print("Vazia?:", lista.esta_vazia())
print("tamanho: ",lista.mostrar_tamanho())
print("REmover frente: ",lista.remover_inicio())
print("Lista: ")
print(lista.mostrar_lista())
