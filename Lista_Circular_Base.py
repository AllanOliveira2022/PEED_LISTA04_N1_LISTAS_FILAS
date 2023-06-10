class Item:
    def __init__(self,valor: object = None, anterior: 'Item' = None, proximo: 'Item' = None):
        self.valor = valor
        self.proximo = proximo
        self.anterior = proximo
    def __str__(self):
        return str(self.valor)    
        
class ListaCircular:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0
    def inserir_inicio(self,valor):
        novo_item = Item(valor)
        if self.inicio is None:
            self.inicio = self.fim = novo_item
        else:
            novo_item.proximo = self.inicio
            self.inicio = novo_item
            novo_item.proximo.anterior = novo_item
            self.inicio.anterior = self.fim
            self.fim.proximo = self.inicio
        self.tamanho += 1
        
    def inserir_fim(self,valor):
        novo = Item(valor)
        if self.inicio is None:
            self.inicio = self.fim = novo
        else:
            novo.anterior = self.fim
            novo.anterior.proximo = novo
            self.fim = novo
            self.fim.proximo = self.inicio
            self.inicio.anterior = self.fim
        self.tamanho += 1 
               
    def remover_inicio(self):
        if self.inicio is None:
            print("A lista está vazia !!")
            return
        if self.inicio == self.fim:
            self.inicio = self.fim = None
        else:
            carga =self.inicio.valor
            self.inicio = self.inicio.proximo
            self.inicio.anterior = self.fim
            self.fim.proximo = self.inicio
        self.tamanho -= 1
        return carga
        
    def remover_fim(self):
        if self.inicio is None:
            print("A lista está vazia !!")
            return
        if self.inicio == self.fim:
            self.inicio = self.fim = None
        else:
            carga = self.fim.valor
            self.fim = self.fim.anterior
            self.fim.proximo = self.inicio
            self.inicio.anterior = self.fim
        self.tamanho -= 1
        return carga
        
    def mostrar_inicio(self):
        return self.inicio.valor
    def mostrar_fim(self):
        return self.fim.valor
    def mostrar_lista(self):
        listaAux = []
        if self.inicio is None:
            print("A lista está vazia !!")
            return
        atual: 'Item' = self.inicio
        listaAux.append(str(atual))
        while atual is not self.fim:
            listaAux.append(str(atual.proximo))
            atual = atual.proximo
        return listaAux 