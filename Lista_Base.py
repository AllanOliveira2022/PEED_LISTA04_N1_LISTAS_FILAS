class Item:
    def __init__(self,num):
        self.valor = num
        self.proximo= None
class Lista:
    def __init__(self):
        self.inicio = None
        self.tamanho = 0
    def esta_vazia(self):
        return self.inicio == None
    def inserir_inicio(self,valor):
        novo_item = Item(valor)
        novo_item.proximo = self.inicio
        self.inicio = novo_item
        self.tamanho += 1
    def inserir_fim(self,valor):
        novo_item = Item(valor)
        if self.esta_vazia():
            self.inicio = novo_item 
        else:
            atual = self.inicio
            while not atual.proximo is None:
                atual = atual.proximo
            atual.proximo = novo_item
            self.tamanho += 1
    def remover_inicio(self):
        if self.esta_vazia():
            raise IndexError("A lista está vazia !!")  
        else: 
            valor = self.inicio.valor
            self.inicio = self.inicio.proximo
            self.tamanho -= 1
        return valor   
    def remover_fim(self):
        if self.esta_vazia():
            raise IndexError("A lista está vazia !!")
        elif self.inicio.proximo is None:
            valor = self.inicio.valor
            self.inicio = None
            self.tamanho -= 1
        else:
            atual = self.inicio
            anterior = None
            while not atual.proximo is None:
                anterior = atual
                atual = atual.proximo
            valor = atual.valor
            anterior.proximo = None
            self.tamanho -= 1
        return valor    
    def mostrar_lista(self):
        mostrar = []
        while not self.esta_vazia():  
            valor = self.remover_inicio()
            mostrar.append(valor)
        return mostrar 
    def mostrar_inicio(self):
        return self.inicio.valor
    def mostrar_fim(self):
        atual = self.inicio
        anterior = None
        while not atual.proximo is None:
            anterior = atual
            atual = atual.proximo
        return atual.valor
    def mostrar_tamanho(self):
        return self.tamanho