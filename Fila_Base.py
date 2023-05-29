class Item:
    def __init__(self,valor):
        self.valor= valor
        self.proximo = None
class Fila:
    def __init__(self):
        self.frente= None
        self.calda= None
        self.tamanho= 0
    def esta_vazia(self):
        return self.frente is None
    def enfileirar(self,valor):
        novo_item = Item(valor)
        if self.esta_vazia():
            self.frente= novo_item
            self.calda= novo_item
        else:
            self.calda.proximo= novo_item
            self.calda= novo_item
        self.tamanho+= 1
        
    def remover(self):
        if self.esta_vazia() :
            raise IndexError("A fila está vazia !")
        valor= self.frente.valor
        self.frente= self.frente.proximo
        if self.frente is None:
            self.calda= None
        self.tamanho -= 1
        return valor
    def mostrar_tamanho(self):
        return self.tamanho   
    
    def mostrar_frente(self):
        if self.esta_vazia():
            raise IndexError("A fila está vazia !")
        return self.frente.valor
    def mostrar_fila(self):
        if self.esta_vazia() == True:
            raise IndexError("A fila está vazia !")
        else:
            FilaLista = []
            while not self.esta_vazia() :
                valor = self.remover()
                FilaLista.append(valor)
        return FilaLista