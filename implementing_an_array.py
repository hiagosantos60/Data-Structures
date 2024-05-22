class Array:
    #Inicia a classe Array, define o comprimento e define um dicionário que armazena os elementos.
    def __init__(self): 
        self.length = 0
        self.data = {}

    #Método __str__ retorna uma representação em string do dicionário.
    def __str__(self):
        return str(self.__dict__)
    
    #Recebe um índice como entrada e retorna o elemento que está nesse índice
    def get(self, index):
        return self.data[index]
    
    #Adiciona um novo elemento no final do Array, ou seja, é add ao self.data
    def push(self, item):
        self.data[self.length] = item
        self.length += 1

    #remove o último item da array, armazena o último item em 'ultimo_item' e reduz o array em 1 unidade
    def pop(self):
        ultimo_item = self.data[self.length - 1]
        del self.data[self.length -1]
        self.length -= 1
        return ultimo_item
    
    #remove o item do índice recebido, armazena o item no deleteitem e reduz a array em 1.
    def delete(self, index):
        deleteitem = self.data[index]
        for i in range(index, self.length -1):
            self.data[i] = self.data [i + 1]
        del self.data[self.length -1]
        self.length -= 1
        return deleteitem
    
arr = Array()
#Área para testes / tests area
print(arr)